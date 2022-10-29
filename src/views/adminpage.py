# admin page
import tkinter as tk
from functools import partial
from tkinter import messagebox
from tkinter.tix import Tree
from tkinter.ttk import Treeview
from xml.etree.ElementTree import TreeBuilder
import models.database as database
from views.feedbackfrom import submit


def adminpage():
    # Show the all the feedbacks in the database in a table format
    def show_feedbacks():
        # Get the feedbacks from the database
        feedbacks = database.get_all_data()
        # Create the treeview to show the feedbacks in a table format
        tree = Treeview(window, columns=("id", "name", "surname", "email", "feedback", "rfid", "status"))
        # Set the headings of the columns
        tree.heading("#0", text="ID")
        tree.heading("#1", text="Name")
        tree.heading("#2", text="Surname")
        tree.heading("#3", text="Email")
        tree.heading("#4", text="Feedback")
        tree.heading("#5", text="RFID")
        tree.heading("#6", text="Status")
        # Set the column width
        tree.column("#0", width=50)
        tree.column("#1", width=100)
        tree.column("#2", width=100)
        tree.column("#3", width=100)
        tree.column("#4", width=100)
        tree.column("#5", width=100)
        tree.column("#6", width=100)
        # Set the treeview
        tree.place(x=50, y=100)
        # Insert the feedbacks into the treeview
        for feedback in feedbacks:
            tree.insert("", tk.END, text=feedback[0], values=(feedback[1], feedback[2], feedback[3], feedback[4], feedback[5], feedback[6]))

    # Create the window
    window = tk.Tk()
    # Set the title
    window.title("Admin Page")
    # Set the size
    window.geometry("800x600")
    # Set the background color
    window.config(bg="#ffffff")
    # Create the label
    label = tk.Label(window, text="Admin Page", font=("Arial", 20))
    # Set the label
    label.place(x=350, y=50)
    # Create the show feedbacks button
    show_feedbacks_button = tk.Button(window, text="Show Feedbacks", font=("Arial", 15), command=show_feedbacks)
    # Set the show feedbacks button
    show_feedbacks_button.place(x=50, y=50)
    # Create the exit button
    exit_button = tk.Button(window, text="Exit", font=("Arial", 15), command=partial(exit, window))
    # Set the exit button
    exit_button.place(x=700, y=550)
    # Start the window

    # Change the status of the feedback button
    change_status_button = tk.Button(window, text="Change Status", font=("Arial", 15), command=partial(change_status, tree))
    # Set the change status button
    change_status_button.place(x=600, y=550)
    # Start the window

    window.mainloop()

    # Change the status of the feedback to closed
    def close_feedback(id):
        # Change the status of the feedback
        change_feedback_status("closed", id)
        # Show the message
        messagebox.showinfo("Success", "Feedback closed successfully")

    # Change the status of the feedback to escalated
    def escalate_feedback(id):
        # Change the status of the feedback
        change_feedback_status("escalated", id)
        # Show the message
        messagebox.showinfo("Success", "Feedback escalated successfully")
        




def change_status(tree):
    # Change the status of the feedback
    # Get the selected item
    selected_item = tree.selection()
    # Get the id of the selected item
    id = tree.item(selected_item, "text")
    # Change the status of the feedback
    database.update_status("read", id)
    # Show the message
    messagebox.showinfo("Success", "Status changed successfully")








def clear(name_text, surname_text, email_text, feedback_text):
    # Clear the name, surname, email and feedback
    name_text.delete(0, tk.END)
    surname_text.delete(0, tk.END)
    email_text.delete(0, tk.END)
    feedback_text.delete(1.0, tk.END)

# Exit the feedback


def exit(window):
    # Exit the window
    window.destroy()

# login access for admin
def admin_login():
    # Create the window
    window = tk.Tk()
    # Set the title
    window.title("Admin Login")
    # Set the size
    window.geometry("500x500")
    # Set the background color
    window.config(bg="#ffffff")
    # Create the label
    label = tk.Label(window, text="Admin Login", font=("Arial", 20))
    # Set the label
    label.place(x=200, y=50)
    # Create the username label
    username_label = tk.Label(window, text="Username", font=("Arial", 15))
    # Set the username label
    username_label.place(x=100, y=150)
    # Create the username entry
    username_entry = tk.Entry(window, width=30)
    # Set the username entry
    username_entry.place(x=200, y=150)
    # Create the password label
    password_label = tk.Label(window, text="Password", font=("Arial", 15))
    # Set the password label
    password_label.place(x=100, y=200)
    # Create the password entry
    password_entry = tk.Entry(window, width=30)
    # Set the password entry
    password_entry.place(x=200, y=200)
    # Create the login button
    login_button = tk.Button(window, text="Login", font=("Arial", 15), command=partial(login, username_entry, password_entry, window))
    # Set the login button
    login_button.place(x=200, y=300)
    # Start the window
    window.mainloop()

# Login to the admin page
def login(username_entry, password_entry, window):
    # Get the username and password
    username = username_entry.get()
    password = password_entry.get()
    # Check if the username and password are correct
    if username == "admin" and password == "admin":
        # Destroy the window
        window.destroy()
        adminpage()




def change_feedback_status(status, id):
    # Change the status of the feedback
    database.update_status(status, id)
