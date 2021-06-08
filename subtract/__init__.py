import json
import logging

import azure.functions as func

from helpers.validate_request_params import validate_request_params


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    res = validate_request_params(req)

    if isinstance(res, func.HttpResponse):
        return res

    difference = res["x"] - res["y"]

    return func.HttpResponse(
        body=json.dumps({"x": res["x"], "y": res["y"], "result": difference}),
        status_code=200,
        mimetype="application/json",
    )
