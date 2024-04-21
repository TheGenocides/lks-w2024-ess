import datetime
import boto3

dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

def lambda_handler(event, context):
    
    timestamp = str(datetime.datetime.now())
    humid = int(event['humid'])
    base_humid = int(event['base_humid'])
    
    table = dynamodb.Table('Enter Table Name')
    
    if humid < base_humid:
        sns.publish(
            TargetArn='Enter topic ARN here',
            Message='Humidity reached below base humid from nama / sekolah at ' + timestamp
        )
        
    table.put_item(
       Item={
           'timestamp': timestamp, 
           'humid': humid,
           'base_humid': base_humid
       }
    )
    
    return 0