from collections import namedtuple
from main import lambda_handler


def lambda_context():
    context = {
        "function_name": "test",
        "memory_limit_in_mb": 128,
        "invoked_function_arn": "arn:aws:lambda:eu-west-1:123456789012:function:test",
        "aws_request_id": "da658bd3-2d6f-4e7b-8ec2-937234644fdc",
    }

    named_context = namedtuple("LambdaContext", context.keys())(*context.values())

    return named_context


def debug_get():
    event = {
        "version": "2.0",
        "routeKey": "$default",
        "rawPath": "/todos",
        "rawQueryString": "",
        "headers": {
            "x-amz-content-sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
            "x-amzn-tls-version": "TLSv1.2",
            "x-amz-date": "20220803T092917Z",
            "x-forwarded-proto": "https",
            "x-forwarded-port": "443",
            "x-forwarded-for": "123.123.123.123",
            "accept": "application/xml",
            "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
            "x-amzn-trace-id": "Root=1-63ea3fee-51ba94542feafa3928745ba3",
            "host": "xxxxxxxxxxxxx.lambda-url.eu-central-1.on.aws",
            "content-type": "application/json",
            "accept-encoding": "gzip, deflate",
            "user-agent": "Custom User Agent",
        },
        "requestContext": {
            "accountId": "123457890",
            "apiId": "xxxxxxxxxxxxxxxxxxxx",
            "authorizer": {
                "iam": {
                    "accessKey": "AAAAAAAAAAAAAAAAAA",
                    "accountId": "123457890",
                    "callerId": "AAAAAAAAAAAAAAAAAA",
                    "cognitoIdentity": None,
                    "principalOrgId": "o-xxxxxxxxxxxx",
                    "userArn": "arn:aws:iam::AAAAAAAAAAAAAAAAAA:user/user",
                    "userId": "AAAAAAAAAAAAAAAAAA",
                }
            },
            "domainName": "xxxxxxxxxxxxx.lambda-url.eu-central-1.on.aws",
            "domainPrefix": "xxxxxxxxxxxxx",
            "http": {
                "method": "GET",
                "path": "/",
                "protocol": "HTTP/1.1",
                "sourceIp": "123.123.123.123",
                "userAgent": "Custom User Agent",
            },
            "requestId": "24f9ef37-8eb7-45fe-9dbc-a504169fd2f8",
            "routeKey": "$default",
            "stage": "$default",
            "time": "03/Aug/2022:09:29:18 +0000",
            "timeEpoch": 1659518958068,
        },
        "isBase64Encoded": False,
    }

    context = lambda_context()


    res = lambda_handler(event=event, context=context)
    print(res)


def debug_post_status():
    event = {
        "path_received": {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/status",
            "rawQueryString": "",
            "headers": {
                "content-length": "31",
                "x-amzn-tls-version": "TLSv1.2",
                "x-forwarded-proto": "https",
                "postman-token": "44fd2685-bd9b-4cac-839a-73b87568802e",
                "x-forwarded-port": "443",
                "x-forwarded-for": "200.232.224.130",
                "accept": "*/*",
                "x-amzn-tls-cipher-suite": "ECDHE-RSA-AES128-GCM-SHA256",
                "x-amzn-trace-id": "Root=1-651e05c8-240a2f734cfe14563bf2c428",
                "host": "u546ua5ofaf242hvuf64dwl4240zxgys.lambda-url.sa-east-1.on.aws",
                "content-type": "application/json",
                "accept-encoding": "gzip, deflate, br",
                "user-agent": "PostmanRuntime/7.33.0",
            },
            "requestContext": {
                "accountId": "anonymous",
                "apiId": "u546ua5ofaf242hvuf64dwl4240zxgys",
                "domainName": "u546ua5ofaf242hvuf64dwl4240zxgys.lambda-url.sa-east-1.on.aws",
                "domainPrefix": "u546ua5ofaf242hvuf64dwl4240zxgys",
                "http": {
                    "method": "POST",
                    "path": "/",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "200.232.224.130",
                    "userAgent": "PostmanRuntime/7.33.0",
                },
                "requestId": "c51a9c55-c2e4-4d13-988c-b07f9eec6676",
                "routeKey": "$default",
                "stage": "$default",
                "time": "05/Oct/2023:00:39:36 +0000",
                "timeEpoch": 1696466376988,
            },
            "body": '{\r\n    "status": "CANCELADO"\r\n}',
            "isBase64Encoded": False,
        }
    }

    context = lambda_context()

    lambda_handler(event=event, context=context)


if __name__ == "__main__":
    debug_get()
    # debug_post_status()
