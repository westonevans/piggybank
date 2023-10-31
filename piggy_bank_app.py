import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def update_balance():
    try:
        deposit_amount = float(deposit_entry.get())
        current_balance = float(balance_label.cget("text")[10:])  # Extract the balance value
        new_balance = current_balance + deposit_amount
        balance_label.config(text=f"Balance: ${new_balance:.2f}")
        
        # Record the transaction
        transaction_history.append(f"Deposit: +${deposit_amount:.2f}")
        
        # Update the transaction list
        update_transaction_history()

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount.")

def set_goal():
    try:
        goal_amount = float(goal_entry.get())
        goal_label.config(text=f"Savings Goal: ${goal_amount:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid amount for the goal.")

def update_transaction_history():
    transaction_text.config(state="normal")
    transaction_text.delete(1.0, "end")  # Clear existing content
    for transaction in transaction_history:
        transaction_text.insert("end", transaction + "\n")
    transaction_text.config(state="disabled")

# Create the main window
root = tk.Tk()
root.title("My First Piggy Bank")

# Load and display a piggy bank image at the top
piggy_bank_image = Image.open("pgbnkpic.png")  # Replace with your image file
piggy_bank_photo = ImageTk.PhotoImage(piggy_bank_image)
piggy_bank_label = tk.Label(root, image=piggy_bank_photo)
piggy_bank_label.image = piggy_bank_photo
piggy_bank_label.pack()

# Create a frame for better organization
frame = tk.Frame(root)
frame.pack(pady=10)

# Balance label
balance_label = tk.Label(frame, text="Balance: $0.00", font=("Arial", 14))
balance_label.grid(row=0, column=0, padx=10)

# Deposit entry
deposit_label = tk.Label(frame, text="Deposit Amount:", font=("Arial", 12))
deposit_label.grid(row=1, column=0, padx=10, pady=5)
deposit_entry = tk.Entry(frame, font=("Arial", 12))
deposit_entry.grid(row=1, column=1, padx=10, pady=5)
deposit_button = tk.Button(frame, text="Deposit", command=update_balance, font=("Arial", 12), bg="green", fg="white")
deposit_button.grid(row=1, column=2, padx=10)

# Savings Goal
goal_label = tk.Label(frame, text="Savings Goal: $0.00", font=("Arial", 12))
goal_label.grid(row=2, column=0, padx=10)
goal_entry = tk.Entry(frame, font=("Arial", 12))
goal_entry.grid(row=2, column=1, padx=10, pady=5)
set_goal_button = tk.Button(frame, text="Set Goal", command=set_goal, font=("Arial", 12), bg="blue", fg="white")
set_goal_button.grid(row=2, column=2, padx=10)

# Transaction History
transaction_history = []
transaction_label = tk.Label(root, text="Transaction History:", font=("Arial", 12))
transaction_label.pack()
transaction_text = tk.Text(root, width=30, height=10, state="disabled")
transaction_text.pack()

# Tip message
tip_message = tk.Label(root, text="Tip: Encourage your child to save a portion of their allowance.", font=("Arial", 10))
tip_message.pack(pady=5)

# Run the main loop
root.mainloop()
