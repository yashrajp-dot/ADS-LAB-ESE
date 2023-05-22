from tkinter import *
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="user3",
    password="user",
    database="db"
)

# Create a cursor
cursor = db.cursor()

# Create the main application window
window = Tk()

# Create form labels
label_name = Label(window, text="Name:")
label_name.grid(row=0, column=0)
label_age = Label(window, text="Age:")
label_age.grid(row=1, column=0)

# Create form entry fields
entry_name = Entry(window)
entry_name.grid(row=0, column=1)
entry_age = Entry(window)
entry_age.grid(row=1, column=1)

# Create CRUD functions
def create():
    name = entry_name.get()
    age = entry_age.get()
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    values = (name, age)
    cursor.execute(query, values)
    db.commit()
    entry_name.delete(0, END)
    entry_age.delete(0, END)

def read():
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")

def update():
    name = entry_name.get()
    age = entry_age.get()
    query = "UPDATE users SET age = %s WHERE name = %s"
    values = (id, name)
    cursor.execute(query, values)
    db.commit()
    entry_name.delete(0, END)
    entry_age.delete(0, END)

def delete():
    name = entry_name.get()
    query = "DELETE FROM users WHERE name = %s"
    values = (name,)
    cursor.execute(query, values)
    db.commit()
    entry_name.delete(0, END)
    entry_age.delete(0, END)

# Create buttons for CRUD operations
button_create = Button(window, text="Create", command=create)
button_create.grid(row=2, column=0)
button_read = Button(window, text="Read", command=read)
button_read.grid(row=2, column=1)
button_update = Button(window, text="Update", command=update)
button_update.grid(row=2, column=2)
button_delete = Button(window, text="Delete", command=delete)
button_delete.grid(row=2, column=3)

# Start the Tkinter event loop
window.mainloop()

# Close the database connection
cursor.close()
db.close()
