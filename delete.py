from tkinter import *

from tkinter import messagebox
from tkinter import filedialog
import sqlite3

root = Tk()
root.title('Database')

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
    print('Deleted Successfully')


    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()



    print_record = ''
    for record in records:

        print_record += str(record[0]) + ' ' + str(record[1]) + ' ' + '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()

    conn.close()







# Create submit button for databases

def submit():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",{
        'f_name':f_name.get(),
        'l_name':l_name.get(),
        'address':address.get(),
        'city':city.get(),
        'state':state.get(),
        'zipcode':zipcode.get()
    })
    # showinfo messagebox
    messagebox.showinfo("Adresses", "Inserted Successfully")

    conn.commit()

    conn.close()


    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)



def query():
    # Create a databases or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # query of the database
    c.execute("SELECT *, oid FROM addresses")

    records = c.fetchall()
   # print(records)

    # Loop through the results
    print_record=''
    for record in records:
        #str(record[6]) added for displaying the id
        print_record += str(record[0]) + ' ' + str(record[1]) + ' '+ '\t' + str(record[6]) + "\n"

    query_label = Label(root, text=print_record)
    query_label.grid(row=11, column=0, columnspan=2)


    conn.commit()
    conn.close()



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

fnamelabel = Label(root, text="First Name")
fnamelabel.grid(row=0, column=0, pady=(10,0))

lnamelabel = Label(root, text="Last Name")
lnamelabel.grid(row=1, column=0)

addresslabel = Label(root, text="Address")
addresslabel.grid(row=2, column=0)

citylabel = Label(root, text="City")
citylabel.grid(row=3, column=0)

statelabel = Label(root, text="State")
statelabel.grid(row=3, column=0)


zipcodelabel = Label(root, text="Zip Code")
zipcodelabel.grid(row=4, column=0)

deletelabel = Label(root, text="Delete ID")
deletelabel.grid(row=9, column=0, pady=5)



submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0,columnspan=2, pady=10, padx=10, ipadx=100)


query_button = Button(root, text="Show Records", command=query)
query_button.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100)


delete_button = Button(root, text="Delete", command=delete)
delete_button.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=100)




conn.commit()
conn.close()
root.mainloop()