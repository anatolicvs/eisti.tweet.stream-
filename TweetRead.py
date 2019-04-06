from datetime import timezone
from email.utils import parsedate_tz
from datetime import datetime, timedelta
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import socket
import json
from TweetDocument import TweetDocument
from mongoengine import *
from datetime import datetime


connect(
    db='data-bi-eisti',
    username='eisti',
    password='foe9cohRaice',
    host='mongodb://eisti:foe9cohRaice@ds145474.mlab.com:45474/data-bi-eisti'
)


# Set up your credentials
consumer_key = 'wQ911IIChpFpu1ilnii02Kb4m'
consumer_secret = 'r6N0hOWYajP1ohwdJpuGAu0bcZr7ijSOXqWfejb2fD4p2fjQvE'
access_token = '322944700-Qmlu7oTK0SV5X81HK8dgnWRwYwUC3BwhGbvgN3HL'
access_secret = 'mkdBNmtgb3ugu5uJQ92bKLGbXfkGc7Qd04rllYeuokfft'


class TweetsListener(StreamListener):

    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            msg = json.loads(data)
            if msg["user"]["location"]:

                td = TweetDocument(
                    MESSAGE_ID=msg["id_str"],
                    MESSAGE_POSTED_TIME=datetime.strptime(msg["created_at"], '%a %b %d %H:%M:%S %z %Y').replace(
                        tzinfo=timezone.utc).astimezone(tz=None).strftime('%Y-%m-%d %H:%M:%S'),
                    MESSAGE_BODY=msg["text"],
                    USER_ID=msg["user"]["id_str"],
                    # USER_LOCATION=msg["geo"]["coordinates"],
                    # USER_GENDER=msg["user"][""],
                    # USER_COUNTRY=msg["place"]["country"],
                    USER_COUNTRY=msg["user"]["location"],
                    # USER_CITY=msg["place"]["full_name"],
                    # USER_PLACE_TYPE=msg["place"]["place_type"],
                    MESSAGE_LANGUAGE=msg["lang"],
                    RETWEET_COUNT=int(msg["retweet_count"]),
                    FAVORITE_COUNT=int(msg["favorite_count"]),
                    REPLY_COUNT=int(msg["reply_count"]),
                    USER_FOLLOWERS_NUM=int(msg["user"]["followers_count"]),
                    USER_FRIENDS_COUNT=int(msg["user"]["friends_count"])
                    # USER_FOLLOWERS_NUM=int(msg["user"])
                )
                td.save()
            else:
                print("There is no place information on tweet")

            self.client_socket.send(msg['text'].encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True


def sendData(c_socket):
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)

    twitter_stream = Stream(auth, TweetsListener(c_socket))
    twitter_stream.filter(track=['#MachineLearning'])


if __name__ == "__main__":
    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "10.183.226.17"     # Get local machine name
    port = 5555                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port

    print("Listening on port: %s" % str(port))

    s.listen(5)                 # Now wait for client connection.
    c, addr = s.accept()        # Establish connection with client.

    print("Received request from: " + str(addr))

    sendData(c)
