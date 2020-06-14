import pickle
from googleapiclient.discovery import build


def get_service():
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

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
        msg_details = {'id': m['id']}
        for headers in msg['payload']['headers']:
            if headers['name'] == 'From':
                msg_details['From'] = headers['value']
            elif headers['name'] == 'Date':
                msg_details['Date'] = headers['value']
        message_list.append(msg_details)

    return message_list


# service = get_service()
# get_labels(service)
# messages = get_messages(service)

# for message in messages:
#     print(message)
