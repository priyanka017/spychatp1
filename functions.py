from spy_details import *

#reading chat_history
def read_chat_history():
    read_for = select_friend()
    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %b %y"),'You said:' ,chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime("%d %b %y"), friends[read_for].name, chat.message)

def start_chat(user):
    print("Welcome " + user.salutation + " " + user.name)
    print("What do you want to do next ??")

    result = True
    while result:
        choice = menu_choices()

        # checking the choices.
        if (choice == 1):
            add_status()
        elif (choice == 2):
            update_status()
        elif(choice == 3):
            add_friend()
        elif(choice == 4):
            send_message()
        elif(choice == 5):
            read_message()
        elif(choice == 6):
            read_chat_history()
        elif(choice == 7):
            result = False
        else:
            print ("Wrong choice. Please try again.")

def menu_choices():
    print("1. Add a status")
    print("2. Update a status")
    print("3. Add a friend")
    print("4. Send a secret message")
    print("5. Receive/Read secret message")
    print("6. Read chat History")
    print("7. Exit Application.")

    choice = int(raw_input("Enter your choice: "))

    # return choice
    return  choice


def update_status():
    #to be implemented.

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

def select_friend():
    item = 0
    for choose in friends:
        print ("%s %d %.2f" %(choose.name, choose.age,choose.rating))
        item = item + 1
    #selecting friends.
    friend_choice = int(raw_input("choose: "))

    frnd = int(friend_choice) - 1
    return frnd

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

def read_message():
    sender = select_friend()
    output_path =raw_input("output.jpg")
    text =raw_input("text")
    secret_text =Steganography.decode(output_path)
    new_chat = chat_message(text, True)
    friends[sender].chats.append(new_chat)
    print("your message has been sent")
read_message()

