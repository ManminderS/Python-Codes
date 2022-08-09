import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') 

# Create table
DynamoDBtable = dynamodb.create_table(
    TableName='MyFavoutiteGames', 
    KeySchema=[
        {
            'AttributeName': 'Game-UniqueCode', 
            'KeyType': 'HASH'  
        },
        {
            'AttributeName': 'GameName',
            'KeyType': 'RANGE' 
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'Game-UniqueCode',
            'AttributeType': 'S'  
        },
        {
            'AttributeName': 'GameName',
            'AttributeType': 'S'  
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

print("status of the table: ", DynamoDBtable.table_status) 