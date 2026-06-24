import tkinter as tk
from tkinter import messagebox
import re

def check_password():
    password = entry.get()

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 1:
        strength = "WEAK 🔴"
        color = "red"
    elif score <= 3:
        strength = "MEDIUM 🟡"
        color = "orange"
    else:
        strength = "STRONG 🟢"
        color = "green"

    result_label.config(
        text=f"Password Strength: {strength}\nSecurity Score: {score}/4",
        fg=color
    )

# Main Window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#1e1e2f")

title = tk.Label(
    root,
    text="🔐 Password Strength Checker",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="white"
)
title.pack(pady=20)

entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 14),
    show="*"
)
entry.pack(pady=10)

check_btn = tk.Button(
    root,
    text="Check Strength",
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    command=check_password
)
check_btn.pack(pady=15)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=20)

footer = tk.Label(
    root,
    text="Cyber Security Internship Project",
    bg="#1e1e2f",
    fg="lightgray"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
