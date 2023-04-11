wl = float(input("Enter a wavelength in nanometers: "))

if 380 <= wl < 450:
    print("The color is violet.")
elif 450 <= wl < 495:
    print("The color is blue.")
elif 495 <= wl < 570:
    print("The color is green.")
elif 570 <= wl < 590:
    print("The color is yellow.")
elif 590 <= wl < 620:
    print("The color is orange.")
elif 620 <= wl <= 750:
    print("The color is red.")
else:
    print("Error: wavelength must be between 380 and 750 nanometers.")
