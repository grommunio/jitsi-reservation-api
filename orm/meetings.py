# SPDX-License-Identifier: AGPL-3.0-or-later
# SPDX-FileCopyrightText: 2020-2023 grommunio GmbH

from sqlalchemy.dialects.mysql import INTEGER

from . import DB
from .DataModel import DataModel, Id, Text


class Meetings(DataModel, DB.Model):
    __tablename__ = "meetings"

    id = DB.Column("id", INTEGER(10), primary_key=True)
    name = DB.Column("name", DB.VARCHAR(50))
    mail_owner = DB.Column("mail_owner", DB.VARCHAR(50), default="")
    start_time = DB.Column("start_time", DB.VARCHAR(50), default="")
    duration = DB.Column("duration", INTEGER(10), default=3600)
    previd = DB.Column("previd", INTEGER(11), default="")
    password = DB.Column("password", DB.VARCHAR(50), default="")

    _dictmapping_ = (Id(),
                     Text("name", flags="patch"),
                     Text("mail_owner", flags="patch"),
                     Text("start_time", flags="patch"),
                     Text("previd", flags="patch"),
                     Text("password", flags="patch"),
                     Text("duration", flags="patch"),),

    def __repr__(self):
        """Generate string representation of the object."""
        return "<id={} name='{}' startTime={}".format(self.id, self.name, self.start_time)
