import boto3

dynamodb = boto3.resource('dynamodb')

DynamoDBtable = dynamodb.Table('MyFavoutiteGames')

response = DynamoDBtable.put_item(
Item = { 
     'Game-UniqueCode': '2022-early',
     'GameName': 'Forza-22'
       }
)
print(response)