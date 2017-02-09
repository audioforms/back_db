# fAudApi
[![Build Status](https://travis-ci.org/formsaudio/fAudApi.svg?branch=master)](https://travis-ci.org/formsaudio/fAudApi)

faAPI is the *F*orms *Aud*io *A*pplication *P*rogramming *I*nterface

fAudApi handles document storage, retrieval, database configuration, authorization, and audit for the FormsAudio site

#API documentation#
## api notes ##
see http://forms.audio/fAudApi/ for api commands

### Authentication Notes ###
(almost) every request should have a username and authkey field corresponding to an existing user
a 401 error will come back if authentication is valid but not sufficient

### 400 Notes ###
the application returns a 400 when a necessary field is missing.
