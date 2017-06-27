
def add_status():
    all_status = ['available', 'sleeping']
    choice=int(raw_input("press 1 to add new status or press other key to add other status"))
    if choice==1:
        current_status=raw_input("enter new status")
        all_status.append(current_status)
    else:
        count=1
        for temp in all_status:
            print("%d. %s" %(count,temp))
            count+=1
        choose=int(raw_input("which status you want?"))
        current_status=all_status[choose-1]



print("welcome to spychat")
user = raw_input("Continue as default user or new user.\n Press 'Y' to create new user or any other key to login as default user.")
if user.upper()!= 'Y':
    from spy0 import spyage, spyrating, spyname
else:
    spyname = raw_input ("Enter your name:")
    while len(spyname)<=0:
        spyname =raw_input ("incorrect name.Please enter again:")
    spyage = int(raw_input ("Enter your age:"))
    while spyage>50 or spyage < 12 :
        spyage=raw_input("incorrect age.Please enter again:")
    spyrating = float(raw_input ("Enter your rating:"))
    while spyrating <0 or spyrating>5:
        spyrating=raw_input("incorrect rating.Please enter again:")
    add_status()

def add_friend():
