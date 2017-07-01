from datetime import datetime
time=datetime.now()
print time()
def send_message():
    now_chat = {
        "message": text,
        "time":hours,

    }

    def start_chat(Spy):

        Spy.name = Spy.salutation + " " + Spy.name

        if Spy.age > 12 and Spy.age < 50:
            print "Authentication complete. Welcome " + Spy.name + " age: " \
                  + str(Spy.age) + " and rating of: " + str(Spy.rating) + " Proud to have you onboard"

    print("welcome to spychat")
    user = raw_input(
        "Continue as default user or new user.\n Press 'Y' to create new user or any other key to login as default user.")
    if user.upper() == 'Y':
        spy_user = Spy("Bond", "mr", 20, 4.5)
        start_chat(spy_user)
    elif user.upper() == 'N':
        spy_user = Spy('', '', 0, 0.0)
        spy_user.name = raw_input("enter friends name")
        if len(spy_user.name) <= 0:
            spy_user.name = raw_input("enter again")
        spy_user.salutation = raw_input("enter mr or ms")
        if len(spy_user.salutation) <= 0:
            spy_user.salutation = raw_input("enter again")
        spy_user.age = int(raw_input("enter age"))
        if spy_user.age > 12 or spy_user < 50:
            spy_user.age = raw_input("enter again")
        spy_user.rating = float(raw_input("enter rating"))
        if spy_user.rating < 0 and spy_user.rting > 5:
            spy_user.rating = raw_input("enter again")
            start_chat(spy_user)
    else:
        print'please enter a specific name'

