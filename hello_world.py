import json

print('loading function')
def lambda_handler(event, context):
    print("value 1 = "+event['key1'])
    print("value 2 = "+event['key2'])
    print("value 3 = "+event['key3'])

    return event['key1']