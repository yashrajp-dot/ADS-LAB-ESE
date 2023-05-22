from tkinter import *
import tkinter.messagebox as messagebox
import pymongo

#setting up the connection database and collections

global url 
# url = "mongodb://localhost:27017/"
url = "mongodb+srv://yashraj:yashraj>@cluster0.c13bbvn.mongodb.net/"
db = pymongo.MongoClient(url)
db_name = "db1"
crud_db = db[db_name]
collection_name="assignment9"
student = crud_db[collection_name]

 
def create():
    name = ename.get()
    prn = eprn.get()
    phone = ephone.get()
    if(name=="" or prn=="" or phone==""):
        messagebox.showinfo("Create","All fields are required")
    else:
        read = student.find_one({'prn':prn})
        if(read):
            messagebox.showinfo("Create","Student with this prn already present")
            ename.delete(0,END)
            eprn.delete(0,END)
            ephone.delete(0,END)
        else:
            data = {
                'name': name,
                'prn':prn,
                'phone':phone
            }
            student.insert_one(data)
            messagebox.showinfo("Create","Data Inserted successfully")
            ename.delete(0,END)
            eprn.delete(0,END)
            ephone.delete(0,END)

def reset():
    ename.delete(0,END)
    eprn.delete(0,END)
    ephone.delete(0,END)
def update():
    name = ename.get()
    prn = eprn.get()
    phone = ephone.get()
    if(name=="" or prn=="" or phone==""):
        messagebox.showinfo("Create","All fields are required")
    else:
        read = student.find_one({'prn':prn})
        if(read):
            current = student.find_one({'prn':prn})
            new={'$set':{'name':name,'phone':phone}}
            student.update_one(current,new)
            messagebox.showinfo("Create","Student Data Updated successfully")
            ename.delete(0,END)
            eprn.delete(0,END)
            ephone.delete(0,END)
        else:
            messagebox.showinfo("Update",f"NO student with {prn} exists")
            eprn.delete(0,END)

def read():
    data = student.find({})
    list_of_list = []
    name = []
    prn = []
    phone = []
    for i in data:
        name.append(i['name'])
        prn.append(i['prn'])
        phone.append(i['phone'])
    list_of_list.append(name)
    list_of_list.append(prn)
    list_of_list.append(phone)
    if(data):
        subwindow = Toplevel(root)
        subwindow.title("Student Data")
        subwindow.minsize(600,300)
        subwindow.geometry("600x300")
        rowtitle = ["name","prn","phone"]
        for k in range(3):
            e = Entry(subwindow,width=20)
            e.grid(row=0,column=k)
            e.insert(END,rowtitle[k])
        for i in range(3):
            for j in range(len(list_of_list[0])):
                e = Entry(subwindow,width=20)
                e.grid(row=j+1,column=i)
                e.insert(END,list_of_list[i][j])
    else:
        messagebox.showinfo("Read","No Student Data found")

def delete():
    prn = eprn.get()
    data = student.find_one({'prn':prn})
    if(prn=="" ):
        messagebox.showinfo("Delete","PRN field is compulsory ")
    else:
        if(data):
            data = student.delete_one({'prn':prn})
            messagebox.showinfo("Create","Student Deleted successfully")
            eprn.delete(0,END)
        else:
            messagebox.showinfo("Read","No Student Data found")

#GUI part

root = Tk()
root.minsize(600,300)
root.geometry('600x300')
root.title("CRUD Application")

#labels
name = Label(root,text="Enter Name : ",font=('bold',10))
name.place(x=20,y=40)
prn = Label(root,text="Enter PRN(eg.92): ",font=('bold',10))
prn.place(x=20,y=70)
phone = Label(root,text="Enter Phone : ",font=('bold',10))
phone.place(x=20,y=100)

#Entries
ename = Entry(root,width=60)
ename.place(x=150,y=40)
eprn = Entry(root,width=60)
eprn.place(x=150,y=70)
ephone = Entry(root,width=60)
ephone.place(x=150,y=100)

#buttons
create = Button(root,text="Create",font=('italic',12),bg='green',command=create)
create.place(x=40,y=150)
reset = Button(root,text="Reset",font=('italic',12),bg='yellow',command=reset)
reset.place(x=140,y=150)
update = Button(root,text="Update",font=('italic',12),bg='yellow',command=update)
update.place(x=240,y=150)
read = Button(root,text="Read",font=('italic',12),bg='white',command=read)
read.place(x=340,y=150)
delete = Button(root,text="Delete",font=('italic',12),bg='red',command=delete)
delete.place(x=440,y=150)

root.mainloop()


# from tkinter import *
# from tkinter import ttk
# from tkinter import simpledialog
# import tkinter, tkinter.messagebox
# from pymongo import MongoClient
# from pymongo.server_api import ServerApi
# from dotenv import load_dotenv
# import os

# # Loading the data from .env file
# load_dotenv()

# # Getting the .env variables
# MONGO_USER = "yashraj"
# MONGO_PASS = "yashraj"
# MONGO_DB_NAME = "db1"
# MONGO_COLLECTION = "assignment9"

# # Connecting to DB
# client = MongoClient(f"mongodb+srv://yashraj:yashraj@cluster0.c13bbvn.mongodb.net/test", server_api=ServerApi('1'))
# db = client[MONGO_DB_NAME] # Select DB
# collection = db[MONGO_COLLECTION] # Select collection

# # Initializing Window
# window = Tk()
# window.title("MongoDB Database Connectivity") # Title of window
# window.geometry('900x900') # Size of window (width X height)
# window.configure(background = "pink"); # Background color of window
# window.option_add("*Font", "Times 16") # Setting the font-family & font-size 

# usr_name = Label(window ,text = f"Connected to Cloud MongoDB as: Yashraj", background = "white").grid(row = 0, column = 1, pady=20)

# # CRUD Functions
# # 1. View
# def view_tb():
#     newWindow = Toplevel(window)
#     newWindow.title("VIEW Table")
#     newWindow.geometry('900x900')
#     newWindow.configure(background = "white"); # Background color of window
#     newWindow.option_add("*Font", "Times 20") # Setting the font-family & font-size
#     Label(newWindow ,text = f"Viewing Collection - Assignment09", background = "white").grid(row = 0, column = 0, padx=10, pady=10)

#     # Getting all column names from table
#     coll_keys = collection.find_one()
#     columns = [a for a in coll_keys]
#     tree = ttk.Treeview(newWindow, height=20, columns=columns, show='headings')
#     tree.grid(row=1, column=0, sticky='news', padx=10, pady=10)

#     # setup columns attributes
#     for col in columns:
#         tree.heading(col, text=col)
#         tree.column(col, width=100, anchor=tkinter.CENTER)

#     # populate data to treeview
#     all_data = collection.find({})
#     data_list = []
#     for a in all_data:
#         data_list.append(tuple(a.values()))
#     for d in data_list:
#         tree.insert('', 'end', value=d)

#     # scrollbar
#     sb = tkinter.Scrollbar(newWindow, orient=tkinter.VERTICAL, command=tree.yview)
#     sb.grid(row=1, column=1, sticky='ns', padx=0, pady=10)
#     tree.config(yscrollcommand=sb.set)

#     sbx = tkinter.Scrollbar(newWindow, orient=tkinter.HORIZONTAL, command=tree.xview)
#     sbx.grid(row=2, column=0, sticky='ew', padx=10, pady=0)
#     tree.config(xscrollcommand=sbx.set)

# # 2. Insert
# def insert_tb():
#     newWindow = Toplevel(window)
#     newWindow.title("INSERT into Table")
#     newWindow.geometry('900x900')
#     newWindow.configure(background = "white"); # Background color of window
#     newWindow.option_add("*Font", "Times 20") # Setting the font-family & font-size
    
#     Label(newWindow ,text = f"Insert values in collection: Assignment09", background = "white").grid(row = 0, column = 0, padx=10, pady=10)
    
#     # Getting columns names
#     coll_keys = collection.find_one()
#     columns = [a for a in coll_keys]
#     columns.pop(0) # Removing the _id field (entered automatically)
    
#     ent_ref = [] # For storing the Entry references
#     # Populating Labels and Entries
#     for ind, nm in enumerate(columns):
#         Label(newWindow ,text = nm, background = "white").grid(row = ind+1, column = 0, padx=10, pady=10)
#         ent = Entry(newWindow)
#         ent.grid(row = ind+1,column = 1)
#         ent_ref.append(ent)

#     def insert_val():
#         val = []
#         is_empty = False

#         # Getting value from each entry field
#         for r in ent_ref:
#             if len(r.get()) > 0:
#                 val.append(r.get())
#             else:
#                 tkinter.messagebox.showerror("ERROR", "All the fields are required!")
#                 is_empty = True
#                 break

#         # Checking if all fields are filled, before inserting
#         if not is_empty:
#             v = []
#             # Typecasting values (int, float & string)
#             for x in val:
#                 try:
#                     v.append(int(x))
#                 except ValueError:
#                     try: 
#                         v.append(float(x))
#                     except ValueError:
#                         v.append(x)

#             doc_obj = dict(zip(columns, v))

#             # Inserting values
#             try:
#                 collection.insert_one(doc_obj)
#                 for r in ent_ref:
#                     r.delete(0, END)
#                 tkinter.messagebox.showinfo("SUCCESS", "Values inserted into Collection successfully!")
#             except Exception as e:
#                 tkinter.messagebox.showerror("ERROR", e)

#     Button(newWindow, text="Insert Values", command=insert_val, background="green", foreground="white").grid(row = ind+2, column = 1, pady=20, sticky='ew')

# # 3. Update
# def update_tb():
#     try:
#         id = simpledialog.askinteger(title="UPDATE", prompt="Enter the PRN to be updated: ")

#         if id is not None:
#             query={"PRN":{"$eq":id}}
#             present_data = collection.find_one(query)
            
#             if present_data is None:
#                 tkinter.messagebox.showerror("ERROR", "No record was found with the given PRN !")
#             else:
#                 newWindow = Toplevel(window)
#                 newWindow.title("UPDATE Table")
#                 newWindow.geometry('900x900')
#                 newWindow.configure(background = "white"); # Background color of window
#                 newWindow.option_add("*Font", "Times 20") # Setting the font-family & font-size
                
#                 Label(newWindow ,text = f"Update values in collection: Assignment09", background = "white").grid(row = 0, column = 0, padx=10, pady=10)

#                 coll_keys = collection.find_one()
#                 columns = [a for a in coll_keys]
#                 columns.pop(0) # Removing the _id field (entered automatically)

#                 ent_ref = []

#                 val = []
#                 for k, v in present_data.items():
#                     val.append(str(v))

#                 val.pop(0) # Removing ObjectId

#                 for ind, nm in enumerate(columns):
#                     Label(newWindow ,text = nm, background = "white").grid(row = ind+1, column = 0, padx=10, pady=10)
#                     ent = Entry(newWindow)
#                     ent.grid(row = ind+1,column = 1)
#                     ent.insert(0, val[ind])
#                     ent_ref.append(ent)

#                 def update_val():
#                     upd_val = []
#                     is_empty = False

#                     for r in ent_ref:
#                         if len(r.get()) > 0:
#                             upd_val.append(r.get())
#                         else:
#                             tkinter.messagebox.showerror("ERROR", "All the fields are required!")
#                             is_empty = True
#                             break

#                     if not is_empty:
#                         v = []
#                         for x in upd_val:
#                             try:
#                                 v.append(int(x))
#                             except ValueError:
#                                 try: 
#                                     v.append(float(x))
#                                 except ValueError:
#                                     v.append(x)
                        
#                         try:
#                             doc_obj = dict(zip(columns, v))
#                             new_data = {"$set":doc_obj}
#                             collection.update_one(present_data, new_data)
#                             newWindow.destroy()
#                             tkinter.messagebox.showinfo("SUCCESS", "Values updated successfully!")
#                         except Exception as e:
#                             tkinter.messagebox.showerror("ERROR", e)

#                 Button(newWindow, text="Update Values", command=update_val, background="blue", foreground="white").grid(row = ind+2, column = 1, pady=20, sticky='ew')

#     except Exception as e:
#         tkinter.messagebox.showerror("ERROR", e)

# # 4. Delete
# def delete_tb():
#     try:
#         id = simpledialog.askinteger(title="DELETE", prompt="Enter the PRN to be deleted: ")

#         if id is not None:
#             query={"PRN":{"$eq":id}}
#             present_data = collection.find_one(query)
            
#             if present_data is None:
#                 tkinter.messagebox.showerror("ERROR", "Cannot DELETE!\nNo record was found with the given PRN !")
#             else:
#                 collection.delete_one(query)
#                 tkinter.messagebox.showinfo("SUCCESS", "Deleted record from Collection successfully!")

#     except Exception as e:
#         tkinter.messagebox.showerror("ERROR", e)

# # CRUD operation buttons
# Label(window ,text = "Operations on collection:", background = "white", font='Helvetica 18 bold').grid(row = 3, column = 0, padx=10, pady=60)

# view_btn = Button(window, text="View", command=view_tb, background="#9629ff", foreground="white", border=3).grid(row = 4, column = 0)
# insert_btn = Button(window, text="Insert", command=insert_tb, background="green", foreground="white", border=3).grid(row = 4, column = 1, sticky='w', columnspan=1)
# update_btn = Button(window, text="Update", command=update_tb, background="blue", foreground="white", border=3).grid(row = 4, column = 1, columnspan=2)
# delete_btn = Button(window, text="Delete", command=delete_tb, background="red", foreground="white", border=3).grid(row = 4, column = 2)

# window.mainloop() # window remains until user closes it
# client.close() # Closing the connection to database