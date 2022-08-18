import random,string, os

def pass_gen():
    password_length = int(input("How long should the password be? "))
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    for x in range(password_length):
        password.append(random.choice(password_characters))
    print(''.join(password))
    programPause = string(input("Type 'yes' to generate again or type 'no' to quit"))
    if programPause == 'yes':
        pass_gen()
    elif programPause == 'no':
        pass
print(pass_gen())
