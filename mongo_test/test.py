import pymongo
from pymongo import MongoClient
# pip3 install pymongo
# Replace the placeholder string with your MongoDB connection string
mongo_uri = "mongodb+srv://<username>:<password>@musecluster.egcmgf4.mongodb.net/?retryWrites=true&w=majority"

# Create a MongoDB client and connect to the sample_training database
client = MongoClient(mongo_uri, ssl=True, tlsAllowInvalidCertificates=True)
db = client.ESD_Muse

# Get a handle to the User collection
User_collection = db.User

# Insert a user
# user = {'name': 'John Doe', 'email': 'johndoe@example.com','GroupId':'1','PlaylistId':'blablabla'}
# result = User_collection.insert_one(user)

#Insert a group
group_collection = db.group
group = {'group_id':1, 'created_by':'John Doe', 'group_name':'power rangers'}
result = group_collection.insert_one(group)
#Insert a friend
friend_collection = db.friend
friend = {'group_id':1,'friend_email':'donald@gmail.com','friend_name':'donald'}
result = friend_collection.insert_one(friend)
#Insert a recommendation
recommendations_collection = db.recommendations
recommendation = {'group_id':1,'recommended_playlist_id':'5E0Em3Qd5vJmO93rJS3IPM?si=df574f938a08406b'}
result = recommendations_collection.insert_one(recommendation)
#Insert a error_log
error_log_collection = db.error_log
error_log = {'error_code':200,'error_msg':'bad connection','datetime':'2023-03-20 14:15:02.886664'}
result = error_log_collection.insert_one(error_log)

# Print the inserted_id
# print(result.inserted_id)


#CREATING ACCOUNTS
emails=['mdnguyen.2021@scis.smu.edu.sg','jfiore.2021@scis.smu.edu.sg','zllow.2021@scis.smu.edu.sg','jasperchong.2021@scis.smu.edu.sg','jaron.chan.2021@business.smu.edu.sg',]
for email in emails:
    pw=email.split('@')
    