# fAudApi
[![Build Status](https://travis-ci.org/formsaudio/fAudApi.svg?branch=master)](https://travis-ci.org/formsaudio/fAudApi)

faAPI is the *F*orms *Aud*io *A*pplication *P*rogramming *I*nterface

fAudApi handles document storage, retrieval, database configuration, authorization, and audit for the FormsAudio site

#api documentation#

### authentication notes ###
(almost) every request should have a username and authkey field corresponding to an existing user
a 401 error will come back if authentication is valid but not sufficient

### 400 notes ###
the application returns a 400 when a necessary field is missing.

### new form ###
Note that an empty viewers list implies public. Include yourself to make it private.
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "title": "FormsAudio Sample",
    "content": {
        "question": {
            "title": "What day is today?",
            "datatype": "string",
            "validation": "none"
        }
    },
    "viewers": []
}
```

### new form response###
Note that an empty viewers list implies public. Include yourself to make it private.
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "title": "FormsAudio Sample Response",
    "content": {
        "question": {
            "title": "What day is today?",
            "response": "Wednesday",
            "datatype": "string",
            "validation": "none"
        }
    },
    "viewers": []
}
```

### new user ###
New user does not require authentication, for obvious reasons
```json
{
    "username": "birm2"
}
```

### find form by id ###
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "id": "some_object_id"
}
```

### find response by id ###
```json
{
    "username": "birm",
    "authkey": "<AUTHKEY>",
    "id": "some_object_id"
}
```
