def discount(amount,prime_member,friday):
    if prime_member and friday:
        return (amount-((23*amount)/100))
    elif prime_member:
        return (amount-((15*amount)/100))
    else:
        return 'No discount'
        
print(discount(1200,True,False))
