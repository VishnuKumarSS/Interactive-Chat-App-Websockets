import pymongo
import gridfs

try:
    client = pymongo.MongoClient() # empty means localhost with mongodb default port 27017 # or we can pass MongoClient("127.0.0.1", "27017")
    # print(client)
except Exception:
    print("Error: ", Exception)

my_db = client["chatapp"]

my_collection = my_db['image_uploads']

# file system
fs = gridfs.GridFS(my_db)

# current_user = my_collection.find_one({'user_id':2})
# current_user
# img_id = current_user['img_id']
# img = my_db.fs.files.find_one({'_id':img_id})
# img
