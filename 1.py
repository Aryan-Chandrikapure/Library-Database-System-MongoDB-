#print("Heelo wold")
import pymongo

if __name__=="__main__":
    print("welcome to Library")
    client =pymongo.MongoClient("localhost:27017")
    print(client)
    db=client['Library']
    collection=db['Library_collection']