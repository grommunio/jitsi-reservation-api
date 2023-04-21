# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from flask_sqlalchemy import SQLAlchemy
from api import app
import os
import sqlite3


def _loadDBConfig():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    sqlitePath = BASE_DIR + '\\db.db'
    if not os.path.exists(sqlitePath):
        # Create sqlite db
        with open("data/schema.sql", "r") as f:
            schema = f.read()
        con = sqlite3.connect(sqlitePath)
        cur = con.cursor()
        for statement in schema.split(";"):
            cur.execute(statement)
        print("SQLite created")
    return "sqlite:///{sqlitePath}".format(sqlitePath=sqlitePath)


DB_uri = _loadDBConfig()
app.config["SQLALCHEMY_DATABASE_URI"] = DB_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(app)
print("Database loaded")
