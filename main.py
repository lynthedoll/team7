import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from PIL import Image, ImageTk

class Student:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Teacher:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bison Advisor - Login")

        # Howard University header
        header_label = tk.Label(root, text="Howard University", font=("Helvetica", 16))
        header_label.pack(pady=(10, 0))  # Add padding at the top

        # Social media icon frame
        social_frame = tk.Frame(self.root)
        social_frame.pack(pady=10)

        # Load and resize images for social media icons
        twitter_image = Image.open("twitter.jpeg").resize((32, 32), Image.LANCZOS)
        facebook_image = Image.open("facebook.jpeg").resize((32, 32), Image.LANCZOS)
        linkedin_image = Image.open("linkedin.png").resize((32, 32), Image.LANCZOS)

        self.twitter_photo = ImageTk.PhotoImage(twitter_image)
        self.facebook_photo = ImageTk.PhotoImage(facebook_image)
        self.linkedin_photo = ImageTk.PhotoImage(linkedin_image)

        # Buttons for social media icons
        tk.Button(social_frame, image=self.twitter_photo, borderwidth=0).pack(side=tk.LEFT, padx=2)
        tk.Button(social_frame, image=self.facebook_photo, borderwidth=0).pack(side=tk.LEFT, padx=2)
        tk.Button(social_frame, image=self.linkedin_photo, borderwidth=0).pack(side=tk.LEFT, padx=2)

        # Title Label
        title_label = tk.Label(self.root, text="Bison Advisor", font=("Helvetica", 20))
        title_label.pack(pady=(0, 20))  # Reduce padding at the bottom

        # Entry fields frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=5)

        # Create labels and entry widgets for username and password
        tk.Label(entry_frame, text="User name").grid(row=0, column=0, pady=5)
        self.username_entry = tk.Entry(entry_frame)
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(entry_frame, text="Password").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(entry_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5, padx=5)

        # Help link
        help_link = tk.Label(self.root, text="Need help logging in?", fg="blue", cursor="hand2")
        help_link.pack()

        # Create login button
        login_button = tk.Button(self.root, text="SIGN IN", command=self.login)
        login_button.pack(pady=20)

        # Bind the help link
        help_link.bind("<Button-1>", lambda e: messagebox.showinfo("Help", "Help instructions go here."))
