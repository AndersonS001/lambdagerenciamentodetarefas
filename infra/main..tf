data "aws_iam_policy_document" "assume_role" {
  statement {
    effect = "Allow"

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }

    actions = ["sts:AssumeRole"]
  }
}

resource "aws_iam_role" "iam_for_lambda" {
  name               = "iam_for_lambda"
  assume_role_policy = data.aws_iam_policy_document.assume_role.json
}

data "archive_file" "lambda" {
  type        = "zip"
  source_dir = "../app"
  output_path = "../zip/lambda_function_payload.zip"
}

resource "aws_lambda_function" "lambda" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "../zip/lambda_function_payload.zip"
  function_name = "lambdagerenciamento"
  role          = aws_iam_role.iam_for_lambda.arn
  handler       = "main.lambda_handler"
  architectures = ["arm64"]
  timeout       = 100

  layers = [ "arn:aws:lambda:sa-east-1:017000801446:layer:AWSLambdaPowertoolsPythonV2-Arm64:45" ]

  source_code_hash = data.archive_file.lambda.output_base64sha256

  runtime = "python3.11"

#   environment {
#     variables = {
#       foo = "bar"
#     }
#   }
}

resource "aws_lambda_function_url" "url" {
  function_name      = aws_lambda_function.lambda.function_name
  authorization_type = "NONE"

  cors {
    allow_credentials = true
    allow_origins     = ["*"]
    allow_methods     = ["*"]
    allow_headers     = ["date", "keep-alive"]
    expose_headers    = ["keep-alive", "date"]
    max_age           = 86400
  }
}