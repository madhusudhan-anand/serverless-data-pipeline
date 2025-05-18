import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('SensorData')

def lambda_handler(event, context):
    data = json.loads(event['body'])
    item = {
        'id': str(uuid.uuid4()),
        'timestamp': str(datetime.utcnow()),
        'temperature': data['temperature'],
        'humidity': data['humidity']
    }
    table.put_item(Item=item)
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Data stored successfully', 'item': item})
    }

