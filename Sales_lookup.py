#!/usr/bin/env python

### import mongoSettings.py and other required libraries
from mongoSettings import *
import pymongo
import sys
import random
import uuid
import math
import string
### sys.version_info.major : to identify python version (major release identifier)

### open mongo connection
mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=MONGO_CONNECTION_TIMEOUT)
db = mongo_client[DATABASE_NAME]

### main logic
try:

	### lookup_email_servers : delete existing data & load new data
	les = db["lookup_email_servers"]
	les.delete_many({})
	les_docs = [
	{ "row_id":  1, "email_server": "@gmail.com" } ,
	{ "row_id":  2, "email_server": "@yahoo.com" } ,
	{ "row_id":  3, "email_server": "@aol.com" } ,
	{ "row_id":  4, "email_server": "@mail.com" } ,
	{ "row_id":  5, "email_server": "@icloud.com" } ,
	{ "row_id":  6, "email_server": "@inbox.com" } ,
	{ "row_id":  7, "email_server": "@email.net" } ,
	{ "row_id":  8, "email_server": "@fastmail.com" } ,
	{ "row_id":  9, "email_server": "@lycos.com" } ,
	{ "row_id": 10, "email_server": "@hushmail.com" }
	]
	les.insert_many(les_docs)
	print("loaded data into sales.lookup_email_servers")

	### lookup_usa_states : delete existing data & load new data
	lus = db["lookup_usa_states"]
	lus.delete_many({})
	lus_docs = [
	{ "row_id":  1, "state_code": "AK", "state_name": "Alaska" } ,
	{ "row_id":  2, "state_code": "AL", "state_name": "Alabama" } ,
	{ "row_id":  3, "state_code": "AR", "state_name": "Arkansas" } ,
	{ "row_id":  4, "state_code": "AZ", "state_name": "Arizona" } ,
	{ "row_id":  5, "state_code": "CA", "state_name": "California" } ,
	{ "row_id":  6, "state_code": "CO", "state_name": "Colorado" } ,
	{ "row_id":  7, "state_code": "CT", "state_name": "Connecticut" } ,
	{ "row_id":  8, "state_code": "DC", "state_name": "District of Columbia" } ,
	{ "row_id":  9, "state_code": "DE", "state_name": "Delaware" } ,
	{ "row_id": 10, "state_code": "FL", "state_name": "Florida" } ,
	{ "row_id": 11, "state_code": "GA", "state_name": "Georgia" } ,
	{ "row_id": 12, "state_code": "HI", "state_name": "Hawaii" } ,
	{ "row_id": 13, "state_code": "IA", "state_name": "Iowa" } ,
	{ "row_id": 14, "state_code": "ID", "state_name": "Idaho" } ,
	{ "row_id": 15, "state_code": "IL", "state_name": "Illinois" } ,
	{ "row_id": 16, "state_code": "IN", "state_name": "Indiana" } ,
	{ "row_id": 17, "state_code": "KS", "state_name": "Kansas" } ,
	{ "row_id": 18, "state_code": "KY", "state_name": "Kentucky" } ,
	{ "row_id": 19, "state_code": "LA", "state_name": "Louisiana" } ,
	{ "row_id": 20, "state_code": "MA", "state_name": "Massachusetts" } ,
	{ "row_id": 21, "state_code": "MD", "state_name": "Maryland" } ,
	{ "row_id": 22, "state_code": "ME", "state_name": "Maine" } ,
	{ "row_id": 23, "state_code": "MI", "state_name": "Michigan" } ,
	{ "row_id": 24, "state_code": "MN", "state_name": "Minnesota" } ,
	{ "row_id": 25, "state_code": "MO", "state_name": "Missouri" } ,
	{ "row_id": 26, "state_code": "MS", "state_name": "Mississippi" } ,
	{ "row_id": 27, "state_code": "MT", "state_name": "Montana" } ,
	{ "row_id": 28, "state_code": "NC", "state_name": "North Carolina" } ,
	{ "row_id": 29, "state_code": "ND", "state_name": "North Dakota" } ,
	{ "row_id": 30, "state_code": "NE", "state_name": "Nebraska" } ,
	{ "row_id": 31, "state_code": "NH", "state_name": "New Hampshire" } ,
	{ "row_id": 32, "state_code": "NJ", "state_name": "New Jersey" } ,
	{ "row_id": 33, "state_code": "NM", "state_name": "New Mexico" } ,
	{ "row_id": 34, "state_code": "NV", "state_name": "Nevada" } ,
	{ "row_id": 35, "state_code": "NY", "state_name": "New York" } ,
	{ "row_id": 36, "state_code": "OH", "state_name": "Ohio" } ,
	{ "row_id": 37, "state_code": "OK", "state_name": "Oklahoma" } ,
	{ "row_id": 38, "state_code": "OR", "state_name": "Oregon" } ,
	{ "row_id": 39, "state_code": "PA", "state_name": "Pennsylvania" } ,
	{ "row_id": 40, "state_code": "RI", "state_name": "Rhode Island" } ,
	{ "row_id": 41, "state_code": "SC", "state_name": "South Carolina" } ,
	{ "row_id": 42, "state_code": "SD", "state_name": "South Dakota" } ,
	{ "row_id": 43, "state_code": "TN", "state_name": "Tennessee" } ,
	{ "row_id": 44, "state_code": "TX", "state_name": "Texas" } ,
	{ "row_id": 45, "state_code": "UT", "state_name": "Utah" } ,
	{ "row_id": 46, "state_code": "VA", "state_name": "Virginia" } ,
	{ "row_id": 47, "state_code": "VT", "state_name": "Vermont" } ,
	{ "row_id": 48, "state_code": "WA", "state_name": "Washington" } ,
	{ "row_id": 49, "state_code": "WI", "state_name": "Wisconsin" } ,
	{ "row_id": 50, "state_code": "WV", "state_name": "West Virginia" } ,
	{ "row_id": 51, "state_code": "WY", "state_name": "Wyoming" }
	]
	lus.insert_many(lus_docs)
	print("loaded data into sales.lookup_usa_states")

	### lookup_product_categories : delete existing data & load new data
	lpc = db["lookup_product_categories"]
	lpc.delete_many({})
	lpc_docs = [
	{ "row_id":  1, "product_category": "Books" } ,
	{ "row_id":  2, "product_category": "Games" } ,
	{ "row_id":  3, "product_category": "Movies" } ,
	{ "row_id":  4, "product_category": "Computers" } ,
	{ "row_id":  5, "product_category": "Audio Systems" } ,
	{ "row_id":  6, "product_category": "Baby Products" } ,
	{ "row_id":  7, "product_category": "Collectibles" } ,
	{ "row_id":  8, "product_category": "Gift Cards" } ,
	{ "row_id":  9, "product_category": "Appliances" } ,
	{ "row_id": 10, "product_category": "Garden Tools" } ,
	{ "row_id": 11, "product_category": "Music" } ,
	{ "row_id": 12, "product_category": "Fine Arts" } ,
	{ "row_id": 13, "product_category": "Pet Supplies" } ,
	{ "row_id": 14, "product_category": "Software" } ,
	{ "row_id": 15, "product_category": "Office Products" } ,
	{ "row_id": 16, "product_category": "Magazines" } ,
	{ "row_id": 17, "product_category": "Beauty Products" } ,
	{ "row_id": 18, "product_category": "Electronics" } ,
	{ "row_id": 19, "product_category": "Light Bulbs" } ,
	{ "row_id": 20, "product_category": "Travel Gear" }
	]
	lpc.insert_many(lpc_docs)
	print("loaded data into sales.lookup_product_categories")

	### lookup_user_platforms : delete existing data & load new data
	lup = db["lookup_user_platforms"]
	lup.delete_many({})
	lup_docs = [
	{ "row_id":  1, "platform": "Android Phone" } ,
	{ "row_id":  2, "platform": "Android Tablet" } ,
	{ "row_id":  3, "platform": "iPhone" } ,
	{ "row_id":  4, "platform": "iPad" } ,
	{ "row_id":  5, "platform": "Mac OS" } ,
	{ "row_id":  6, "platform": "BlackBerry" } ,
	{ "row_id":  7, "platform": "Linux" } ,
	{ "row_id":  8, "platform": "ChromeBook" } ,
	{ "row_id":  9, "platform": "Firefox" } ,
	{ "row_id": 10, "platform": "Mozilla" }
	]
	lup.insert_many(lup_docs)
	print("loaded data into sales.lookup_user_platforms")

except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	output_message = "for SalesApp : Initial Lookup Data Load Completed."
	print(output_message)


### close mongo connection
mongo_client.close()
