import json
import requests

def lambda_handler(event, context):
    # TODO implement
    print("It's working!!")
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
NewTest
