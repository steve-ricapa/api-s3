import boto3
import json


def lambda_handler(event, context):
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)

    nombre_bucket = body['bucket']
    nombre_directorio = body['directorio'].strip('/')

    s3 = boto3.client('s3')
    s3.put_object(Bucket=nombre_bucket, Key=f'{nombre_directorio}/')

    return {
        'statusCode': 200,
        'message': 'Directorio creado correctamente',
        'bucket': nombre_bucket,
        'directorio': nombre_directorio,
    }
