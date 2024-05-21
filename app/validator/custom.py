from wtforms import ValidationError


class Required:
    def __init__(self, message=None):
        self.message = message

    def __call__(self, form, field):
        if field.data is None or field.data == "":
            if self.message is None:
                message = field.gettext("Field is required.")
            else:
                message = self.message

            raise ValidationError(message)
