email = input()
if "@" in email and "." and email.find('.') >  email.find('@'):
    print("Ok")
else:
    print("Mistake")