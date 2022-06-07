import pymongo
import pandas as pd

class variables:
    """Placeholder for reused strings in the across the module"""
    USERNAME = 'varshith'
    PASSWORD = 'Jjx0O63qLbueEXQa'

client = pymongo.MongoClient("mongodb+srv://{variables.USERNAME}:<{variables.PASSWORD}>@project-a-z.auh8afh.mongodb.net/?retryWrites=true&w=majority")
data = client.list_database_names()
print(data)