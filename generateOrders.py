#!/usr/bin/env python

### import mongoSettings.py and other required libraries
from mongoSettings import *
import pymongo
from datetime import datetime, date, timedelta
import sys
import random
import uuid
import math
import string

### sys.version_info.major : to identify python version (major release identifier)

### user is expected to pre-generate 10000 users using SalesApp_GenerateUsers.py
var_users_count    = 10000

### user is expected to pre-generate 50000 products using SalesApp_GenerateProducts.py
var_products_count = 50000

v_number_of_orders = 0

### v_max_orders should be greater than 10
v_max_orders = 20

### main logic
try:
	### open mongo connection
	mongo_client = pymongo.MongoClient(MONGO_CONNECTION_STRING, serverSelectionTimeoutMS=MONGO_CONNECTION_TIMEOUT)
	db = mongo_client[DATABASE_NAME]

	saos = db["sales_orders"]

	### generate orders using for loop - start
	for var_orders in range(1, random.randint(10, v_max_orders)):

		### pick a user
		usr = db["users"]
		usr_rec = usr.find({ "user_id": random.randint(1, var_users_count) })[0]
		var_user_id           = usr_rec['user_id']
		var_user_email_id     = usr_rec['user_email_id']
		var_user_name         = usr_rec['user_name']
		var_user_phone_number = usr_rec['user_phone_number']
		var_user_platform     = usr_rec['user_platform']
		var_user_state_code   = usr_rec['user_state_code']

		ord_usr_doc = {
		          "user_id": var_user_id           ,
		    "user_email_id": var_user_email_id     ,
		        "user_name": var_user_name         ,
		"user_phone_number": var_user_phone_number ,
		    "user_platform": var_user_platform     ,
		  "user_state_code": var_user_state_code
		}
		
		### setup order info
		var_order_date                          = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
		var_order_timestamp                     = datetime.now().replace(microsecond=0)
		var_order_code_temp                     = str(uuid.uuid4()).replace('-', '')
		var_order_code                          = var_order_code_temp[0:4] + "-" + var_order_code_temp[4:8] + "-" + var_order_code_temp[8:12]
		var_order_discount_percent				= random.randint(0, 5)
		var_order_estimated_shipping_date		= var_order_date + timedelta(days=random.randint(3, 20))
		var_order_grand_total                   = 0
		var_order_number_of_products            = 0
		var_order_total                         = 0

		ord_prd_docs = []

		### generate order-products using for loop - start
		for var_order_products in range(1, random.randint(3, 8)):

			### pick a product
			prdt = db["products"]
			prdt_rec = prdt.find({ "product_id": random.randint(1, var_products_count) })[0]
			var_product_id             = prdt_rec['product_id']
			var_product_category       = prdt_rec['product_category']
			var_product_code           = prdt_rec['product_code']
			var_product_name           = prdt_rec['product_name']
			var_product_price          = prdt_rec['product_price']
			var_product_qoh            = prdt_rec['product_qoh']
			var_product_sold_quantity  = random.randint(2, 5)
			var_product_price_total    = (var_product_price * var_product_sold_quantity)

			### save order-products in db only if product quantity on hand is good
			if ( var_product_qoh > (var_product_sold_quantity+50) ):

				ord_prd_doc = {
				           "product_id": var_product_id             ,
				     "product_category": var_product_category       ,
				         "product_code": var_product_code           ,
				         "product_name": var_product_name           ,
				   "product_price_each": var_product_price          ,
				  "product_price_total": var_product_price_total    ,
				"product_sold_quantity": var_product_sold_quantity
				}

				ord_prd_docs.append(ord_prd_doc)

				var_new_product_qoh = var_product_qoh - var_product_sold_quantity
				prdt.update_one({ "product_id": var_product_id}, { "$set": { "product_qoh": var_new_product_qoh } })

				var_order_number_of_products = var_order_number_of_products + 1
				var_order_total = var_order_total + var_product_price_total

		### generate order-products using for loop - end

		var_order_grand_total = var_order_total - ( (var_order_total * var_order_discount_percent) / 100 )

		### save orders in db only if any products were sold
		if ( var_order_number_of_products > 0 ):

			order_doc = {
			                   "order_date": var_order_date                    ,
			              "order_timestamp": var_order_timestamp               ,
			                   "order_code": var_order_code                    ,
			       "order_discount_percent": var_order_discount_percent        ,
			"order_estimated_shipping_date": var_order_estimated_shipping_date ,
			            "order_grand_total": var_order_grand_total             ,
			     "order_number_of_products": var_order_number_of_products      ,
			                  "order_total": var_order_total                   ,
			                 "user_details": ord_usr_doc                       ,
			       "order_products_details": ord_prd_docs
			}

			saos.insert_one(order_doc)

			v_number_of_orders = v_number_of_orders + 1

	### generate orders using for loop - end


except Exception as e:
	### something went wrong
	output_message = str(var_order_timestamp) + " | something went wrong."
	print(output_message)
	print(e)
else:
	### all went well
	output_message = str(var_order_timestamp) + " | " + str(v_number_of_orders) + " orders generated."
	print(output_message)
	# print("Done.")


### close mongo connection
mongo_client.close()
