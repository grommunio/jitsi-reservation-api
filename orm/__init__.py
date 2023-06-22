# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from flask_sqlalchemy import SQLAlchemy
from api import app
import os
import sqlite3
import yaml

_defaultConfig_ = {
    "sqlitePath": "/var/lib/jitsi-reservation-api/reservationDB.db",
    "autodelete": False,
    "deleteStandoff": 3600,
    "max_occupants": 10,
    "lobby": True
}


def _loadDBConfig():
    config = _defaultConfig_
    try:
        with open("config.yaml", "r") as file:
            externalConfig = yaml.load(file, Loader=yaml.SafeLoader) or {}
            config.update(externalConfig)
    except FileNotFoundError:
        print("config.yaml not found")

    sqlitePath = config["sqlitePath"]
    if not os.path.exists(sqlitePath):
        # Create sqlite db
        with open("data/schema.sql", "r") as f:
            schema = f.read()
        con = sqlite3.connect(sqlitePath)
        cur = con.cursor()
        for statement in schema.split(";"):
            cur.execute(statement)
        print("SQLite created")
    return config


Config = _loadDBConfig()
DB_uri = "sqlite:///{sqlitePath}".format(sqlitePath=Config["sqlitePath"])
app.config["SQLALCHEMY_DATABASE_URI"] = DB_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
DB = SQLAlchemy(app)
print("Database loaded")
