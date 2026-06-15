import boto3
import json


def lambda_handler(event, context):
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)

    nombre_bucket = body['bucket']

    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=nombre_bucket)

    return {
        'statusCode': 200,
        'message': 'Bucket creado correctamente',
        'bucket': nombre_bucket,
    }
