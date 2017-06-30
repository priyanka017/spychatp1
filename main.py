#importing libraries
from functions import *
from spy_details import *

print("welcome to spychat")
user = raw_input("Continue as default user or new user.\n Press 'Y' to create new user or any other key to login as default user.")
if user.upper()== 'Y':
    spy_user = Spy("Bond","mr", 20,4.5)
    start_chat(spy_user)
else:
    spy_user = Spy('','', 0, 0.0)
    spy_user.name = raw_input("enter friends name")
    if len(spy_user.name) <=0:
        spy_user.name = raw_input("enter again")
    spy_user.salutation = raw_input("enter mr or ms")
    if len(spy_user.salutation) <= 0:
        spy_user.salutation = raw_input("enter again")
    spy_user.age =int (raw_input("enter age"))
    if spy_user.age < 12 or  spy_user > 50:
        spy_user.age = raw_input("enter again")
    spy_user.rating = float(raw_input("enter rating"))
    if spy_user.rating < 0 and spy_user.rting > 5:
        spy_user.rating = raw_input("enter again")

    start_chat(spy_user)