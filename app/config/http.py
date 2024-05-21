class HTTPResponse:
    @staticmethod
    def __getStatus(code):
        code = str(code)[0]

        match code:
            case "1":
                message = "Informational"
            case "2":
                message = "Success"
            case "3":
                message = "Redirection"
            case "4":
                message = "Client Error"
            case _:
                message = "Server Error"

        return message

    @staticmethod
    def __JSONResponse(code, message, data=None):
        payload = {
            "meta": {
                "success": str(code)[0] == "2",
                "code": int(code),
                "status": HTTPResponse.__getStatus(code),
                "message": message,
            }
        }

        if data:
            if code == 422:
                payload["errors"] = data
            else:
                payload["data"] = data

        return payload

    @staticmethod
    def success(message, data: dict | None = None, code=200):
        return HTTPResponse.__JSONResponse(code, message, data), int(code)

    @staticmethod
    def error(message, data=None, code=500):
        return HTTPResponse.__JSONResponse(code, message, data), int(code)


class ErrorHandler:
    @staticmethod
    def handleNotFound(e):
        return HTTPResponse.error("Resource not found", code=404)

    @staticmethod
    def handleMethodNotAllowed():
        return HTTPResponse.error("Method not allowed", code=405)

    @staticmethod
    def handleInternalServerError(e):
        return HTTPResponse.error("Internal server error", code=500)

    @staticmethod
    def handleUnprocessableEntity(e):
        return HTTPResponse.error("Unprocessable entity", code=422)

    @staticmethod
    def handleBadRequest(e):
        return HTTPResponse.error("Bad request", code=400)

    @staticmethod
    def handleUnauthorized(e):
        return HTTPResponse.error("Unauthorized", code=401)

    @staticmethod
    def handleForbidden(e):
        return HTTPResponse.error("Forbidden", code=403)

    @staticmethod
    def registerErrorHandler(app):
        app.register_error_handler(404, ErrorHandler.handleNotFound)
        app.register_error_handler(405, ErrorHandler.handleMethodNotAllowed)
        app.register_error_handler(500, ErrorHandler.handleInternalServerError)
        app.register_error_handler(422, ErrorHandler.handleUnprocessableEntity)
        app.register_error_handler(400, ErrorHandler.handleBadRequest)
        app.register_error_handler(401, ErrorHandler.handleUnauthorized)
        app.register_error_handler(403, ErrorHandler.handleForbidden)


class ExceptionHandler(Exception):
    def __init__(self, message, data, status):
        self.message = message
        self.data = data
        self.status = status

    def to_dict(self):
        return {"message": self.message, "data": self.data, "status": self.status}
