import time, schedule
import requests, json
import boto3
import argparse
import functions

#    parser = argparse.ArgumentParser()
#    parser.add_argument('max_queue', type=int, help='put number for the queue');
#    args = parser.parse_args()
#    max_queue = args.max_queue

url = requests.get("https://drawtt.com/wp-json/drawtt/v1/getqueue")
text = url.text
data = json.loads(text)

success = (data["success"])
queue = (data["queue"])

def spot_monitor():
        print(text)
        if success == True:
            print("success is true")

        if queue > 15:
            print("The queue is over 15")
        #booting another one 
            functions.boot_spot_instance() 

        if queue <= 5:
            print("The queue is same with or less than  5, no need spot-request.")
        #shuting down one
            functions.shutdown_spot_instance()

#schedule.every(10).seconds.do(spot_monitor)
schedule.every(30).minutes.do(spot_monitor)


if __name__ == '__main__':

while True:
    schedule.run_pending()