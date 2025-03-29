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

v_number_of_products = 0

### input verification
# if (len(sys.argv) < 2):
# 	sys.exit('ERROR : Missing Input. Requires 1 Number Input.')
# try:
# 	input_var = int(sys.argv[1])
# except:
# 	sys.exit('ERROR : Requires 1 Number Input.')

# code will generate 50,000 products
input_var = 50000

### main logic
try:
	### open mongo connection
	mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=MONGO_CONNECTION_TIMEOUT)
	db = mongo_client[DATABASE_NAME]

	### products : delete existing data & generate new data
	prds = db["products"]
	prds.delete_many({})

	### generate data using for loop
	for var_product_id in range(1, input_var+1):

		lpc = db["lookup_product_categories"]
		lpc_rec = lpc.find({ "row_id": random.randint(1, 20) })[0]

		var_product_category = lpc_rec['product_category']

		var_product_code = str(uuid.uuid4()).replace('-', '')[1:13]
		var_product_name = str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 9)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 9)]
		var_product_description = str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 6)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(6, 9)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(3, 5)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(7, 11)]

		var_product_price = float( str(random.randint(10, 60)) + '.' + str(random.randint(0, 99)) )
		var_product_qoh = random.randint(555, 5555)

		prd_doc = {
		         "product_id": var_product_id            ,
		       "product_code": var_product_code          ,
		       "product_name": var_product_name          ,
		"product_description": var_product_description   ,
		   "product_category": var_product_category      ,
		      "product_price": var_product_price         ,
		        "product_qoh": var_product_qoh
		}

		prds.insert_one(prd_doc)

		v_number_of_products = var_product_id

except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	output_message = str(v_number_of_products) + " products generated."
	print(output_message)
	print("Done.")


### close mongo connection
mongo_client.close()
