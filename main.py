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
    return flask.jsonify(tables.Form.seralize), 201

@app.route('/af/api/response/new', methods=['POST'])
def new_Response():
    """Create a new form via api call."""
    if not flask.request.json or not 'title' in flask.request.json:
        abort(400)
    response = tables.Response(
        title = flask.request.json.get('title', "Untitled Form"),
        owner = flask.request.json.get('owner', "0"),
        content = flask.request.json.get('content', ""),
        permissions = flask.request.json.get('permissions', "0")
    )
    tables.session.add(response)
    return flask.jsonify(tables.Response.seralize), 201

if __name__ == '__main__':
    app.run(debug=True)
