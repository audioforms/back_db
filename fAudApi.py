"""
The api handler for fAudApi.

Responds to and with json messages.
A flask application.
"""

import flask
import os
import datetime
import mongodocs as docs

app = flask.Flask(__name__)


def handle_questions(questions, response=False):
    """Handle questions and question responses."""
    references = []
    for question in questions:
        try:
            default = ""
            title = question['title']
            datatype = question['datatype']
            validation = question['validation']
            if ('default' in question):
                default = question['default']
            if response:
                response = question['response']
        except KeyError:
            flask.abort(400, "A required key in a question was not included.")
    if response:
        resp = docs.QuestionResponse(title=title,
                                     datatype=datatype,
                                     validation=validation,
                                     default=default,
                                     response=response)
        references.append(resp)
    else:
        qst = docs.Question(title=title,
                            datatype=datatype,
                            validation=validation,
                            default=default)
        references.append(qst)
    # do we need to save all references, or having as children ok?


def auth(response):
    """Return the owner name if the key matches."""
    try:
        name = response['username']
        key = response['authkey']
    except KeyError:
        flask.abort(400, "Necessary authorization information was" +
                    "not included.")
    dbkey = docs.User.objects(name=name).first().key
    if (dbkey == key):
        return name
    else:
        return False


@app.errorhandler(400)
def error400(error):
    """Allow errors messages to be passed with 400 errors."""
    response = flask.jsonify({'message': error.description})
    return response


@app.route('/faudapi/form/new', methods=['POST'])
def new_form():
    """Create a new form via api call."""
    req = flask.request.get_json()
    if not req:
        flask.abort(400, "JSON improperly transmitted.")
    # parse the response, give errors if needed
    try:
        title = req['title']
        content = handle_questions(req['content'], False)
        viewers = req['viewers']
    except KeyError:
        flask.abort(400, "A required key was not included.")
    # check owner key
    owner = auth(req)
    if not owner:
        flask.abort(400, "Name or auth key incorrect.")
    form = docs.Form(title=title,
                     owner=owner,
                     content=content,
                     viewers=viewers)
    form.save()
    return flask.jsonify(form.to_json()), 201


@app.route('/faudapi/response/new', methods=['POST'])
def new_Response():
    """Create a new form response via api call."""
    req = flask.request.get_json()
    if not req:
        flask.abort(400, "JSON improperly transmitted.")
    # parse the response, give errors if needed
    try:
        title = req['title']
        content = handle_questions(req['content'], True)
        viewers = req['viewers']
    except KeyError:
        flask.abort(400, "A required key was not included.")
    # check owner key
    owner = auth(req)
    if not owner:
        flask.abort(400, "Name or auth key incorrect.")
    form_response = docs.Form(title=title,
                              owner=owner,
                              content=content,
                              viewers=viewers)
    form_response.save()
    return flask.jsonify(form_response.to_json()), 201


@app.route('/faudapi/user/new', methods=['POST'])
def new_User():
    """Create a new user via api call."""
    req = flask.request.get_json()
    if not req:
        flask.abort(400, "JSON improperly transmitted.")
    # parse the response, give errors if needed
    try:
        name = req['name']
    except KeyError:
        flask.abort(400, "Username (name key) was not included.")
    # check if a user with this name already exists
    if not (docs.User.objects(name=name).count() == 0):
        flask.abort(400, "user %s already exists.".format(name))
    else:
        # generate a key for this new user
        key = os.urandom(20).encode("hex")
        user = docs.User(name=name,
                         key=key,
                         created=datetime.now())
        user.save()
        return flask.jsonify(user.to_json), 201


@app.route('/faudapi/get/forms')
def get_form(formid):
    """Get a form json from api."""
    req = flask.request.get_json()
    if not req:
        flask.abort(400, "JSON improperly transmitted.")
    # parse the response, give errors if needed
    try:
        formid = req['id']
    except KeyError:
        flask.abort(400, "Title of response desired was not included.")
    owner = auth(req)
    resp = docs.Form.objects(id=formid).first()
    if (owner and owner in resp.viewers) or (not resp.viewers):
        # if the owner is logged in and can view, or if it's public
        # public is empty viewer list
        return flask.jsonify(resp.to_json), 201
    else:
        flask.abort(401)


@app.route('/faudapi/get/responses', methods=['POST'])
def get_form_resp(respid):
    """Get a form response json from api."""
    req = flask.request.get_json()
    if not req:
        flask.abort(400, "JSON improperly transmitted.")
    # parse the response, give errors if needed
    try:
        respid = req['id']
    except KeyError:
        flask.abort(400, "Title of response desired was not included.")
    owner = auth(req)
    resp = docs.FormResponse.objects(id=respid).first()
    if (owner and owner in resp.viewers) or (not resp.viewers):
        # if the owner is logged in and can view, or if it's public
        # public is empty viewer list
        return flask.jsonify(resp.to_json), 201
    else:
        flask.abort(401)


if __name__ == '__main__':
    app.run(debug=True)
