import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
from countrieslist import countries
from countrieslist import values

# Establish database connection
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Iamgwapo234',
    database='sql_biodata'  
)

cursor = conn.cursor()
create_table_query = """
                        CREATE TABLE IF NOT EXISTS biodata (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            last_name VARCHAR(255),
                            first_name VARCHAR(255),
                            middle_name VARCHAR(255),
                            sex VARCHAR(10),
                            address VARCHAR(255),
                            email VARCHAR(255),
                            phone VARCHAR(15),
                            country VARCHAR(255)
                        );
                        """


cursor.execute(create_table_query)
conn.commit()

# Data for database
def insert_data():
    last_name = last_name_entry.get()
    first_name = first_name_entry.get()
    middle_name = middle_name_entry.get()
    sex = sex_var.get()
    address = address_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    country = countries_var.get()

    insert_query = """
    INSERT INTO biodata (last_name, first_name, middle_name, sex, address, email, phone, country)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (last_name, first_name, middle_name, sex, address, email, phone, country)
    cursor.execute(insert_query, values)
    conn.commit()

    # Clear the input fields after insertion
    last_name_entry.delete(0, 'end')
    first_name_entry.delete(0, 'end')
    middle_name_entry.delete(0, 'end')
    address_entry.delete(0, 'end')
    email_entry.delete(0, 'end')
    phone_entry.delete(0, 'end')

# Main Window
window = tk.Tk()
window.title("Biodata Recorder")

# Canvas
canvas = Canvas(window, width=1000, height=750, bg="SpringGreen2")
canvas.pack()
canvas.create_rectangle(20, 20, 980, 730, fill="white")
canvas.create_text(500, 100, text="Biodata Compiler", fill="black", font=('Helvetica 60 bold'))

# Frame
frame = tk.Frame(window, bg="white")
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
canvas.create_rectangle(20, 20, 980, 730, fill="white")
canvas.create_text(500, 100, text="Biodata Compiler", fill="black", font=('Helvetica 60 bold'))

# Last Name
last_name_label = tk.Label(frame, text="Last Name:", font=('Helvetica 15 bold'), bg="white")
last_name_label.grid(row=0, column=0, sticky=tk.W, padx=5)
last_name_entry = tk.Entry(frame, width=30)
last_name_entry.grid(row=0, column=1, padx=5, pady=5)

# First Name
first_name_label = tk.Label(frame, text="First Name:", font=('Helvetica 15 bold'))
first_name_label.grid(row=0, column=2, sticky=tk.W, padx=5)
first_name_entry = tk.Entry(frame, width=30)
first_name_entry.grid(row=0, column=3, padx=5, pady=5)

# Middle Name
middle_name_label = tk.Label(frame, text="Middle Name:", font=('Helvetica 15 bold'))
middle_name_label.grid(row=0, column=4, sticky=tk.W, padx=5)
middle_name_entry = tk.Entry(frame, width=30)
middle_name_entry.grid(row=0, column=5, padx=5, pady=5)

# Sex
options = ["Male", "Female"]
sex_label = tk.Label(frame, text="Sex:", font=('Helvetica 15 bold'))
sex_label.grid(row=3, column=0, sticky=tk.W, padx=5)
sex_var = tk.StringVar(frame)
sex_dropdown = tk.OptionMenu(frame, sex_var, *options)
sex_dropdown.grid(row=3, column=1, padx=5, pady=5)

# Address
address_label = tk.Label(frame, text="Address:", font=('Helvetica 15 bold'))
address_label.grid(row=4, column=0, sticky=tk.W, padx=5)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=4, column=1, padx=5, pady=5)

# Email Address
email_label = tk.Label(frame, text="Email Address:", font=('Helvetica 15 bold'))
email_label.grid(row=5, column=0, sticky=tk.W, padx=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=5, column=1, padx=5, pady=5)

# Phone
phone_label = tk.Label(frame, text="Phone:", font=('Helvetica 15 bold'))
phone_label.grid(row=6, column=0, sticky=tk.W, padx=5)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=6, column=1, padx=5, pady=5)

# Countries
countries_label = tk.Label(frame, text="Country:", font=('Helvetica 15 bold'))
countries_label.grid(row=7, column=0, sticky=tk.W, padx=5)
countries_var = tk.StringVar(frame)
countries_dropdown = tk.OptionMenu(frame, countries_var, *countries)
countries_dropdown.grid(row=7, column=1, padx=5, pady=5)

# Submit Button
submit_button = tk.Button(frame, text="Submit", command=insert_data)
submit_button.grid(row=8, column=0, columnspan=2, padx=5, pady=10)


# Start the main loop
window.mainloop()



