"""
Continually grab data from randomuser.me and
post it to a Kinesis Stream
"""

import json
import random
import time
import uuid
import requests
import boto3

client = boto3.client('kinesis', region_name='us-east-1')
PARTITION_KEY = str(uuid.uuid4())

while True:
    r = requests.get('https://randomuser.me/api/?exc=login')
    data = json.dumps(r.json())
    client.put_record(
        StreamName='my-stream',
        Data=data,
        PartitionKey=PARTITION_KEY)
    time.sleep(random.uniform(0, 1))
