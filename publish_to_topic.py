print("Docker running successfully")
import logging
import os 
from time import sleep
from requests import Session
from concurrent import futures
from google.cloud.pubsub_v1 import PublisherClient
from google.cloud.pubsub_v1.publisher.futures import Future

# TODO(developer)

class api_to_pubsub:

    def __init__(self):
        self.project_id = "rich-sprite-317301"
        self.topic_id = "capstone1-pubsub-topic"
        self.publisher = PublisherClient()
        self.topic_path = self.publisher.topic_path(self.project_id, self.topic_id)
        self.publish_futures = []
        pass

    def fetch_covid_data(self):
        url="https://api.covidtracking.com/v1/us/current.csv"

        ses = Session() 
        res = ses.get(url)
        if 200 <= res.status_code < 400:
            logging.info("Data fetched successfully")
            print("data fetched")
            return res.text
        else:
            raise Exception("Failed to fetch API data")

    def get_callback(self, publish_future, data):
        def callback(publish_future):
            try:
                # Wait 60 seconds for the publish call to succeed.
                print(publish_future.result(timeout=60))
            except futures.TimeoutError:
                print("Publishing {data} timed out.")

        return callback
        
    def send_to_topic(self, message):
        publish_future = self.publisher.publish(self.topic_path, message.encode("utf-8"))
        # Non-blocking. Publish failures are handled in the callback function.
        publish_future.add_done_callback(self.get_callback(publish_future, message))
        self.publish_futures.append(publish_future)

        # Wait for all the publish futures to resolve before exiting.
        futures.wait(self.publish_futures, return_when=futures.ALL_COMPLETED)

if __name__ == "__main__":
    
    publish_object = api_to_pubsub()
    for i in range(1):
        message = publish_object.fetch_covid_data()
        # print(message)
        publish_object.send_to_topic(message)
        # sleep(20)