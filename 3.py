import pymongo

if __name__=="main_":
    print("welcome to Library")
    client =pymongo.MongoClient("localhost:27017")
    print(client)
    db=client['Library']
    collection=db['Library_collection']
    #dictionary={"name":"HUzefa", "marks":88}
    #collection.insert_one(dictionary)
    insertThese=[
        {'Name':"Rahul",'Location':'Nagpur','author':"xyz"},
        {'Name':"Ishan",'Location':'Delhi','author':"hdj"},
        {'Name':"Kajal",'Location':'City','author':"jhdh"},
        {'Name':"Falgun",'Location':'Nagpur','author':"jhop"},
    ]
    
    
    collection.insert_many(insertThese)