import pymongo
import tkinter as tk
from tkinter import ttk

def connect_to_db():
    global client, db, collection
    try:
        client = pymongo.MongoClient("localhost:27017")
        db = client['Library']
        collection = db['Library_collection']
        status_label.config(text="Connected to MongoDB successfully!")
    except Exception as e:
        status_label.config(text=f"Error connecting to MongoDB: {str(e)}")

def insert_data():
    name = name_entry.get()
    location = location_entry.get()
    author = author_entry.get()

    if not name or not location or not author:
        status_label.config(text="Please fill in all fields.")
        return

    try:
        collection.insert_one({'Name': name, 'Location': location, 'author': author})
        status_label.config(text="Data inserted successfully!")
    except Exception as e:
        status_label.config(text=f"Error inserting data: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Library Database GUI")

# Create labels and entry fields
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

location_label = tk.Label(window, text="Location:")
location_label.pack()
location_entry = tk.Entry(window)
location_entry.pack()

author_label = tk.Label(window, text="Author:")
author_label.pack()
author_entry = tk.Entry(window)
author_entry.pack()

# Create buttons
connect_button = tk.Button(window, text="Connect to DB", command=connect_to_db)
connect_button.pack()

insert_button = tk.Button(window, text="Insert Data", command=insert_data)
insert_button.pack()

# Create a status label
status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()