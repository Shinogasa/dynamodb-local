import boto3

dynamodb = boto3.client('dynamodb', endpoint_url="http://172.28.0.1:8000",
                            region_name='us-west-2',
                            aws_access_key_id='ACCESS_ID',
                            aws_secret_access_key='ACCESS_KEY')

tables = dynamodb.list_tables()

print('Tables List:',tables['TableNames'])
