#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exercise 1: compare two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print("Both numbers are equal")


# In[2]:


# Exercise 2: Even or Odd Number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# In[3]:


# Exercise 3: Positive or Negative Number
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")


# In[4]:


# Exercise 4: Password Checker
password = input("Enter the password: ")

if password == "jayasthishreddy":
    print("Access granted.")
else:
    print("Access denied.")


# In[5]:


# Exercise 5: Age Checker
age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")


# In[6]:


# Exercise 6: Voting Eligibility
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


# In[7]:


# Exercise 7: Temperature Conversion
temperature_celsius = float(input("Enter the temperature in Celsius: "))

if temperature_celsius > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")


# In[8]:


# Exercise 8: Positive or Negative Number (Improved)
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")


# In[9]:


# Exercise 9: Grade Classification (Improved)
score = float(input("Enter the student's score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")


# In[10]:


# Exercise 10: Number Comparison (Improved)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print("Both numbers are equal")


# In[11]:


# Exercise 11: Odd or Even Number (Improved)
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")


# In[12]:


# Exercise 12: Positive, Negative, or Zero (Improved)
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive.")
elif num < 0:
    print(f"{num} is negative.")
else:
    print("The number is zero.")


# In[13]:


# Exercise 13: Age Group Classification
age = int(input("Enter your age: "))

if age < 13:
    print("Child.")
elif 13 <= age <= 19:
    print("Teenager.")
else:
    print("Adult.")


# In[14]:


# Exercise 14: Password Strength Checker
password = input("Enter the password: ")

if len(password) < 8:
    print("Weak.")
else:
    print("Strong.")


# In[15]:


# Exercise 15: Age Verification
age = int(input("Enter your age: "))

if age >= 21:
    print("You are allowed to enter.")
else:
    print("Access denied.")


# In[16]:


# Exercise 16: Number Comparison (Improved)
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 == num2:
    print("Both numbers are equal.")
else:
    print("The numbers are not equal.")


# In[17]:


# Exercise 17: Grading System
score = float(input("Enter the student's score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score <= 89:
    print("Grade: B")
elif 70 <= score <= 79:
    print("Grade: C")
elif 60 <= score <= 69:
    print("Grade: D")
else:
    print("Grade: F")


# In[19]:


# Exercise 18: Discount Calculator
original_price = float(input("Enter the original price: "))
discounted_price = 0.9 * original_price 

print(f"Final price after 10% discount: {discounted_price}")


# In[20]:


# Exercise 19: BMI Calculator
weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")


# In[21]:


# Exercise 20: Password Verification (Improved)
password = input("Enter the password: ")

if password == "password123":
    print("Access granted.")
else:
    print("Access denied.")


# In[38]:


# Exercise 21: Ticket Price Calculator
age = int(input("Enter your age: "))

if age <= 12:
    ticket_price = 5
elif 13 <= age <= 18:
    ticket_price = 8
else:
    ticket_price = 12

print(f"Ticket price: ${ticket_price}")



# In[39]:


# Exercise 22: Discount Coupon
purchase_amount = float(input("Enter the total purchase amount: "))

if purchase_amount >= 50:
    discount_amount = 0.1 * purchase_amount  # 10% discount
    final_amount = purchase_amount - discount_amount
    print(f"Final amount after 10% discount: {final_amount}")
else:
    print(f"Original amount: {purchase_amount}")


# In[40]:


# Exercise 23: Traffic Light Simulator
color = input("Enter a color (red, yellow, or green): ")

if color == "red":
    print("Stop.")
elif color == "yellow":
    print("Slow down.")
elif color == "green":
    print("Go.")
else:
    print("Invalid color.")


# In[41]:


# Exercise 24: Simple Calculator
num1 = float(input("Enter the first number: "))
operator = input("Enter an operator (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        result = None
else:
    print("Invalid operator.")
    result = None

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")


# In[42]:


# Exercise 25: Exam Result
exam_score = float(input("Enter your exam score as a percentage (0-100): "))

if 90 <= exam_score <= 100:
    print("Excellent")
elif 80 <= exam_score <= 89:
    print("Good")
elif 70 <= exam_score <= 79:
    print("Satisfactory")
elif 0 <= exam_score <= 69:
    print("Needs Improvement")
else:
    print("Invalid score. Please enter a percentage between 0 and 100.")


# In[ ]:




