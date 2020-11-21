import time
import boto3
from locust import HttpUser, TaskSet, task, between, constant

class UserBehavior(TaskSet):
    @task(1)
    def dynamodb(self):
        dynamodb = boto3.client('dynamodb', endpoint_url="http://172.28.0.1:8000",
                            region_name='us-west-2',
                            aws_access_key_id='ACCESS_ID',
                            aws_secret_access_key='ACCESS_KEY')

        tables = dynamodb.list_tables()

        print('Tables List:',tables['TableNames'])
        return tables

class WebsiteUser(HttpUser):
    tasks = {UserBehavior:1}
    wait_time = constant(0)
