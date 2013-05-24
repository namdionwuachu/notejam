from formencode import Schema, validators


class SignupSchema(Schema):
    allow_extra_fields = True
    filter_extra_fields = True

    email = validators.Email(not_empty=True)
    password = validators.UnicodeString(min=6)
    confirm_password = validators.UnicodeString(min=6)
    passwords_match = [
        validators.FieldsMatch('password', 'confirm_password')
    ]


class SigninSchema(Schema):
    allow_extra_fields = True
    filter_extra_fields = True

    email = validators.Email(not_empty=True)
    password = validators.UnicodeString(min=6)
