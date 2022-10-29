import tkinter as tk
from functools import partial
from tkinter import messagebox

# Feedback form for the user to fill in name, surname, email, feedback
def create_from():
    # Create a window
    window = tk.Tk()
    window.title("Feedback Form")
    window.geometry("500x500")

    # Create a label for the name
    name_label = tk.Label(window, text="Name")
    name_label.place(x=10, y=10)

    # Create a text box for the name
    name_text = tk.Entry(window)
    name_text.place(x=10, y=30)

    # Create a label for the surname
    surname_label = tk.Label(window, text="Surname")
    surname_label.place(x=10, y=60)

    # Create a text box for the surname
    surname_text = tk.Entry(window)
    surname_text.place(x=10, y=80)

    # Create a label for the email
    email_label = tk.Label(window, text="Email")
    email_label.place(x=10, y=110)

    # Create a text box for the email
    email_text = tk.Entry(window)
    email_text.place(x=10, y=130)

    # Create a label for the feedback
    feedback_label = tk.Label(window, text="Feedback")
    feedback_label.place(x=10, y=160)

    # Create a text box for the feedback
    feedback_text = tk.Text(window, height=10, width=50)
    feedback_text.place(x=10, y=180)

    # Create a button to submit the feedback
    submit_button = tk.Button(window, text="Submit", command=partial(submit, name_text, surname_text, email_text, feedback_text))
    submit_button.place(x=10, y=400)

    # Create a button to clear the feedback
    clear_button = tk.Button(window, text="Clear", command=partial(clear, name_text, surname_text, email_text, feedback_text))
    clear_button.place(x=100, y=400)

    # Create a button to exit the feedback
    exit_button = tk.Button(window, text="Exit", command=partial(exit, window))
    exit_button.place(x=200, y=400)

    # Create a button to login as admin
    admin_button = tk.Button(window, text="Admin Login", command=admin_login)
    admin_button.place(x=300, y=400)

    # Start the window
    window.mainloop()

# Submit the feedback
def submit(name_text, surname_text, email_text, feedback_text):
    # Get the name, surname, email and feedback
    name = name_text.get()
    surname = surname_text.get()
    email = email_text.get()
    feedback = feedback_text.get("1.0", "end-1c")

    # Check if the name, surname, email and feedback are not empty
    if name != "" and surname != "" and email != "" and feedback != "":
        # Check if the email is valid
        if validate_email(email):
            # Submit the feedback
            submit_feedback(name, surname, email, feedback)
            # Show a message box
            messagebox.showinfo("Success", "Feedback submitted successfully")
        else:
            # Show a message box
            messagebox.showerror("Error", "Invalid email")
    else:
        # Show a message box
        messagebox.showerror("Error", "Please fill in all the fields")
        
# Clear the feedback
def clear(name_text, surname_text, email_text, feedback_text):
    # Clear the name, surname, email and feedback
    name_text.delete(0, "end")
    surname_text.delete(0, "end")
    email_text.delete(0, "end")
    feedback_text.delete("1.0", "end")

# Exit the feedback
def exit(window):
    # Exit the window
    window.destroy()


import controllers.controller as controller
def submit_feedback(name, surname, email, feedback):
    controller.submit_feedback(name, surname, email, feedback)


# Validate the email
def validate_email(email):
    # Check if the email is valid
    if "@" in email and "." in email:
        return True
    else:
        return False
    

# admin login button
import views.adminpage as adminpage
def admin_login():
    import views.adminpage as adminpage
    adminpage.admin_login()