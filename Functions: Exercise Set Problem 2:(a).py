def chit_chat_application(message):
    if len(message) <=200:
        return message
    else:
        return 'message is greater then 200 letters'


b=input()
a=chit_chat_application(b)
print(a)
