# Importing Pymongo driver for the database connectivity of our MongoDB Database with Python Programming Language
import pymongo

if __name__=="__main__":
    # creating a mongo client and establishing a localhost database connectivity
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    
    # creating a databse named as 'Movies'
    db = client['Movies']
    
    # creating a collection into the mongoDB database 'Movies'
    collection = db['MoviesDetails']
    
    # creating a list of data to be inserted
    List_of_Movies=[
        {'Movie Name':'Jab We Met','Lead Actor':'Shahid Kapoor','Actress':'Kareena Kapoor','Releasing Year':2007,'Director Name':'Imtiaz Ali'},
        {'Movie Name':'Golmaal Again','Lead Actor':'Ajay Devgan','Actress':'Parineeti Chopra','Releasing Year':2017,'Director Name':'Rohit Shetty'},
        {'Movie Name':'Yeh Jawaani Hai Deewani','Lead Actor':'Ranbeer Kapoor','Actress':'Deepika Padukone','Releasing Year':2013,'Director Name':'Ayan Mukerji'},
        {'Movie Name':'Dear Zindagi','Lead Actor':'Shah Rukh Khan','Actress':'Alia Bhatt','Releasing Year':2016,'Director Name':'Gauri Shinde'},
        {'Movie Name':'Dream Girl','Lead Actor':'Ayushmann Khurrana','Actress':'Nushrat Bharucha','Releasing Year':2019,'Director Name':'Raaj Shaandilyaa'}
    ]

# inserting data into the collection
collection.insert_many(List_of_Movies)  

# quering all rows from the movies table
allDocs=collection.find()
for item in allDocs:
    print(item)

# query with parameter 'Lead Actor'
find_query=collection.find_one({'Lead Actor': 'Ajay Devgan'})
print(find_query)
   