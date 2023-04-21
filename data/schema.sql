CREATE TABLE meetings(
id integer primary key autoincrement,
name varchar(50) default '',
mail_owner varchar(50) default '',
previd int(11) default 0,
start_time varchar(50) default '',
duration integer default 3600,
password varchar(50) default ''
);
