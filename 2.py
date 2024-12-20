import pymongo

if __name__=="main_":
    print("welcome to Library")
    client =pymongo.MongoClient("localhost:27017")
    print(client)
    db=client['Library']  
    collection=db['Library_collection']
    dictionary={"Name":"Aryan","location":"Nagpur","Author":"xyz"}
    collection.insert_one(dictionary)