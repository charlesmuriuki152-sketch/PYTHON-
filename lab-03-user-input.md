# Lab 03: User Input

## Objective

The objective of this lab is to learn how to collect information from a user using the `input()` function and display the entered data.

## What I Learned

In this lab, I learned:

- How to use the `input()` function.
- How to store user input in variables.
- How to display user-provided information.
- How to build an interactive Python program.

## Python Code

```python
name = input("Enter your name: ")
device = input("What device are you using? ")
os = input("What is its operating system? ")
ip_address = input("Check the IP address and type it here: ")
wifi_name = input("What is your WiFi name? ")
password = input("Enter password: ")

print()
print("User Information")
print("----------------")
print("Name:", name)
print("Device:", device)
print("Operating System:", os)
print("IP Address:", ip_address)
print("WiFi Name:", wifi_name)
print("Password:", password)
```

## Expected Output

```
Enter your name: Charles
What device are you using? Phone
What is its operating system? Android
Check the IP address and type it here: 10.6.7
What is your WiFi name? Ecospot Africa
Enter password: 4841

User Information
----------------
Name: Charles
Device: Phone
Operating System: Android
IP Address: 10.6.7
WiFi Name: Ecospot Africa
Password: 4841
```

## Key Takeaways

- `input()` allows Python programs to interact with users.
- Every value returned by `input()` is a string.
- User input can be stored in variables and displayed later.

## Conclusion

This lab introduced interactive programming using the `input()` function. These skills are important for creating cybersecurity tools that request information from users before performing tasks.