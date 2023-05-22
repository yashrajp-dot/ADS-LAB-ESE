

from tkinter import *
from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['localhost'])
session = cluster.connect('demo2')

# Define the GUI
root = Tk()
root.title("Cassandra GUI")
root.geometry("800x200")
root.configure(bg='#D4EFFC')

# Define the functions for CRUD operations
def create():
    name = name_entry.get()
    email = email_entry.get()
    id = int(id_entry.get())
    session.execute("INSERT INTO demo2.users (id, email, name) VALUES (%s, %s, %s)", (id, email, name))

def read():
    result = session.execute("SELECT * FROM demo2.users")
    for row in result:
        print(row.name, row.email)

def update():
    name = name_entry.get()
    email = email_entry.get()
    session.execute("UPDATE demo2.users SET email = %s WHERE name = %s", (email, name))

def delete():
    name = name_entry.get()
    session.execute("DELETE FROM demo2.users WHERE name = %s", [name])

# Define the labels and input fields
name_label = Label(root, text="Name:", bg='#D4EFFC')
name_label.grid(row=0, column=0, padx=10, pady=10)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

email_label = Label(root, text="Email:", bg='#D4EFFC')
email_label.grid(row=1, column=0, padx=10, pady=10)
email_entry = Entry(root)
email_entry.grid(row=1, column=1, padx=10, pady=10)

id_label = Label(root, text="ID:", bg='#D4EFFC')
id_label.grid(row=2, column=0, padx=10, pady=10)
id_entry = Entry(root)
id_entry.grid(row=2, column=1, padx=10, pady=10)

# Define the buttons for CRUD operations
create_button = Button(root, text="Create", command=create, bg='#4CAF50', fg='white', width=10)
create_button.grid(row=3, column=0, padx=10, pady=10)

read_button = Button(root, text="Read", command=read, bg='#2196F3', fg='white', width=10)
read_button.grid(row=3, column=1, padx=10, pady=10)

update_button = Button(root, text="Update", command=update, bg='#FFC107', fg='white', width=10)
update_button.grid(row=4, column=0, padx=10, pady=10)

delete_button = Button(root, text="Delete", command=delete, bg='#FF5733', fg='white', width=10)
delete_button.grid(row=4, column=1, padx=10, pady=10)

# Run the GUI
root.mainloop()
