import cmath  # For handling complex numbers

print("Equation: ax^2 + bx + c ")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = b**2 - 4*a*c
d1 = cmath.sqrt(d)  # Use cmath.sqrt to handle complex roots

if d < 0:
    # The roots are complex numbers
    r1 = (-b + d1) / (2*a)
    r2 = (-b - d1) / (2*a)
    print("The first root: ", round(r1.real, 2), "+", round(r1.imag, 2), "i")
    print("The second root: ", round(r2.real, 2), "+", round(r2.imag, 2), "i")
else:
    # The roots are real numbers
    r1 = (-b + d1) / (2*a)
    r2 = (-b - d1) / (2*a)
    print("The first root: ", round(r1, 2))
    print("The second root: ", round(r2, 2))