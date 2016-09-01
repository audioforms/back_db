import flask
# table engine (tables.py)
import tables

app = flask.Flask(__name__)

@app.route('/af/api/form/new', methods=['POST'])
def new_form():
    """Create a new form via api call."""
    if not flask.request.json or not 'title' in flask.request.json:
        abort(400)
    form = tables.Form(
        title = flask.request.json.get('title', "Untitled Form"),
        owner = flask.request.json.get('owner', "0"),
        content = flask.request.json.get('content', ""),
        permissions = flask.request.json.get('permissions', "0")
    )
    tables.session.add(form)
    return flask.jsonify(tables.Form.serialize_list(form)), 201

@app.route('/af/api/response/new', methods=['POST'])
def new_Response():
    """Create a new form response via api call."""
    if not flask.request.json or not 'title' in flask.request.json:
        abort(400)
    response = tables.Response(
        title = flask.request.json.get('title', "Untitled Form"),
        owner = flask.request.json.get('owner', "0"),
        content = flask.request.json.get('content', ""),
        permissions = flask.request.json.get('permissions', "0")
    )
    tables.session.add(response)
    return flask.jsonify(tables.Response.serialize_list(response)), 201

@app.route('/af/api/user/new', methods=['POST'])
def new_Response():
    """Create a new user via api call."""
    if not flask.request.json or not 'title' in flask.request.json:
        abort(400)
    user = tables.User(
        title = flask.request.json.get('name',""),
    )
    tables.session.add(user)
    return flask.jsonify(tables.User.serialize_list(user)), 201

@app.route('/af/api/form/<formid>')
def  get_form(formid):
    form = tables.session.query(Form).get(formid)
    return flask.jsonify(tables.Form.serialize_list(form)), 201

if __name__ == '__main__':
    app.run(debug=True)
