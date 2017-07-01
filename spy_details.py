from  datetime import  datetime

#list
friends = []

#functions class
class chat_message:
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me =raw_input("enter message")

class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name,
        self.salutation =salutation,
        self.age = age,
        self.rating = rating,
        self.is_online = True,
        self.chats = []
        self.current_status_message = None

#creating obj of class spy
spy_obj = Spy('priya','ms', 13, 4.5)

friend_one = Spy('Priyanka', 'Ms.', 19, 4.5)
friend_two = Spy('Archi', 'Ms.', 20, 4.3)
friend_three = Spy('No', 'Dr.', 30, 4.9)

friends = [friend_one, friend_two, friend_three]
