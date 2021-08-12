from tkinter import *
import sqlite3
root=Tk()
root.title("DAATA")


conn=sqlite3.connect('addressbook.db')




c = conn.cursor()

#c.execute(""" CREATE TABLE addresses(
#first_name text,
#last_name text,
#address text,
#city text,
#state text,
#zipcode integer)""")


#print("Table created sucessfully")
def submit():
    # clear the text boxes
    f_name.delete(0,END)
    l_name.delete(0,END)
    address.delete(0,END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)




first_name=Label(root,text="First name").grid(row=0,column=0)
name1=Entry(root).grid(row=0,column=1)

last_name=Label(root,text="Last name").grid(row=1,column=0)
name2=Entry(root).grid(row=1,column=1)

add=Label(root,text="Address").grid(row=2,column=0)
address1=Entry(root).grid(row=2,column=1)

city_name=Label(root,text="City").grid(row=3,column=0)
city1=Entry(root).grid(row=3,column=1)

zipcode=Label(root, text="Zipcode").grid(row=4,column=0)
zip1=Entry(root).grid(row=4, column=1)

submit_btn = Button(root, text="Add Records", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)








conn.commit()
conn.close()
mainloop()