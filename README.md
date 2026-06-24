# Decodelab-Internship-T-1
A collection of Cyber Security projects developed during DecodeLabs Internship using Python.
# 🔐 Password Strength Checker

## 📌 Project Overview

Password security is one of the most important aspects of cybersecurity. Weak passwords can be easily guessed or cracked by attackers, leading to unauthorized access to sensitive information. This project aims to evaluate the strength of a password based on several security criteria and classify it as Weak, Medium, or Strong.

The Password Strength Checker helps users understand whether their password is secure enough for use in online accounts, applications, and systems. It provides a simple yet effective method to analyze password quality using Python programming.

---

## 🎯 Objective

The main objective of this project is to create a Python-based application that analyzes a user's password and determines its strength based on predefined security rules.

The project focuses on:

* Password validation
* Security awareness
* String handling techniques
* Conditional logic implementation
* Basic cybersecurity concepts

---

## 🚀 Features

### ✅ Password Length Verification

Checks whether the password meets the minimum recommended length.

### ✅ Uppercase Letter Detection

Verifies if the password contains at least one uppercase letter (A-Z).

### ✅ Number Detection

Checks whether the password includes numeric digits (0-9).

### ✅ Special Character Detection

Identifies special characters such as:
@, #, $, %, &, !, *, etc.

### ✅ Password Strength Classification

Based on the security score, the password is categorized as:

* Weak Password
* Medium Password
* Strong Password

---

## 🛠 Technologies Used

| Technology | Purpose                           |
| ---------- | --------------------------------- |
| Python     | Core Programming Language         |
| VS Code    | Code Editor                       |
| GitHub     | Version Control & Project Hosting |

---

## 📂 Project Structure

PasswordStrengthChecker/

├── password_checker.py

├── README.md

└── screenshots/

---

## ⚙️ Working Methodology

### Step 1

The user enters a password.

### Step 2

The system analyzes the password based on:

* Length
* Uppercase letters
* Numbers
* Symbols

### Step 3

Each valid security parameter increases the score.

### Step 4

The final score is calculated.

### Step 5

The password is classified and displayed to the user.

---

## 🔄 Algorithm

1. Accept password input from user.
2. Initialize score = 0.
3. Check password length.
4. Check uppercase letters.
5. Check numeric digits.
6. Check special symbols.
7. Increase score for every satisfied condition.
8. Determine password strength.
9. Display result.

---

## 📊 Password Strength Criteria

| Score | Strength |
| ----- | -------- |
| 0 - 1 | Weak     |
| 2 - 3 | Medium   |
| 4     | Strong   |

---

## 💻 Sample Output

Example 1

Enter Password: abc123

Result: Weak Password

Example 2

Enter Password: Abc12345

Result: Medium Password

Example 3

Enter Password: Abc@12345

Result: Strong Password

---

## 🔒 Importance of Strong Passwords

Strong passwords help protect:

* Personal Accounts
* Banking Information
* Social Media Profiles
* Email Accounts
* Confidential Data

Using strong passwords significantly reduces the risk of cyberattacks and unauthorized access.

---

## 🎓 Learning Outcomes

After completing this project, the following concepts are understood:

* Python String Handling
* Conditional Statements
* Regular Expressions
* Cybersecurity Fundamentals
* Password Security Concepts
* Logic Building

---

## 📈 Future Enhancements

The project can be enhanced by adding:

* Password entropy calculation
* Password breach database checking
* Password suggestions
* GUI interface using Tkinter
* Real-time password strength meter
* Advanced security analysis

---

## ✅ Conclusion

The Password Strength Checker is a beginner-friendly cybersecurity project that demonstrates the importance of secure password creation. It helps users understand password security standards while improving programming and logical thinking skills. This project serves as a strong foundation for learning cybersecurity concepts and secure authentication practices.

---

## 👩‍💻 Author

**Anandi Bhayani**

Cyber Security Internship Project

DecodeLabs Internship Program

Batch 2026
