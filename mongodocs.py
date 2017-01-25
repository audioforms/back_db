import abc
import mongoengine

# start host/connection

class BaseDoc(mongoengine.Document, abc.ABCMeta):
    """BaseDoc: Abstract Base Class for all document types."""

    meta = {
        'abstract': True,
    }

    def unique(self):
        """Check uniqueness of document in context."""
        pass

    def authorized(self):
        """Check if use of the document is authroized."""
        pass

    def serialize(self):
        """Return a serialization of the document."""
        pass

    def yaml(self):
        """Return the yaml version of the document."""
        pass

class Question(BaseDoc):
    """Represents a question within a Form document.
    Properties: title, type, validation, default"""
    pass

class QuestionResponse(BaseDoc):
    """Represents an answered question within a Response document.
    Properties: response, title, type, validation, default"""
    pass

class Form(BaseDoc):
    """Represents a form and form questions document."""
    """Properties: title, owner (reference to User), viewers,
    created, content (sub-docs: Question)"""
    owner = mongoengine.ReferenceField('User',
                                       reverse_delete_rule=mongoengine.CASCADE)
    pass

class Response(BaseDoc):
    """Represents a filled out form document."""
    """Properties: title, owner (reference to User), viewers,
    created, content (Sub-docs: QuestionResponse)"""
    owner = mongoengine.ReferenceField('User',
                                       reverse_delete_rule=mongoengine.CASCADE)
    content = mongoengine.ListField(mongoengine.ReferenceField(
        QuestionResponse))
    pass

class User(BaseDoc):
    """Represents a user document."""
    """Properties: name, key, created"""
    """sub-docs: question"""
    pass
