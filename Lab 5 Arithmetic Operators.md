# Lab 5: Arithmetic Operators

## Objective
The purpose of this lab is to learn how Python performs mathematical calculations using arithmetic operators. These operators are used in almost every Python program, from simple calculators to advanced cybersecurity scripts.

---

# Introduction

Arithmetic operators allow us to perform mathematical operations on numbers. Python supports several arithmetic operators that make calculations easy and efficient.

---

# Arithmetic Operators in Python

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| + | Addition | 10 + 5 | 15 |
| - | Subtraction | 10 - 5 | 5 |
| * | Multiplication | 10 * 5 | 50 |
| / | Division | 10 / 5 | 2.0 |
| // | Floor Division | 10 // 3 | 3 |
| % | Modulus | 10 % 3 | 1 |
| ** | Exponent | 2 ** 3 | 8 |

---

# Explanation of Each Operator

## Addition (+)
Adds two numbers together.

Example:
```python
print(5 + 3)
```

Output:
```
8
```

---

## Subtraction (-)

Subtracts one number from another.

Example:

```python
print(10 - 4)
```

Output:

```
6
```

---

## Multiplication (*)

Multiplies two numbers.

Example:

```python
print(6 * 7)
```

Output:

```
42
```

---

## Division (/)

Divides one number by another and returns a decimal if necessary.

Example:

```python
print(10 / 4)
```

Output:

```
2.5
```

---

## Floor Division (//)

Divides two numbers and returns only the whole-number result, removing the decimal part.

Example:

```python
print(10 // 3)
```

Output:

```
3
```

---

## Modulus (%)

Returns the remainder after division.

Example:

```python
print(10 % 3)
```

Output:

```
1
```

---

## Exponent (**)

Raises a number to a power.

Example:

```python
print(2 ** 5)
```

Output:

```
32
```

---

# Lab Program

```python
age = int(input("Enter your age: "))
child_age = int(input("Enter the child's age: "))
your_power = int(input("Enter the power for your age: "))
child_power = int(input("Enter the power for your child's age: "))

print()
print("Here are the results...")
print("Seven years ago:", age - 7)
print("Ten years from now:", age + 10)
print("You are", age / child_age, "times older than your child.")
print("Floor division of your ages:", age // child_age)
print("Modulus of your ages:", age % child_age)
print("Your age raised to the entered power:", age ** your_power)
print("Your child's age raised to the entered power:", child_age ** child_power)
print("Your ages combined:", age + child_age)
print("You are", age - child_age, "years older than your child.")
```

---

# What I Learned

- How to use arithmetic operators.
- The difference between division and floor division.
- How the modulus operator returns the remainder.
- How to raise numbers to powers using the exponent operator.
- How arithmetic operators can be combined in one program.

---

# Real-World Applications

Arithmetic operators are used in:

- Building calculator applications.
- Financial calculations.
- Data analysis.
- Game development.
- Cybersecurity scripts for calculations, timing, and statistics.
- Scientific computing.

---

# Challenge

Create your own calculator that asks the user for two numbers and displays the results of every arithmetic operator.

---

# Common Mistakes

- Forgetting to convert user input to integers.
- Dividing by zero.
- Confusing `/` with `//`.
- Thinking `%` gives the answer instead of the remainder.

---

# Key Takeaways

- Python has seven main arithmetic operators.
- `/` returns a decimal result.
- `//` returns only the whole-number result.
- `%` returns the remainder.
- `**` raises a number to a power.

---

# Achievement

🎉 Congratulations!

I successfully learned Python arithmetic operators and created a program that performs different mathematical operations using user input.

This knowledge forms the foundation for solving programming problems and developing automation and cybersecurity tools with Python.