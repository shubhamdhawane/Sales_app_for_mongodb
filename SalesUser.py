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

v_number_of_users = 0

### input verification
# if (len(sys.argv) < 2):
# 	sys.exit('ERROR : Missing Input. Requires 1 Number Input.')
# try:
# 	input_var = int(sys.argv[1])
# except:
# 	sys.exit('ERROR : Requires 1 Number Input.')

# code will generate 10,000 users
input_var = 10000

### main logic
try:
	### open mongo connection
	mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=MONGO_CONNECTION_TIMEOUT)
	db = mongo_client[DATABASE_NAME]

	### users : delete existing data & generate new data
	usrs = db["users"]
	usrs.delete_many({})

	### generate data using for loop
	for var_user_id in range(1, input_var+1):

		les = db["lookup_email_servers"]
		les_rec = les.find({ "row_id": random.randint(1, 10) })[0]

		lus = db["lookup_usa_states"]
		lus_rec = lus.find({ "row_id": random.randint(1, 51) })[0]
	
		lup = db["lookup_user_platforms"]
		lup_rec = lup.find({ "row_id": random.randint(1, 10) })[0]

		var_email_server = les_rec['email_server']
		var_state_code   = lus_rec['state_code']
		var_platform     = lup_rec['platform']

		var_user_name         = str(uuid.uuid4()).replace('-', '')[1:13]
		var_user_email_id     = var_user_name + var_email_server
		var_user_phone_number = str(random.randint(700, 900)) + '-' + str(random.randint(100, 900)) + '-' + str(random.randint(1001, 9999))

		usr_doc = {
		          "user_id": var_user_id            , 
		        "user_name": var_user_name          , 
		    "user_email_id": var_user_email_id      , 
		  "user_state_code": var_state_code         , 
		"user_phone_number": var_user_phone_number  , 
		    "user_platform": var_platform
		}

		usrs.insert_one(usr_doc)

		v_number_of_users = var_user_id

except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	output_message = str(v_number_of_users) + " users generated."
	print(output_message)
	print("Done.")


### close mongo connection
mongo_client.close()
