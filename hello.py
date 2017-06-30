

print "hello"
print"what's up?"
print"let/s get started"
spy_name=raw_input("welcome to spy_chat,what is your name?")
print "welcome" + spy_name +".glad to have you back with us."
spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
spy_name = spy_salutation + " " + spy_name
print "ok " + spy_name + ". I'd like to know a  bit more about you."
if len(spy_name) > 0:
    spy_name = raw_input("welcome to spy_chat,what is your name?")
    print "welcome" + spy_name + ".glad to have you back with us."
    spy_salutation = raw_input("What should we call you (Mr. or Ms.)?")
    spy_name = spy_salutation + " " + spy_name
    print "ok " + spy_name + ". I'd like to know a  bit more about you."

else:
    print "A spy needs a valid name. Try again."