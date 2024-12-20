import pymongo

if __name__ == "_main_":
    print("Welcome to Library")
    client = pymongo.MongoClient("localhost:27017")
    print(client)
    db = client['Library']
    collection = db['Library_collection']
    
    # Fetch and print all documents
    print("All documents in the collection:")
    for document in collection.find():
        print(document)