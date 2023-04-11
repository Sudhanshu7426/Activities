def Earthquake_Impact(SP):
    if SP<2:
        return "Micro Earthquake"
    elif 2<=SP<3:
        return "Very Minor Earthquake"
    elif 3<=SP<4:
        return "Minor Earthquake"
    elif 4<=SP<5:
        return "Light Earthquake"
    elif 5<=SP<6:
        return "Moderate Earthquake"
    elif 6<=SP<7:
        return "Strong Earthquake"
    elif 7<=SP<8:
        return "Major Earthquake"
    else:
        return "Great Earthquake"
print(Earthquake_Impact(5))
