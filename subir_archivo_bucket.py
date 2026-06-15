import base64
import boto3
import json


def lambda_handler(event, context):
    body = event.get('body', {})
    if isinstance(body, str):
        body = json.loads(body)

    nombre_bucket = body['bucket']
    nombre_directorio = body['directorio'].strip('/')
    nombre_archivo = body['archivo']
    contenido = body['contenido']
    content_type = body.get('content_type', 'application/octet-stream')
    es_base64 = body.get('base64', False)

    if es_base64:
        contenido = base64.b64decode(contenido)

    s3 = boto3.client('s3')
    s3.put_object(
        Bucket=nombre_bucket,
        Key=f'{nombre_directorio}/{nombre_archivo}',
        Body=contenido,
        ContentType=content_type,
    )

    return {
        'statusCode': 200,
        'message': 'Archivo subido correctamente',
        'bucket': nombre_bucket,
        'directorio': nombre_directorio,
        'archivo': nombre_archivo,
    }
