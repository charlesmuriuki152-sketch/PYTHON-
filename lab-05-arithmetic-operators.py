# Lab 5: Arithmetic Operators

age = int(input("Enter your age: "))
child_age = int(input("Enter the child's age: "))
your_power = int(input("Enter the power for your age: "))
child_power = int(input("Enter the power for your child's age: "))

print()
print("========== RESULTS ==========")

# Addition
print("Your ages combined:", age + child_age)

# Subtraction
print("Seven years ago:", age - 7)
print("Ten years from now:", age + 10)
print("You are", age - child_age, "years older than your child.")

# Multiplication
print("Your age multiplied by 2:", age * 2)
print("Your child's age multiplied by 3:", child_age * 3)

# Division
print("You are", age / child_age, "times older than your child.")

# Floor Division
print("Floor division of your ages:", age // child_age)

# Modulus
print("Modulus of your ages:", age % child_age)

# Exponent
print("Your age raised to the entered power:", age ** your_power)
print("Your child's age raised to the entered power:", child_age ** child_power)

print()
print("Thank you for using the Arithmetic Operators program!")