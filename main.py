#importing class spy
from test1 import friends, Spy
#importing datetime
from datetime import datetime
#importing steaganography
from steganography.steganography import Steganography
#CREATING LIST
# friend1 =spy("priyanka", "ms", 20, 4.5)
# friend2 =spy("prince", "mr", 20, 3.6)
# friend3 =spy("bond", "mr", 22, 5)
# friends = [friend1, friend2, friend3]
def start_chat():
    friend1 =Spy_user("priyanka", "ms", 20, 3.5)
    friend2 =Spy_user("priya", "ms", 16, 5)
    friend3 =Spy_user("prince", "ms", 12, 4.5)


class chat_message:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me =raw_input("enter message")
#adding status
def add_status():
    all_status = ['available', 'sleeping']
    choice=int(raw_input("press 1 to add new status or press other key to add other status"))
    if choice==1:
        current_status=raw_input("enter new status")
        all_status.append(current_status)
    else:
        count=1
        for temp in all_status:
            print("%d %s" %(count,temp))
            count+=1
        choose=int(raw_input("which status you want?"))
        current_status=all_status[choose-1]



print("welcome to spychat")
user = raw_input("Continue as default user or new user.\n Press 'Y' to create new user or any other key to login as default user.")
if user.upper()== 'Y':
    spy_user = Spy("bond","mr", 20,4.5)
    print("Welcome " + spy_user.salutation + " " + spy_user.name)
   # start_chat(spy_user)
start_chat()



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
    add_status()
#adding friend
#functions
def add_friend():
    new_friend = Spy('','',0,0.0)
    new_friend.name = raw_input("enter friends name")
    new_friend.salutation = raw_input("enter mr or ms")
    new_friend.age =int(raw_input("enter age"))
    new_friend.rating = float(raw_input("enter rating"))
    if len(new_friend.name) > 0 and new_friend.age > 12 :
        friends.append(new_friend)
    else:
        print 'Invalid entry. We cant add spy with the details you provided'

#selecting friend
def select_friend():
    item = 0
    for choose in friends:
        print ("%s %d %.2f" %(choose.name, choose.age,choose.rating))
        item = item + 1
    #selecting friends.
    friend_choice = int(raw_input("choose: "))

    frnd = int(friend_choice) - 1
    return frnd

#calling function (remain)
select_friend()
#sending a message
original_image = raw_input("enter image")
def send_message():
    friend_choice = select_friend()
    output_path =raw_input("enter output path")
    text = raw_input("enter text")
    Steganography.encode = (original_image,output_path,text)
    new_chat = \
        chat_message(text , True)
    friends[friend_choice].chats.append(new_chat)
    print ("Your secret message is ready")
send_message()
#for reading message
def read_message():
    sender = select_friend()
    output_path =raw_input("output.jpg")
    text =raw_input("text")
    secret_text =Steganography.decode(output_path)
    new_chat = chat_message(text, True)
    friends[sender].chats.append(new_chat)
    print("your message has been sent")
read_message()

#reading chat_history
def read_chat_history():
    read_for = select_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %b %y"),'You said:' ,chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %b %y"), friends[read_for].name, chat.message)