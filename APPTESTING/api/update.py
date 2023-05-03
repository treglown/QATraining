import os 
import json
import uuid
import datetime
import boto3
from .helper import respond, parse_username_from_claims

def handler(event, context):
    data = None

    try:
        data = json.loads(event['body'])
    except Exception as ex:
        return respond(ex.args[0], None)
    
    table_name = os.getenv('TODO_TABLE', 'todo_test')
    region_name = os.getenv('AWS_REGION', 'eu-west-1')
    client = boto3.resource('dynamodb', region_name=region_name)

    user_id = parse_username_from_claims(event)
    result = update(client, user_id, data, table_name)

    return respond(None, result)

def update(client, user_id, data, table_name):
    """ client is the dynammoDB client
        user id is the id for the user that own the record to update
        data is for the properties to store in dynamodb
        table_name is the name of the dynamoDB table where records are stored
    """

    if 'item' not in data or 'completed' not in data:
        raise ValueError(
            'Cannot find any values to set. Expecting item or data.'
        )
    if 'todoId' not in data:
        raise ValueError('You must set the todoId in order to update an item')
    
    ex_attr_name = {}
    ex_attr_value = {}
    update_exp_lst = []

    if 'item' in data:
        ex_attr_name['#item'] = 'item'
        ex_attr_value[':i'] = data['item']
        update_exp_lst.append('#item = :i')

    if 'completed' in data:
        ex_attr_name['#completed'] = 'completed'
        ex_attr_value[':c'] = data['completed']
        update_exp_lst.append('#completed = :c')

    table = client.Table(table_name)

    result = table.update_item(
        ReturnValues='UPDATED_NEW',
        ExpressionAttributeNames=ex_attr_name,
        ExpressionAttributeValues=ex_attr_value,
        Key={
            'userId': user_id
            'todoId': data['todoId'],
        },
        UpdateExpression='SET {}'.format(', '.join(update_exp_lst)))
    return result.get('Attributes', {})