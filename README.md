🔹 What is Python?
Python হলো একটি high-level, interpreted, and easy-to-learn programming language.
এটি simple syntax এবং huge library support এর জন্য বিখ্যাত।

🔹 Variables
Variable মানে হলো ডেটা সংরক্ষণের জায়গা।

🔹 Data Types
Type	       Example	        Description

int	         10	              Whole numbers
float        3.14	            Decimal numbers
str	         "Hello"	        Text
bool	       True / False	    Logical value
list	       [1,2,3]	        Ordered, changeable
tuple	       (1,2,3)	        Ordered, unchangeable
dictionary	{"name":"Utpal"}	Key-value pairs
set	        {1,2,3}	          Unordered, unique

3️⃣ Operators
Python এ বিভিন্ন ধরনের operator আছে:
Type	        Example         	Description

Arithmetic	  +, -, *, /, %	    Mathematical
Assignment	  =, +=, -=	        Value assign
Comparison	  ==, !=, >, <	    Compare values
Logical	      and, or, not	    Combine conditions
Membership	  in, not in	      Check membership

4️⃣ Conditional Statements
🔹 if-else
age = 18
if age >= 18:
    print("You are adult")
else:
    print("You are minor")
    
🔹 elif
num = 0
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    
5️⃣ Loops
🔹 for loop
for i in range(5):
    print(i)
    
🔹 while loop
count = 0
while count < 5:
    print(count)
    count += 1
    
🔹 Loop Control
break, continue, pass

6️⃣ Functions
🔹 Define and Call Function
def greet(name):
    return "Hello " + name
print(greet("Utpal"))

🔹 Default Argument
def add(a, b=10):
    return a + b
print(add(5))

🔹 Lambda Function
square = lambda x: x*x
print(square(5))

🔹 What is OOP?
OOP (Object-Oriented Programming) হলো এমন একটি প্রোগ্রামিং পদ্ধতি যেখানে ডেটা ও সেই ডেটার সাথে সম্পর্কিত ফাংশনগুলোকে একসাথে রাখা হয় একটি Object এর মাধ্যমে।
এটি কোডকে আরও modular, reusable, এবং organized করে।

1️⃣ Class
Class হলো একটি blueprint বা template, যার মাধ্যমে object তৈরি করা হয়।

2️⃣ Object
Object হলো class-এর instance — অর্থাৎ, class থেকে তৈরি একটি বাস্তব entity।

3️⃣ Constructor (__init__)
Constructor হলো একটি special method যা object তৈরি হওয়ার সময় automatically call হয়।

4️⃣ Methods
Class-এর ভেতরে যেসব ফাংশন define করা হয়, সেগুলোকে method বলা হয়।

5️⃣ Inheritance (উত্তরাধিকার)
একটি class অন্য class-এর property ও method নিতে পারে — একে inheritance বলে।

6️⃣ Encapsulation
Encapsulation মানে হলো ডেটা ও ফাংশনগুলোকে একসাথে রেখে data hiding করা।

7️⃣ Polymorphism
একই নামের function কিন্তু আলাদা কাজ করে — একে polymorphism বলে।

8️⃣ Abstraction
অপ্রয়োজনীয় তথ্য লুকিয়ে শুধুমাত্র প্রয়োজনীয় অংশ দেখানো হয়।
এটি করতে abstract class ব্যবহার করা হয়।

11️⃣ Modules and Packages
🔹 Import Module
import math
print(math.sqrt(16))
