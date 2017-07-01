from spy_details import*
from steganography.steganography import Steganography
from colorama import init,Fore,Style
from datetime import datetime

#reading chat_history
def read_chat_history():
    read_for = select_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            init(autoreset=True)
            msg_chat=Fore.BLUE+chat.time.strftime("%d %b %y")
            print '[%s] %s: %s' %(msg_chat ,'You said:' ,chat.message)
        else:
            print '[%s] %s said: %s' % (msg_chat, friends[read_for].name, chat.message)

#starting chat
def start_chat(user):

    result = True
    while result:
        choice = menu_choices()

        # checking the choices.
        if (choice == 1):
            add_status()
        elif(choice == 2):
            add_friend()
        elif(choice == 3):
            send_message()
        elif(choice == 4):
            read_message()
        elif(choice == 5):
            read_chat_history()
        elif(choice == 6):
            result = False
        else:
            print ("Wrong choice.Sorry you are not of the correct age to be a spy")
#introducing menu_choice
def menu_choices():
    print("1. Add a status")
    print("2. Add a friend")
    print("3. Send a secret message")
    print("4. Receive/Read secret message")
    print("5. Read chat History")
    print("6. Exit Application.")

    choice = int(raw_input("Enter your choice: "))

    # return choice
    return  choice

#adding status
def add_status():
    all_status = ['available', 'sleeping', 'at work']
    choice = int(raw_input("press 1 to add new status or press other key to add other status"))
    if choice == 1:
        current_status = raw_input("enter new status")
        all_status.append(current_status)
    else:
        count = 1
        for temp in all_status:
            print("%d %s" % (count, temp))
            count += 1
        choose = int(raw_input("which status you want?"))
        current_status = all_status[choose - 1]

#adding friend
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
    return len(friends)

#selecting friend
def select_friend():
    item = 0
    for friend in friends:
        print (friend.name, friend.age,friend.rating)
        item = item + 1
    #selecting friends.
    friend_choice = int(raw_input("choose: "))

    frnd = int(friend_choice) - 1
    return friend_choice

#sending message
def send_message():
    friend_choice = select_friend()
    original_image='nature.jpg'
    output_path ='output.jpg'
    #its secret message
    text = 'YOO I DID IT.FINALLY I AM FEELING GOOD'

    Steganography.encode(original_image,output_path,text)
    new_chat = chat_message(text , True)
    friends[friend_choice].chats.append(new_chat)
    print ("Your secret message is ready")
send_message()

#reading message
def read_message():
    sender = select_friend()
    output_path =("output.jpg")
    get = Steganography.decode(output_path)
    print get
    new_chat = chat_message( get,False)
    friends[sender].chats.append(new_chat)
    print("your message has been sent")
read_message()

