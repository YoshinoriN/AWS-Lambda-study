# lambda_function.py
import json

print('Loading function')

def hello_hello(event, context):
    print("value1 =" + event['key1'])
    print("value2 =" + event['key2'])
    print("value3 =" + event['key3'])

    return event['key1']
