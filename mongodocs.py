import abc
import mongoengine
# serialization with compatibility
try:
    import json
except ImportError:
    import simplejson as json
import yaml


class BaseDoc(mongoengine.Document, abc.ABCMeta):
    """BaseDoc: Abstract Base Class for all document types."""

    meta = {'abstract': True}

    def serialize_all(self):
        """Return a serialization of all documents."""
        jsonlist = []
        for obj in self.objects:
            jsonlist.append(obj.to_json())
        return json.dumps(jsonlist)

    def yaml_all(self):
        """Return the yaml version of the document."""
        return yaml.dump(yaml.load(self.seralize_all), default_flow_style=False))


class Question(BaseDoc):
    """
    Represents a question within a Form document.
    Properties: title, datatype, validation, default
    """
    meta = {'allow_inheritance': True}

    title = mongoengine.fields.StringField(required=True)
    datatype = mongoengine.fields.StringField(required=True)
    validation = mongoengine.fields.StringField()
    default = mongoengine.fields.DynamicFields()


class QuestionResponse(Question):
    """
    Represents an answered question within a Response document.
    Properties: response
    Inhereted properties: title, datatype, validation, default
    """
    response = mongoengine.fields.DynamicField(required=True)


class Form(BaseDoc):
    """
    Represents a form and form questions document.
    Properties: title, owner (reference to User), viewers (reference to Users),
    created, content (sub-docs: Question)
    """
    # define index and other information
    meta = {'allow_inheritance': True, 'indexes': ['owner', '$title']}

    # define fields
    owner = mongoengine.fields.ReferenceField(
        'User', reverse_delete_rule=mongoengine.CASCADE)
    title = mongoengine.fields.StringField(required=True, unique_with=owner)
    viewers = mongoengine.fields.ListField(
        mongoengine.fields.ReferenceField(
            'User', reverse_delete_rule=mongoengine.CASCADE))
    created = mongoengine.fields.DateTimeField()
    pass


class Response(Form):
    """
    Represents a filled out form document.
    Inhereted properties: title, owner (reference to User), viewers, created
    Overridden inhereted properties: content (Sub-docs: QuestionResponse)
    """
    # define index and other information
    meta = {'indexes': ['owner', '$title']}

    # define fields
    # change content base type because response
    content = mongoengine.fields.ListField(mongoengine.fields.ReferenceField(
        QuestionResponse))
    pass


class User(BaseDoc):
    """
    Represents a user document.
    Properties: name, key, created
    """
    # define index and other information
    meta = {'indexes': ['name']}

    # define fields
    name = mongoengine.fields.StringField(required=True, unique=True)
    key = mongoengine.fields.StringField(required=True)
    created = mongoengine.fields.DateTimeField()
    pass


# start host/connection
