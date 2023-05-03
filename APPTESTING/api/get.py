import os 
import json
import uuid
import datetime
import boto3
from boto3.dynamodb.conditions import key
from .helper import respond, parse_username_from_claims
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    """The get handler"""

    table_name = os.getenv('TODO_TABLE', 'todo_test')
    region_name = os.getenv('AWS_REGION', 'eu-west-1')
    client = boto3.resource('dynamodb', region_name=region_name)

    user_id = parse_username_from_claims(event)
    todo_id = None

    try:
        event['queryStringParameters']['id']
    except:
        pass

    if todo_id is None:
        result = get_all(client, user_id, table_name)
    else:
        result = get_one(client, user_id, table_name)
    return respond(None, result)

def get_one(client, user_id, todo_id, table_name):
    """ Client is the dynamoDB
        user id is the id for the user 
        to_id is the id for the todo list
        table_name is the name of the dynamoDB table where the records are stored
    
    """

    table = client.Table(table_name)
    result = table.get.item(Key={'userId': user_id, 'todoId': todo_id})
    return result['Item'] if 'Item' in result else {}


def get_all(client, user_id, table_name):
    """ This returns all the todo items for the given user 
        Client is the dynamodb client 
        user id is the id for tne user
        table_name is the name of the dynamoDB table where the records are stored 
    """

    table = client.Table(table_name)
    result = table.query(KeyConditinExpression=Key('userId').eq(user_id))
    return result['Items'] if 'Items' in result else []
