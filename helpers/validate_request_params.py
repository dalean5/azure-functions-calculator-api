import json
from typing import Any

from azure.functions import HttpRequest, HttpResponse


def validate_request_params(req: HttpRequest) -> Any:
    """
    Takes in an instance of azure.functions.HttpRequest
    and pulls from it the parameters x, and y.

    These params are validated to be integers and returned
    to the caller. If these params cannot be converted to
    type `int`, return an InvalidRequestParams exception
    with status code 400.
    """

    request_params = {}

    try:
        request_params["x"] = int(req.params.get("x", 0))
        request_params["y"] = int(req.params.get("y", 0))
        return request_params
    except ValueError:
        return HttpResponse(
            body=json.dumps(
                {"error": {"msg": "request params x, and y must be integers"}}
            ),
            status_code=400,
            mimetype="application/json",
        )
