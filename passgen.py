import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x250")

        self.create_widgets()

    def create_widgets(self):
        self.length_label = tk.Label(self.master, text="Password Length:", font=('Arial', 12))
        self.length_label.pack(pady=10)

        self.length_entry = tk.Entry(self.master, width=10)
        self.length_entry.pack(pady=5)

        self.generate_button = tk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.master, text="", font=('Arial', 12), wraplength=300)
        self.password_label.pack(pady=10)

        self.copy_button = tk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
        except ValueError as e:
            self.password_label.config(text=f"Error: {e}")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        self.password_label.config(text=f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        if password:
            self.master.clipboard_clear()
            self.master.clipboard_append(password)
            tk.messagebox.showinfo("Success", "Password copied to clipboard!")
        else:
            tk.messagebox.showwarning("Error", "No password to copy!")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
