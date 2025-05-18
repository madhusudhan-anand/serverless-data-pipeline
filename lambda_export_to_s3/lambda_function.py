import json
import boto3
from decimal import Decimal
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')

TABLE_NAME = 'SensorData'
BUCKET_NAME = 'sensor-data-export-ma'

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    data = response['Items']

    key = f"exported-data-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.json"

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(data, default=decimal_default),
        ContentType='application/json'
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data exported to S3', 's3_key': key})
    }

