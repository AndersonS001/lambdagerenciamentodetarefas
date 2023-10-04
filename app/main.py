from aws_lambda_powertools.event_handler import LambdaFunctionUrlResolver

app = LambdaFunctionUrlResolver()


@app.get(".+")
def get():
    return {"event_received": app.current_event.raw_event}

@app.post(".+")
def post():
    return {"path_received": app.current_event.raw_event}

@app.put(".+")
def put():
    return {"path_received": app.current_event.raw_event}

@app.delete(".+")
def delete():
    return {"path_received": app.current_event.raw_event}


def lambda_handler(event: dict, context) -> dict:
    return app.resolve(event, context)