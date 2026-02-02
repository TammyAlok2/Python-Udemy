import csv
import os 

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME,"w",newline="",encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name","Phone","Email"])
        

def add_contact():
    name = input("Name ").strip()
    phone = input("Phone: ").strip()
    email = input("Email").strip()
    
    
    
        
        
        