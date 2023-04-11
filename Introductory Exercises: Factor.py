F=float(input('Input air temperature in degree celsius: '))
D=float(input('Input wind speed in km/h: '))
C = 13.12 + 0.6215 * F * (0.3965 * F - 11.37) * (D**0.16)
print(C)
