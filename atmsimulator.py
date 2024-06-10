import tkinter as tk
from tkinter import messagebox

class ATM:
    def __init__(self, master):
        self.master = master
        self.master.title("ATM Simulator")
        self.balance = 1000  # Initial balance
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Welcome to ATM Simulator", font=("Helvetica", 16)).grid(row=0, columnspan=2)

        tk.Label(self.master, text="Current Balance:").grid(row=1, column=0, sticky=tk.E)
        self.balance_label = tk.Label(self.master, text="${}".format(self.balance))
        self.balance_label.grid(row=1, column=1, sticky=tk.W)

        tk.Label(self.master, text="Amount:").grid(row=2, column=0, sticky=tk.E)
        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.grid(row=2, column=1, sticky=tk.W)

        tk.Button(self.master, text="Check Balance", command=self.check_balance).grid(row=3, columnspan=2, pady=5)
        tk.Button(self.master, text="Deposit", command=self.deposit).grid(row=4, columnspan=2, pady=5)
        tk.Button(self.master, text="Withdraw", command=self.withdraw).grid(row=5, columnspan=2, pady=5)

    def check_balance(self):
        messagebox.showinfo("Balance", "Your balance is ${}".format(self.balance))

    def deposit(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            self.balance += amount
            self.update_balance_display()
            messagebox.showinfo("Deposit", "Deposit successful. New balance is ${}".format(self.balance))
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")

    def withdraw(self):
        try:
            amount = float(self.amount_entry.get())
            if amount <= 0:
                raise ValueError
            if amount > self.balance:
                raise Exception("Insufficient funds")
            self.balance -= amount
            self.update_balance_display()
            messagebox.showinfo("Withdraw", "Withdrawal successful. New balance is ${}".format(self.balance))
        except ValueError:
            messagebox.showerror("Error", "Invalid amount")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def update_balance_display(self):
        self.balance_label.config(text="${}".format(self.balance))

def main():
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()

if __name__ == "__main__":
    main()
