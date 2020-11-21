import boto3

dynamodb = boto3.resource('dynamodb', 
                          endpoint_url="http://172.27.0.1:8000",
                          region_name='us-west-2',
                          aws_access_key_id='fakeMyKeyId',
                          aws_secret_access_key='fakeSecretAccessKey')

table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'user_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'user_id',
            'AttributeType': 'N'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print('Table status:', table.table_status)
