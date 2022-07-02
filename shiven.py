print("a. velocity")
print("b. acceleration")
print("c. force")

user_choice = (input("what do you want to calculatr from above: "))

if user_choice in ["a","A"]:
    L = int(input("what is the distace covered by object(in m): "))
    T = int(input("what is the time the distace in covered in(in sec): "))
    v = L/T
    print(v,"m/s")
elif user_choice in ["b","B"]:
    L = int(input("what is the distace covered by object(in m): "))
    T = int(input("what is the time the distace in covered in(in sec): "))
    a = L/T**2
    print(a)
elif user_choice in ["c","C"]:
    M = int(input("what is the mass of the object(in g): "))
    L = int(input("what is the distace covered by object(in m): "))
    T = int(input("what is the time the distace in covered in(in sec): "))
    F = M/(L/T**2)
    print(F)
else:
    print("enter a valid value!")