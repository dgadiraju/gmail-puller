import uuid
import pymongo
import pandas as pd

def get_collection(mongo_host):
    client = pymongo.MongoClient(f'mongodb://{mongo_host}:27017')
    db = client.get_database('email_db')
    collection = db.get_collection('emails')
    return collection


def load_db(collection, mail_ids):
    for mail_id in mail_ids:
        collection.insert_one(mail_id)


def write_to_s3(messages, bucket, folder, start_date):
    df = pd.DataFrame(messages)
    df.to_json(f's3://{bucket}/{folder}/date={start_date.replace("/", "-")}/part-{uuid.uuid1()}')
