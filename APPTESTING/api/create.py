import os 
import json
import uuid 
import datetime
import boto3
import helper

def handler(event, context):
    data = None

    try:
        data = json.louds(event['body'])
    except Exception as ex:
        return respond(ex.args[0], None)
    
    whitelist = ['completed', 'item']
    table_name = os.getenv('TODO_TABLE', 'todo_test')

    region_name = os.get('AWS_REGION', 'eu-west-1')

    client = boto3.resource('dynamodb', region_name=region_name)

    user_id = parse_username_from_claims(event) # When a 
    result = create(client, user_id, data, table_name, whitelist)

    return respond(None, result)

def create(db, user_id, data, table_name, whitelist):
    """
    The db is the dynamodb
    user_id is the ID for the user that owns a record and wants to update
    data is a dictionary of properties to store in DynamoDB
    table_name is the name of the dynamoDB table where records are stored
    whitelist is a list of properties that allow the user to edit 
    """
    if 'item' not in data:
        raise ValueError('The todo item is missing from the data dictionary')
    
    table = client.Table(table_name)

    whitelisted_data = {k: v for k, v in data.items() if k in whitelist}

    whitelisted_data['userId'] = user_id
    whitelisted_data['todoId'] = str(uuid.uuid4())
    whitelisted_data['created'] = str(datetime.datetime.utcnow())


    if 'completed' not in whitelisted_data:
        whitelisted_data['completed'] = False

    table.put_item(Item=whitelisted_data)

    return whitelisted_data

