import json
import logging

import azure.functions as func

from helpers.validate_request_params import validate_request_params


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    res = validate_request_params(req)

    if isinstance(res, func.HttpResponse):
        return res

    try:
        quotient = res["x"] / res["y"]
    except ZeroDivisionError:
        return func.HttpResponse(
            body=json.dumps({"error": {"msg": "cannot divide by zero"}}),
            status_code=400,
            mimetype="application/json",
        )

    return func.HttpResponse(
        body=json.dumps({"x": res["x"], "y": res["y"], "result": quotient}),
        status_code=200,
        mimetype="application/json",
    )
