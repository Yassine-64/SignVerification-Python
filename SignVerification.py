
a = int(input("Veuillez entrer le premier nombre (a) : "))
b = int(input("Veuillez entrer le deuxième nombre (b) : "))


if (a > 0 and b > 0) or (a < 0 and b < 0):
    print("a et b sont de même signe.")
else:
    print("a et b ont des signes différents.")
