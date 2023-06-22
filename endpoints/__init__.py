# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

__all__ = ["meetings"]
from flask import jsonify, request
from orm.DataModel import MissingRequiredAttributeError, InvalidAttributeError
from sqlalchemy.exc import IntegrityError
from orm import DB
from datetime import datetime, timedelta
import re
from orm import Config


def defaultListQuery(Model):
    query = Model.optimized_query(1)
    objects = query.all()
    data = [obj.todict(1) for obj in objects]
    data = {"data": data}
    return jsonify(data)


def parseISO(dateString):
    match = re.match(
        r"^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})T(?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.\d{0,6})?Z?$",
        dateString
    )
    if match:
        print(f"Input string: {dateString}")
        print(f"Match groups: {match.groups()}")
        return datetime(**{key: int(value) for key, value in match.groupdict().items()})
    else:
        print(f"No match for input string: {dateString}")
        return None


def defaultCreate(Model):
    if request.form is None:
        return jsonify(message="Invalid form data"), 400
    data = {**request.form}
    # Prevent layer 8 problems:
    if "name" not in data:
        return jsonify(message="Meeting has no name"), 400
    if "start_time" not in data:
        return jsonify(message="Meeting has no starting time"), 400
    # Set defaults
    if "duration" not in data:
        data["duration"] = "3600"  # 1hour

    sanitizedData = {
        "name": data["name"],
        "start_time": data["start_time"],
        "duration": data["duration"],
        "mail_owner": data["mail_owner"] if "mail_owner" in data else "",
        "password": data["password"] if "password" in data else ""
    }

    query = Model.query.filter(Model.name == sanitizedData["name"])
    query = Model.optimize_query(query, 1)
    objects = query.all()
    existingMeetings = [obj.todict(1) for obj in objects]

    for existingMeeting in existingMeetings:
        if existingMeeting["start_time"] is None:
            continue
        startTime = parseISO(existingMeeting["start_time"])
        if startTime is None:
            continue
        endTime = startTime + timedelta(seconds=int(existingMeeting["duration"] or "3600"))  # For broken objects in DB
        newMeetingStart = parseISO(sanitizedData["start_time"])
        print(startTime, endTime, newMeetingStart)
        if startTime <= newMeetingStart < endTime:
            return jsonify(conflict_id=existingMeeting["id"]), 409

    try:
        created = Model(props=sanitizedData)
    except MissingRequiredAttributeError as err:
        return jsonify(message=err.args[0]), 400
    except ValueError as err:
        return jsonify(message=err.args[0]), 400
    except InvalidAttributeError as err:
        return jsonify(message=err.args[0]), 400
    DB.session.add(created)
    try:
        DB.session.commit()
    except IntegrityError as err:
        DB.session.rollback()
        return jsonify(message="Object violates database constraints", error=err.orig.args[1]), 400
    ID = created.id
    return jsonify(Model.optimized_query(2).filter(Model.id == ID).first().fulldesc()), 201


def defaultDetailQuery(Model, ID):
    query = Model.query.filter(Model.id == ID)
    query = Model.optimize_query(query, 1)
    obj = query.first()
    if obj is None:
        return jsonify(message="Meeting not found"), 404
    obj = obj.todict(1)
    if obj["id"] != obj["previd"]:
        obj["previd"] = obj["id"]
    obj["max_occupants"] = Config["max_occupants"]
    obj["lobby"] = Config["lobby"]
    return jsonify(obj)


def defaultDelete(Model, ID):
    obj = Model.query.filter(Model.id == ID).first()
    if obj is None:
        return jsonify(message="Meeting not found"), 404
    try:
        DB.session.delete(obj)
        DB.session.commit()
    except IntegrityError as err:
        return jsonify(message="Object deletion would violate database constraints", error=err.args[0]), 400
    return jsonify(message="{} #{} deleted.".format("Meeting", ID))
