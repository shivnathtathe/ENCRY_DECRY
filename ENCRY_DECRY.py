def converter():
    keys = 'abcdefghijklmnopqrstuvwxyz !?#@$%^&*,.5312468097-_+=)({}[]:;"/'
    values = keys[-1] + keys [0:-1]

    encryptDict = dict(zip(keys, values))
    decryptDict = dict(zip(values, keys))

    message = input("please enter your message to encrypt or decrypt : ")
    case = input("please choose the option : Encode(E) OR Decode(D) : ")

    if case.upper() == 'E':
        newMessage = ''.join([encryptDict[letter] for letter in message.lower()])

    elif case.upper() == 'D':
            newMessage = ''.join([decryptDict[letter] for letter in message.lower()])

    else:
        print("please enter a correct choice")  

    return newMessage.capitalize()

print(converter())