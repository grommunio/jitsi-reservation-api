# How to use the API

This manual demonstrates the correct usage of the API.


## Create a meeting room

Send an `application/x-www-form-urlencoded` encoded HTTP `POST` request to `/conference` with the following request body:

- `name` (required): Name of the conference
- `start_time` (required): Start date and time of the meeting in YYYY-MM-DDThh:mm:ss.000Z format
- `mail_owner` (optional): Mail of the moderator (Default: Nobody)
- `duration` (optional): Duration of the meeting in seconds (Default: 1 hour)
- `password` (optional): Password for the meeting (Default: No password set)

Example:

```json
{
  "name": "The tragedy of Darth Plagueis the wise",
  "start_time": "2023-06-09T04:20:00.000Z",
  "mail_owner": "sheev@theSenate.com",
  "duration": 420,
  "password": "order66"
}
```

## Get meeting details

Send an HTTP `GET` request to `/conference/{meetingID}`,
where `meetingID` is the ID of the meeting you want to get details from.

Example:

```
GET https://meetings.example.com/conference/69
```

to get details from meeting `69`.

Example return body:

```json
{
  "id": 69,
  "name": "string",
  "start_time": "2023-06-09T04:20:00.000Z",
  "mail_owner": "sheev@theSenate.com",
  "duration": 420,
  "previd": 68,
  "max_occupants": 10,
  "lobby": true
}
```

- `id`: ID of the meeting,
- `name`: Name of the meeting
- `start_time`: Start date and time of the meeting in YYYY-MM-DDThh:mm:ss.000Z format
- `mail_owner`: Mail of the moderator
- `duration`: Duration of the meeting in seconds
- `previd`: ID of the previous meeting
- `max_occupants`: Maximum number of meeting participants
- `lobby`: If true, users can wait in a lobby before joining the meeting

## Delete an existing meeting

Send an HTTP `DELETE` request to `/conference/{meetingID}`,
where `meetingID` is the ID of the meeting you want to delete.

Example:

```
DELETE https://meetings.example.com/conference/69
```
