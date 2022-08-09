import boto3
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
DynamoDBtable = dynamodb.Table('MyFavoutiteGames')    # Input table name  
response = DynamoDBtable.query(
    KeyConditionExpression=Key('Game-UniqueCode').eq('20124') # Input key to query
)

print(response)