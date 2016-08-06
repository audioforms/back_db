import sqlalchemy
import datetime
from sqlalchemy.ext.declarative import declarative_base

"""connect to a database"""
engine = sqlalchemy.create_engine('sqlite:///afAPI.db')

"""Define the base class as recommended by sqlalchemy"""
Base = declarative_base()

"""Base class as temporary fix; thanks to Carl Ekerot"""
class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in
                sqlalchemy.inspection.inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]


class Form(Base, Serializer):
    __tablename__ = "form"
    id = sqlalchemy.schema.Column('id', sqlalchemy.types.Integer,
                                  primary_key = True)
    title = sqlalchemy.schema.Column('title', sqlalchemy.types.String(128))
    owner = sqlalchemy.schema.Column('owner', sqlalchemy.types.Integer)
    content = sqlalchemy.schema.Column('content', sqlalchemy.types.Text)
    viewers = sqlalchemy.schema.Column('viewers',
                                       sqlalchemy.types.Text)
    created = sqlalchemy.schema.Column('created',
                                       sqlalchemy.types.DateTime,
                                       server_default =
                                       sqlalchemy.sql.func.now())
    def serialize(self):
        """get dict representing the object"""
        return Serializer.serialize(self)

class Response(Base, Serializer):
    __tablename__ = "response"
    id = sqlalchemy.schema.Column('id', sqlalchemy.types.Integer,
                                  primary_key = True)
    title = sqlalchemy.schema.Column('title', sqlalchemy.types.String(128))
    owner = sqlalchemy.schema.Column('owner', sqlalchemy.types.Integer)
    content = sqlalchemy.schema.Column('content', sqlalchemy.types.Text)
    viewers = sqlalchemy.schema.Column('viewers',
                                       sqlalchemy.types.Text)
    created = sqlalchemy.schema.Column('created',
                                       sqlalchemy.types.DateTime,
                                       server_default =
                                       sqlalchemy.sql.func.now())

    def serialize(self):
        """get dict representing the object"""
        return Serializer.serialize(self)

class User(Base, Serializer):
    __tablename__ = "user"
    id = sqlalchemy.schema.Column('id', sqlalchemy.types.Integer,
                                  primary_key = True)
    name = sqlalchemy.schema.Column('name', sqlalchemy.types.String(128))
    key = sqlalchemy.schema.Column('key', sqlalchemy.types.String(128))
    created = sqlalchemy.schema.Column('created',
                                       sqlalchemy.types.DateTime,
                                       server_default =
                                       sqlalchemy.sql.func.now())

    def serialize(self):
        """get dict representing the object"""
        return Serializer.serialize(self)


"""create schema if it doesn't exist"""
Base.metadata.create_all(engine)


"""connect to db and start session"""
Session = sqlalchemy.orm.sessionmaker(bind=engine)
