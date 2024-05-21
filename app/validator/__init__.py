from functools import wraps
from flask import request
from app.config.http import ExceptionHandler, HTTPResponse

from .user import UserValidator


def validator(form_class):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                form = form_class(data=request.json)
                if not form.validate():
                    errors = form.errors

                    raise ExceptionHandler("Invalid form data.", errors, 422)

                kwargs["body"] = form.data
            except ExceptionHandler as e:
                return HTTPResponse.error(e.message, e.data, e.status)
            return func(*args, **kwargs)

        return wrapper

    return decorator
