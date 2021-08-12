from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Database GUI')
root.iconbitmap('database.ico')
root.geometry('300x480')

conn = sqlite3.connect('address_book.db')
c = conn.cursor()

'''
# Create table
c.execute(""" CREATE TABLE addresses(
      first_name text,
      last_name text,
      address text,
      city text,
      state text,
      zipcode integer
) """)
'''



def delete():

    conn = sqlite3.connect('address_book.db')


    c = conn.cursor()


    c.execute("DELETE from addresses WHERE oid = " + delete_box.get())
    print(' Record deleted successfully')

    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()



    print_record = ''
    for record in records:
        # str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)

    conn.commit()

    conn.close()


def ediit():
    global edit
    edit = Tk()
    edit.title('Update')
    edit.iconbitmap('database.ico')
    edit.geometry('300x480')


    conn = sqlite3.connect('address_book.db')


    c = conn.cursor()

    record_id = delete_box.get()

    # query
    c.execute("SELECT * FROM addresses WHERE oid=" + record_id)

    records = c.fetchall()

    #declaring all text boxes as  global variable
    global f_name_edit
    global l_name_edit
    global address_edit
    global city_edit
    global state_edit
    global zipcode_edit

    f_name_edit = Entry(edit, width=30)
    f_name_edit.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_edit = Entry(edit, width=30)
    l_name_edit.grid(row=1, column=1)

    address_edit = Entry(edit, width=30)
    address_edit.grid(row=2, column=1)

    city_edit= Entry(edit, width=30)
    city_edit.grid(row=3, column=1)

    state_edit = Entry(edit, width=30)
    state_edit.grid(row=3, column=1)

    zipcode_edit = Entry(edit, width=30)
    zipcode_edit.grid(row=4, column=1)



    # Creating labels
    f_name_label = Label(edit, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))

    l_name_label = Label(edit, text="Last Name")
    l_name_label.grid(row=1, column=0)

    address_label = Label(edit, text="Address")
    address_label.grid(row=2, column=0)

    city_label = Label(edit, text="City")
    city_label.grid(row=3, column=0)

    state_label = Label(edit, text="State")
    state_label.grid(row=3, column=0)

    zipcode_label = Label(edit, text="Zip Code")
    zipcode_label.grid(row=4, column=0)

    # loop
    for record in records:
        f_name_edit.insert(0,record[0])
        l_name_edit.insert(0, record[1])
        address_edit.insert(0, record[2])
        city_edit.insert(0, record[3])
        state_edit.insert(0,record[4])
        zipcode_edit.insert(0, record[5])




    save_btn = Button(edit, text=" SAVE ", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=125)


def update():

    conn = sqlite3.connect('address_book.db')

    c = conn.cursor()
    record_id = delete_box.get()
    c.execute(""" UPDATE addresses SET
         first_name = :first,
         last_name = :last,
         address = :address,
         city = :city,
         state = :state,
         zipcode = :zipcode
         WHERE oid = :oid""",
         {'first': f_name_edit.get(),
          'last': l_name_edit.get(),
          'address': address_edit.get(),
          'city': city_edit.get(),
          'state': state_edit.get(),
          'zipcode': zipcode_edit.get(),
          'oid': record_id
               }
    )
    conn.commit()
    conn.close()

    edit.destroy()



def submit():

    conn = sqlite3.connect('address_book.db')


    c = conn.cursor()


    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })

    messagebox.showinfo("Adresses", "   Records added successfully ")

    conn.commit()

    conn.close()

    #clearing text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')


    c = conn.cursor()


    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()


    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' '+ '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=12, column=0, columnspan=2)


    conn.commit()
    conn.close()




#textbox
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)

address = Entry(root, width=30)
address.grid(row=2, column=1)

city = Entry(root, width=30)
city.grid(row=3, column=1)

state = Entry(root, width=30)
state.grid(row=3, column=1)

zipcode = Entry(root, width=30)
zipcode.grid(row=4, column=1)

delete_box = Entry(root, width=30)
delete_box.grid(row=9, column=1, pady=5)

# Creating textbox labels
f_name_label = Label(root,bg='linen', text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0))

l_name_label = Label(root,bg='linen', text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root,bg='linen', text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root,bg='linen', text="City")
city_label.grid(row=3, column=0)

state_label = Label(root,bg='linen', text="State")
state_label.grid(row=3, column=0)


zipcode_label = Label(root,bg='linen', text="Zip Code")
zipcode_label.grid(row=4, column=0)

delete_box_label = Label(root,bg='linen', text="Delete ID")
delete_box_label.grid(row=9, column=0, pady=5)


# Creating submit button

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

# Creating query button

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


# Creating delete button
delete_btn = Button(root, text="Delete", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx =10, ipadx=120)

#Creating update button
update_btn = Button(root, text="Update", command=ediit)
update_btn.grid(row=11, column=0, columnspan=2, pady=10, padx =10, ipadx=120)



conn.commit()

conn.close()


root.config(bg="lemon chiffon")


mainloop()