import json

def respond(err, res=None):
    body = {}
    if err:
        body = json.dumps({'error': err})
    else:
        body = json.dumps(res)
    return {
        'statusCode': '400' if err else '200',
        'body': body,
        'headers': {
            'content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

def parse_username_from_claims(event):
    return event['requestContext']['authorizer']['claims']['cognito:username']