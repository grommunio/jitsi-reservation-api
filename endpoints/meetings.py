# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from . import defaultCreate, defaultDetailQuery, defaultDelete, parseISO
from orm.meetings import Meetings
from api import app
from orm import Config
from datetime import timedelta, datetime
from flask import request, jsonify


@app.route('/conference', methods=['POST'])
def createMeeting():
    return defaultCreate(Meetings)


@app.route('/conference/<int:conflict_id>', methods=['GET'])
def getMeeting(conflict_id):
    return defaultDetailQuery(Meetings, conflict_id)


@app.route('/conference/<int:conflict_id>', methods=['DELETE'])
def deleteMeeting(conflict_id):
    delete = request.args["delete"] if "delete" in request.args else False
    query = Meetings.query.filter(Meetings.id == conflict_id)
    query = Meetings.optimize_query(query, 1)
    meeting = query.first()
    if meeting is not None:
        meeting = meeting.todict(1)
    else:
        return jsonify(message="Meeting not found"), 404
    meetingOverTime = parseISO(meeting["start_time"]) + \
                      timedelta(seconds=int(meeting["duration"] or "3600") + int(Config["deleteStandoff"]))
    if Config["autodelete"] or datetime.now() > meetingOverTime or delete:
        return defaultDelete(Meetings, conflict_id)
    return jsonify(message="Meeting not deleted")
