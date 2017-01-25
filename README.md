# fAudApi
[![Build Status](https://travis-ci.org/formsaudio/fAudApi.svg?branch=master)](https://travis-ci.org/formsaudio/fAudApi)

faAPI is the *F*orms *Aud*io *A*pplication *P*rogramming *I*nterface

fAudApi handles document storage, retrieval, database configuration, authorization, and audit for the FormsAudio site

#API documentation#

### Authentication Notes ###
(almost) every request should have a username and authkey field corresponding to an existing user
a 401 error will come back if authentication is valid but not sufficient

### 400 Notes ###
the application returns a 400 when a necessary field is missing.

### New Form ###
Note that an empty viewers list implies public. Include yourself to make it private.
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "title": "FormsAudio Sample",
    "content": [
        {
            "title": "What day is today?",
            "datatype": "string",
            "validation": "none"
        }
    ],
    "viewers": []
}
```

### New Form Response###
Note that an empty viewers list implies public. Include yourself to make it private.
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "title": "FormsAudio Sample Response",
    "content": [
        {
            "title": "What day is today?",
            "response": "Wednesday",
            "datatype": "string",
            "validation": "none"
        }
    ],
    "viewers": []
}
```

### New User ###
New user does not require authentication, for obvious reasons
```json
{
    "username": "birm2"
}
```

### Find Form by ID ###
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "id": "some_object_id"
}
```

### Find Response by ID ###
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "id": "some_object_id"
}
```

