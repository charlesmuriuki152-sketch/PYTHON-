# Lab 04: Type Conversion

## Objective

Learn how to convert data from one data type to another in Python.

---

## Concepts Covered

- String (`str`)
- Integer (`int`)
- Float (`float`)
- Boolean (`bool`)
- Type conversion
- The `type()` function

---

## Notes

When using `input()`, Python always stores the value as a string.

To perform calculations, you must convert the input to the correct data type.

Examples:

- `int()` → Converts to an integer.
- `float()` → Converts to a decimal number.
- `str()` → Converts to a string.

The `type()` function is used to check the data type of a variable.

---

## Example Program

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height: "))
cybersecurity = True

print("My name is", name)
print("I am", age, "years old.")
print("Next year I will be", age + 1)
print("My height is", height)
print(cybersecurity)
print(type(cybersecurity))
```

---

## Challenge

Write a program that:

1. Asks for your name.
2. Asks for your favorite number.
3. Converts the number into an integer.
4. Multiplies it by 10.
5. Displays the result.

---

## Achievement

After completing this lab, I can:

- Accept user input.
- Convert between strings, integers, and floats.
- Perform calculations using converted values.
- Check the data type of variables.
- Understand why type conversion is important in Python and cybersecurity.