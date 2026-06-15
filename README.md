# api-s3

API Serverless para operar con S3.

## Funciones

- `GET /s3/lista-buckets`: lista buckets.
- `POST /s3/bucket/lista-objetos`: lista objetos de un bucket.
- `POST /s3/bucket`: crea un bucket.
- `POST /s3/bucket/directorio`: crea un directorio dentro de un bucket.
- `POST /s3/bucket/archivo`: sube un archivo a un directorio de un bucket.

## Despliegue

El `stage` se controla con `--stage` y por defecto usa `dev`.

```bash
serverless deploy --stage dev
serverless deploy --stage test
serverless deploy --stage prod
```

Si quieres ver los endpoints desplegados:

```bash
serverless info --stage dev
serverless info --stage test
serverless info --stage prod
```

## Pruebas con curl en Linux

Reemplaza `API_URL` por la URL base de API Gateway del stage desplegado.

Crear bucket:

```bash
curl -X POST "$API_URL/s3/bucket" \
  -H "Content-Type: application/json" \
  -d '{
    "bucket": "mi-bucket-prueba-s11"
  }'
```

Crear directorio:

```bash
curl -X POST "$API_URL/s3/bucket/directorio" \
  -H "Content-Type: application/json" \
  -d '{
    "bucket": "mi-bucket-prueba-s11",
    "directorio": "documentos"
  }'
```

Subir archivo de texto:

```bash
curl -X POST "$API_URL/s3/bucket/archivo" \
  -H "Content-Type: application/json" \
  -d '{
    "bucket": "mi-bucket-prueba-s11",
    "directorio": "documentos",
    "archivo": "hola.txt",
    "contenido": "Hola mundo desde curl",
    "content_type": "text/plain"
  }'
```

Listar objetos del bucket:

```bash
curl -X POST "$API_URL/s3/bucket/lista-objetos" \
  -H "Content-Type: application/json" \
  -d '{
    "bucket": "mi-bucket-prueba-s11"
  }'
```
