# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from . import defaultCreate, defaultDetailQuery, defaultDelete
from orm.meetings import Meetings
from api import app


@app.route('/conference', methods=['POST'])
def createMeeting():
    return defaultCreate(Meetings)


@app.route('/conference/<int:conflict_id>', methods=['GET'])
def getMeeting(conflict_id):
    return defaultDetailQuery(Meetings, conflict_id)


@app.route('/conference/<int:conflict_id>', methods=['DELETE'])
def deleteMeeting(conflict_id):
    return defaultDelete(Meetings, conflict_id)
