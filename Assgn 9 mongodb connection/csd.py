from tkinter import *
from cassandra.cluster import Cluster

# Connect to the Cassandra cluster
cluster = Cluster(['localhost'])
session = cluster.connect('demo2')

# Define the GUI
root = Tk()
root.title("Cassandra GUI")
root.geometry("400x200")

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
name_label = Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = Entry(root)
name_entry.grid(row=0, column=1)

email_label = Label(root, text="Email:")
email_label.grid(row=1, column=0)
email_entry = Entry(root)
email_entry.grid(row=1, column=1)

id_label = Label(root, text="ID:")
id_label.grid(row=2, column=0)
id_entry = Entry(root)
id_entry.grid(row=2, column=1)

# Define the buttons for CRUD operations
create_button = Button(root, text="Create", command=create)
create_button.grid(row=3, column=0)

read_button = Button(root, text="Read", command=read)
read_button.grid(row=3, column=1)

update_button = Button(root, text="Update", command=update)
update_button.grid(row=4, column=0)

delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=4, column=1)

# Run the GUI
root.mainloop()