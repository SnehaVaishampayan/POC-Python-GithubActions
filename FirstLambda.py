
import json
def lambda_handler(event, context):
    message = 'Hello from localtttt.'
    a = {
        'statusCode': 200,
        'body': json.dumps({'input': message})
        }
    print(a)
    return {
        'statusCode': 200,
        'body': json.dumps({'input': message})
    }
