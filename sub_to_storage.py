import base64
import pandas as pd
from google.cloud.storage import Client  
import datetime

def upload_to_storage(dataframe):
    storage_client = Client()
    filename = "usa_covid_data_"+str(datetime.datetime.now().strftime("%d_%m_%Y_%H:%M:%S"))+".csv"
    bucket = storage_client.get_bucket("capstone1-egen-bucket")   
    bucket.blob(filename).upload_from_string(data=dataframe,content_type="text/csv")  

# def convert_data(data):
#      df = pd.read_json(data)
#      df.to_csv()
#      return df

def sub_to_storage(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
    upload_to_storage(pubsub_message)
