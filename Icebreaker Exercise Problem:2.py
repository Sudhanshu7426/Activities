sp=int(input("Enter Frequency "))
if sp<3*(10**9):
    print("Radio Waves")
elif 3*10**9<=sp<3*10**12:
    print("Microwaves")
elif 3*10**12<=sp<4.3*10**14:
    print("Infrared Light")
elif 4.3*10**9<=sp<7.5*10**14:
    print("Visible Light")
elif 7.5*10**14<=sp<3*10**17:
    print("Ultravoilet Light")
elif 3*10**19<=sp<3*10**19:
    print("X-rays")
else:
    print("Gamma rays")
