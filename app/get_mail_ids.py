import os
import pickle
from googleapiclient.discovery import build
import boto3


def get_service():
    app_home = os.environ.get('APP_HOME')
    sm_client = boto3.client(
        'secretsmanager',
        region_name='us-east-1'
    )
    secret_token = sm_client.get_secret_value(SecretId='gmail_token')['SecretBinary']
    creds = pickle.loads(secret_token)

    service = build('gmail', 'v1', credentials=creds)
    return service


def get_labels(service):
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    for label in labels:
        print(label['name'])


def get_messages(service, START_DATE, END_DATE):
    users = service.users()
    messages = users.messages().list(userId='me', q=f'after:{START_DATE} before:{END_DATE}').execute()
    message_list = []

    for m in messages['messages']:
        msg = users.messages().get(userId='me', id=m['id']).execute()
        message_list.append(msg)

    return message_list


# service = get_service()
# get_labels(service)
# messages = get_messages(service)

# for message in messages:
#     print(message)
