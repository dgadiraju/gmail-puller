import get_mail_ids, load_mail_ids
import os

START_DATE = os.environ.get('START_DATE')
END_DATE = os.environ.get('END_DATE')

# Get email details
service = get_mail_ids.get_service()
messages = get_mail_ids.get_messages(service, START_DATE, END_DATE)

for message in messages:
    print(message)

# Save to Mongo DB Database
# MONGO_HOST = os.environ.get('MONGO_HOST')
# collection = load_mail_ids.get_collection(MONGO_HOST)
# load_mail_ids.load_db(collection, messages)
