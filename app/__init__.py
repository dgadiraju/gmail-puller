import get_mail_ids, load_mail_ids
import os


def lambda_handler(event, context):
    start_date = os.environ.get('START_DATE')
    end_date = os.environ.get('END_DATE')
    bucket_name = os.environ.get('BUCKET_NAME')
    folder = os.environ.get('FOLDER')

    service = get_mail_ids.get_service()
    messages = get_mail_ids.get_messages(service, start_date, end_date)
    load_mail_ids.write_to_s3(messages, bucket_name, folder, start_date)

    for message in messages:
        print(message)
    return {
        'statusCode': 200,
        'body': 'Data is loaded successfully'
    }
