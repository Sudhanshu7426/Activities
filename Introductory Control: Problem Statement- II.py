Nint = 28
Div = 1
sum_of_divisors = 0
while Div < Nint:
    if Nint % Div == 0:
        sum_of_divisors += Div
    Div += 1
if sum_of_divisors > Nint:
    category = "abundant"
elif sum_of_divisors < Nint:
    category = "deficient"
else:
    category = "perfect"
print("The number", Nint, "is", category)
