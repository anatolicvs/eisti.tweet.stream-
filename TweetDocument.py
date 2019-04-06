from mongoengine import *
import datetime

'''
root
 |-- MESSAGE_ID: string (nullable = true)
 |-- MESSAGE_POSTED_TIME: timestamp (nullable = true)
 |-- MESSAGE_BODY: string (nullable = true)
 |-- MESSAGE_LANGUAGE: string (nullable = true)
 |-- MESSAGE_LOCATION: string (nullable = true)
 |-- SOURCE: string (nullable = true)
 |-- USER_ID: string (nullable = true)
 |-- USER_GENDER: string (nullable = true)
 |-- USER_STATE: string (nullable = true)
 |-- USER_COUNTRY: string (nullable = true)
 |-- USER_CITY: string (nullable = true)
 |-- RETWEET_COUNT:  integer (nullable = true)
 |-- FAVORITE_COUNT: integer (nullable = true)
 |-- REPLY_COUNT: integer (nullable = true)
 |-- USER_FOLLOWERS_NUM: integer (nullable = true)
 |-- USER_FRIENDS_COUNT: integer (nullable = true)


  "user": {
    "id": 2244994945,
    "id_str": "2244994945",
    "name": "TwitterDev",
    "screen_name": "TwitterDev",
    "location": "Internet",
    "url": "https://dev.twitter.com/",
    "description": "Your source for Twitter news",
    "verified": true,
    "followers_count": 477684,
    "friends_count": 1524,
    "listed_count": 1184,
    "favourites_count": 2151,
    "statuses_count": 3121,
    "created_at": "Sat Dec 14 04:35:55 +0000 2013",
    "utc_offset": null,
    "time_zone": null,
    "geo_enabled": true,
    "lang": "en",
    "profile_image_url_https": "https://pbs.twimg.com/"
  }
}

'''


class TweetDocument(Document):
    MESSAGE_ID = StringField(max_length=120, required=True)
    MESSAGE_POSTED_TIME = DateTimeField(required=False)
    MESSAGE_BODY = StringField(max_length=250, required=False)
    USER_ID = StringField(max_length=120, required=False)
    # StringField(max_length=120, required=False)
    # ListField(FloatField(blank=True, null=True))
    USER_LOCATION = StringField(max_length=120, required=False)
    # USER_GENDER = StringField(max_length=20, required=False)
    USER_STATE = StringField(max_length=120, required=False)
    USER_COUNTRY = StringField(max_length=120, required=False)
    USER_CITY = StringField(max_length=120, required=False)
    MESSAGE_LANGUAGE = StringField(max_length=120, required=False)
    MESSAGE_LOCATION = StringField(max_length=120, required=False)
    RETWEET_COUNT = IntField()
    FAVORITE_COUNT = IntField()
    REPLY_COUNT = IntField()
    USER_FOLLOWERS_NUM = IntField()
    USER_FRIENDS_COUNT = IntField()
