import base64
import pandas as pd
from google.cloud.storage import Client  
import datetime

def upload_to_storage(dataframe):
    # storage_client = Client()
    # filename = "usa_covid_data_"+str(datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S"))+".csv"
    # bucket = storage_client.get_bucket("capstone1-egen-bucket")   
    # bucket.blob(filename).upload_from_string(data=dataframe,content_type="text/csv")  
    return None

def convert_data(data):
    df = data
    #  df = pd.read_json(data)
    #  print(df)
    df.to_csv()
    print(df)
    return df

def sub_to_storage(data):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    # pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    # print(pubsub_message)
    upload_to_storage(convert_data(data))

sub_to_storage('[{"date":20210307,"states":56,"positive":28756489,"negative":74582825,"pending":11808,"hospitalizedCurrently":40199,"hospitalizedCumulative":776361,"inIcuCurrently":8134,"inIcuCumulative":45475,"onVentilatorCurrently":2802,"onVentilatorCumulative":4281,"dateChecked":"2021-03-07T24:00:00Z","death":515151,"hospitalized":776361,"totalTestResults":363825123,"lastModified":"2021-03-07T24:00:00Z","recovered":null,"total":0,"posNeg":0,"deathIncrease":842,"hospitalizedIncrease":726,"negativeIncrease":131835,"positiveIncrease":41835,"totalTestResultsIncrease":1170059,"hash":"a80d0063822e251249fd9a44730c49cb23defd83"}] ')