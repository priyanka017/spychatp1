class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name,
        self.salutation =salutation,
        self.age = age,
        self.rating = rating,
        self.is_online = True,
        self.chats = []
        self.current_status_message = None

spy_obj = Spy('priya','ms', 13, 4.5)

friend_1 = Spy('Priyanka', 'Ms.', 19, 4.5)
friend_2 = Spy('Archi', 'Ms.', 20, 4.3)
friend_3 = Spy('No', 'Dr.', 30, 4.9)

friends = [friend_1, friend_2, friend_3]
