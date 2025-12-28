# You are building a simple app that registers users. 
# You want to separte concerns: getting input, validating it, and saving it 
# Task : 
#     1) Write register_user that calls : 
#         . get_input()
#         . validate_input()
#         . save_to_db() 

def get_input():
    print("Getting user input")

def valldate_input():
    print("Validating the user info")


def save_to_db():
    print("saving to data base ")
    
def register_user():
    get_input()
    valldate_input()
    save_to_db()
    print("User register Successfully")        

register_user()    