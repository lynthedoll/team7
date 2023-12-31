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
        
    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()
    
        # Validate credentials (dummy data for demonstration purposes)
        student = Student("student123", "password123")
        teacher = Teacher("teacher456", "password456")
    
        if username == student.username and password == student.password:
            messagebox.showinfo("Success", "Student login successful!")
            self.root.destroy()  # Close the login window
            StudentApp(tk.Tk())  # Open the student app window
    
        elif username == teacher.username and password == teacher.password:
            messagebox.showinfo("Success", "Teacher login successful!")
            self.root.destroy()  # Close the login window
            TeacherDashboard(tk.Tk())  # Open the teacher app window
    
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bison Advisor - Student App")
    
        # Load and resize the user icon
        user_icon_image = Image.open("user icon.png").resize((32, 32), Image.LANCZOS)
        self.user_icon_photo = ImageTk.PhotoImage(user_icon_image)
    
        # Create a label to display the user icon in the top-right corner
        user_icon_label = tk.Label(root, image=self.user_icon_photo)
        user_icon_label.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)
    
        # Create student-specific UI elements here
        self.create_navigation_bar()
    
        # Create title at the top-middle-left of the page
        title_label = tk.Label(self.root, text="Bison Advisor", font=("Helvetica", 24, "bold"))
        title_label.place(relx=0.5, rely=0, anchor="n")
    
        # Create logout button in the top right corner
        logout_button = tk.Button(root, text="Logout", command=self.logout)
        logout_button.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)
    
        # Load and resize the image
        profile_image = Image.open("user icon.png").resize((100, 100), Image.LANCZOS)
        self.profile_photo = ImageTk.PhotoImage(profile_image)
    
        canvas = tk.Canvas(root, width=100, height=100)
        canvas.create_image(0, 0, anchor=tk.NE, image=self.profile_photo)
        canvas.pack(side=tk.TOP, anchor=tk.NE, padx=10, pady=10)
    
         # Create "Upcoming Events" table
        events_label = tk.Label(root, text="Upcoming Events", font=("Helvetica", 12, "underline"))
        events_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)  # Centered and raised higher
    
        # Fake data for events
        events_data = [
            {"event": "Event 1", "date": "2023-12-15"},
            {"event": "Event 2", "date": "2023-12-20"},
             {"event": "Event 3", "date": "2023-12-25"},
            {"event": "Event 4", "date": "2023-12-30"},
            ]
    
        # Create a table-like layout for events
        table_frame = tk.Frame(root)
        table_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Centered
    
        for event in events_data:
            event_frame = tk.Frame(table_frame, borderwidth=2, relief="solid")
            event_frame.pack(side=tk.LEFT, padx=10, pady=10)
    
            event_name_label = tk.Label(event_frame, text=event["event"], font=("Helvetica", 9))
            event_name_label.pack()
    
            event_date_label = tk.Label(event_frame, text=event["date"], font=("Helvetica", 9))
            event_date_label.pack()
    def create_bottom_navigation_bar(self):
        # Bottom navigation bar frame
        bottom_nav_frame = tk.Frame(self.root)
        bottom_nav_frame.pack(side=tk.RIGHT, anchor=tk.SE, fill=tk.Y, padx=10, pady=10)

        # Add buttons for Courses, Students, Paid Courses, Duties, and Notifications
        tk.Button(bottom_nav_frame, text="Courses", command=self.courses).pack(pady=5, anchor="e", fill=tk.X)
        tk.Button(bottom_nav_frame, text="Students", command=self.students).pack(pady=5, anchor="e", fill=tk.X)
        tk.Button(bottom_nav_frame, text="Paid Courses", command=self.paid_courses).pack(pady=5, anchor="e", fill=tk.X)
        tk.Button(bottom_nav_frame, text="Duties", command=self.duties).pack(pady=5, anchor="e", fill=tk.X)
        tk.Button(bottom_nav_frame, text="Notifications", command=self.notifications).pack(pady=5, anchor="e", fill=tk.X)

    def create_navigation_bar(self):
        # Navigation bar frame
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)

        # Add buttons for Home, Advisor, Resources, Student Services, Major Explorer, and Settings
        tk.Button(nav_frame, text="Home", command=self.go_home).pack(pady=10, anchor="w", fill=tk.X)
        tk.Button(nav_frame, text="Advisor", command=self.advisor).pack(pady=10, anchor="w", fill=tk.X)
        tk.Button(nav_frame, text="Resources", command=self.resources).pack(pady=10, anchor="w", fill=tk.X)
        tk.Button(nav_frame, text="Student Services", command=self.student_services).pack(pady=10, anchor="w", fill=tk.X)
        tk.Button(nav_frame, text="Major Explorer", command=self.major_explorer).pack(pady=10, anchor="w", fill=tk.X)
        tk.Button(nav_frame, text="Settings", command=self.settings).pack(pady=10, anchor="w", fill=tk.X)

    def go_home(self):
        # Add functionality for the Home button
        messagebox.showinfo("Home", "Welcome to the Home page!")

    def advisor(self):
        # Add functionality for the Advisor button
        messagebox.showinfo("Advisor", "Advisor page")

    def resources(self):
        # Add functionality for the Resources button
        messagebox.showinfo("Resources", "Resources page")

    def student_services(self):
        # Add functionality for the Student Services button
        messagebox.showinfo("Student Services", "Student Services page")

    def major_explorer(self):
        # Add functionality for the Major Explorer button
        messagebox.showinfo("Major Explorer", "Major Explorer page")

    def settings(self):
        # Add functionality for the Settings button
        messagebox.showinfo("Settings", "Settings page")

    def logout(self):
        self.root.destroy()  # Close the student app window
        LoginApp(tk.Tk())   # Open the login window

    def courses(self):
        messagebox.showinfo("Courses", "Courses page")

    def students(self):
        messagebox.showinfo("Students", "Students page")

    def paid_courses(self):
        messagebox.showinfo("Paid Courses", "Paid Courses page")

    def duties(self):
        messagebox.showinfo("Duties", "Duties page")

    def notifications(self):
        messagebox.showinfo("Notifications", "Notifications page")
        
class TeacherDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Welcome to your Teacher Dashboard!")

        self.create_menu()
        self.create_tabs()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # Notifications menu
        notification_menu = tk.Menu(menu_bar, tearoff=0)
        notification_menu.add_command(label="Inbox", command=self.notification_page)
        notification_menu.add_command(label="Notifications Page", command=self.notification_page)
        menu_bar.add_cascade(label="Notifications", menu=notification_menu)

        # Settings menu
        settings_menu = tk.Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Update Information", command=self.update_info)
        settings_menu.add_command(label="Change Language", command=self.change_language)
        settings_menu.add_command(label="Change Password", command=self.change_password)
        settings_menu.add_command(label="Enable 2FA", command=self.enable_2fa)
        settings_menu.add_command(label="Logout", command=self.logout)
        menu_bar.add_cascade(label="Settings", menu=settings_menu)

        self.root.config(menu=menu_bar)

    def create_tabs(self):
        tab_control = ttk.Notebook(self.root)

        # Home Tab
        home_tab = ttk.Frame(tab_control)
        tab_control.add(home_tab, text="Home")
        # Add Home components here
        home_tab_dropdown = tk.Label(home_tab, text="Upcoming Events:\n\n December 18, 2023 - January 1, 2024\n Winter Recess \n\n January 8, 2024\n -- First Day of Classes --\n\n January 15, 2024\n University Closed: MLK Day\n\n January 19, 2024\n -- Last Day to Register --")
        home_tab_dropdown.pack(side="bottom",pady=10)
        home_tab_dropdown = tk.Label(home_tab, text="Calendar")
        home_tab_dropdown.pack(pady=10)
        home_tab_dropdown = tk.Button(home_tab, text="Monthly View")
        home_tab_dropdown.pack(pady=10)
        home_tab_dropdown = tk.Button(home_tab, text="Weekly View")
        home_tab_dropdown.pack(pady=10)
        home_tab_dropdown = tk.Button(home_tab, text="Daily View")
        home_tab_dropdown.pack(pady=10)

        # Students Tab
        advise_student_tab = ttk.Frame(tab_control)
        tab_control.add(advise_student_tab, text="Students")
        # Add your Student components here
        student_tab_dropdown = tk.Button(advise_student_tab, text="Student Selection Page")
        student_tab_dropdown.pack(pady=10)
        student_tab_dropdown = tk.Button(advise_student_tab, text="Student Academic Profile")
        student_tab_dropdown.pack(pady=10)

        # Forms and Approvals Tab
        forms_approvals_tab = ttk.Frame(tab_control)
        tab_control.add(forms_approvals_tab, text="Forms and Approvals")
        # Add your Forms and Approvals components here
        form_tab_dropdown = tk.Button(forms_approvals_tab, text="PDF Selection Page")
        form_tab_dropdown.pack(pady=10)

        tab_control.pack(expand=1, fill="both")

    def notification_page(self):
    # Add logic to change the language
        pass

    def update_info(self):
        # Add logic to change the language
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=5)
        # Update Name
        tk.Label(entry_frame, text="Full name").grid(row=0, column=0, pady=5)
        self.username_entry = tk.Entry(entry_frame)
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)
        # Update Department
        tk.Label(entry_frame, text="Department").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(entry_frame)
        self.password_entry.grid(row=1, column=1, pady=5, padx=5)

        # Create Update button
        login_button = tk.Button(self.root, text="UPDATE INFO", command=self.login)
        login_button.pack(pady=20)

        login_button.bind("<Button-1>", lambda e:
        messagebox.showinfo("Success", "Information updated successfully!"))

    def change_language(self):
        # Add logic to change the language
        lang_label = tk.Label(self.root, text="-- CHANGE LANGUAGE --")
        lang_label.pack(pady=10)
        english_button = tk.Button(self.root, text="ENGLISH", command=self.login)
        english_button.pack(pady=20)
        spanish_button = tk.Button(self.root, text="SPANISH", command=self.login)
        spanish_button.pack(pady=20)
        arabic_button = tk.Button(self.root, text="ARABIC", command=self.login)
        arabic_button.pack(pady=20)
        pass

    def change_password(self):
        # Add logic to change the password
        # Entry fields frame
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=5)

        # Create labels and entry widgets for old and new  passwords
        tk.Label(entry_frame, text="Old Password").grid(row=0, column=0, pady=5)
        self.username_entry = tk.Entry(entry_frame, show="*")
        self.username_entry.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(entry_frame, text="New Password").grid(row=1, column=0, pady=5)
        self.password_entry = tk.Entry(entry_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5, padx=5)

        # Help link
        help_link = tk.Label(self.root, text="Need help?", fg="blue", cursor="hand2")
        help_link.pack()

        # Create Change Password button
        login_button = tk.Button(self.root, text="CHANGE PASSWORD", command=self.login)
        login_button.pack(pady=20)

        # Bind the help link
        help_link.bind("<Button-1>", lambda e: messagebox.showinfo("Help", "Password Should include: Uppercase, Lowercase, Numbers, Special Characters"))

        # Bind the Change password button
        login_button.bind("<Button-1>", lambda e:
        messagebox.showinfo("Success", "Password updated successfully!"))
        pass

    def enable_2fa(self):
        # Add logic to enable 2-factor authentication
        pass

    def logout(self):
        self.root.destroy()  # Close the student app window

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
# ///////////////////
