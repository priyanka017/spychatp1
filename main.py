#importing libraries
from functions import *
from datetime import datetime
from spy_details import *
#start chat
print("WELCOME TO SPYCHAT")
user = raw_input("Continue as default user or new user.\n Press 'Y' to create new user or any other key to login as default user.")
existing=raw_input(user)
if user.upper()== 'Y':
    spy_user = Spy("Bond","mr", 20,4.5)
    start_chat(spy_user)
elif user.upper()=='N':
    spy_user = Spy('','', 0, 0.0)
    spy_user.name = raw_input("enter friends name")
    if len(spy_user.name) <=0:
        spy_user.name = raw_input("enter again")
    spy_user.salutation = raw_input("enter mr or ms")
    if len(spy_user.salutation) <= 0:
        spy_user.salutation = raw_input("enter again")
    spy_user.age =int (raw_input("enter age"))
    if spy_user.age > 12 or  spy_user < 50:
        spy_user.age = (raw_input("enter valid age"))
    spy_user.rating = float(raw_input("enter rating"))
    if spy_user.rating > 0 and spy_user.rating > 5:
        spy_user.rating = raw_input("enter again")
        start_chat(spy_user)
else:
    print'please enter a specific name'
