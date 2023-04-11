SP = float(input("Enter magnitude of Earthquake: "))

if SP<2:
    print("Micro Earthquake")
elif 2<=SP<3:
    print("Very Minor Earthquake")
elif 3<=SP<4:
    print("Minor Earthquake")
elif 4<=SP<5:
    print("Light Earthquake")
elif 5<=SP<6:
    print("Moderate Earthquake")
elif 6<=SP<7:
    print("Strong Earthquake")
elif 7<=SP<8:
    print("Major Earthquake")
else:
    print("Great Earthquake")
