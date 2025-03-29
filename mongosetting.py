#!/usr/bin/env python

### connection variables
MONGO_RW_HOST            = "172.31.10.210"
MONGO_RW_PORT            = "27017"
DATABASE_NAME            = "sales"
MONGO_CONNECTION_STRING  = "mongodb://" + MONGO_RW_HOST + ":" + MONGO_RW_PORT + "/"
MONGO_CONNECTION_TIMEOUT = 5000 ### in milli-seconds
