from marshmallow import Schema, fields

class AuthorSchema(Schema):
    id = fields.UUID(dump_only=True)
    name = fields.Str(required=True)
    bio = fields.Str()
    birth_date = fields.Date()

class BookSchema(Schema):
    id = fields.UUID(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    published_date = fields.Date()
    author_id = fields.UUID(required=True)
