def chit_word_application(message):
    word=message.split()
    if len(word) <=30:
        return message
    else:
        return 'message is greater then 30 words'
        
        
b=input()
a=chit_word_application(b)
print(a)
