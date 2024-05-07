import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
datebase = client['birthday']
db_person = datebase.persons 

def dateofbirth():
    print("Welcome to the birthday dictionary. We know the birthdays of:")
    for i in db_person.find():
        print(i["name"])
    while True:
        input_name = input("Who's birthday do you want to look up? =")
        res = db_person.find_one({"name":input_name})
        if res:
            re = res["dob"]
            print(f"{input_name}'s birthday is {re}.")
        else:
            print(f"Sorry, we don't have birthday information for {input_name}.")
        num = input("Do you want someone else date of birthday in your list[yes/no]=")
        if num == "no":
           break
        else:
           pass
       
dateofbirth()      
        