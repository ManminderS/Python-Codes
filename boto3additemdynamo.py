
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

DynamoDBtable = dynamodb.Table('MyFavoutiteGames') # Input table name

# Write items to table
with DynamoDBtable.batch_writer() as batch:
    batch.put_item(Item={"Game-UniqueCode": "20124", "GameName": "GTA5"})
    batch.put_item(Item={"Game-UniqueCode": "20073", "GameName": "GTAVice"})
    batch.put_item(Item={"Game-UniqueCode": "20094", "GameName": "GTALibertyCity"})
    batch.put_item(Item={"Game-UniqueCode": "20101", "GameName": "GTASan"})


print(batch)
  