import json
def lambda_handler(event, context):
    message = 'Hello everybody'
    a = {
        'statusCode': 200,
        'body': json.dumps({'input': message})
        }
    print(a)
    return {
        'statusCode': 200,
        'body': json.dumps({'input': message})
    }



if __name__ == "__main__":
    lambda_handler({},{})