email = input()
if "@" in email and "." and email.rfind('.') >  email.find('@'):
    print("Ok")
else:
    print("Mistake")