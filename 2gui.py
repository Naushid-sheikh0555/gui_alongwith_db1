from tkinter import *
import mysql.connector
from mysql.connector import Error

def submit():
    fname = entry_fname.get()
    lname = entry_lname.get()
    gender = "Male" if var_gender.get() == 1 else "Female"
    subjects = [listbox.get(i) for i in listbox.curselection()]
    subjects_str = ", ".join(subjects)  # Convert list to string for DB

    try:
        # Connect to MySQL
        connection = mysql.connector.connect(
            host='localhost',
            database='studentdb',
            user='root',
            password=''
        )

        if connection.is_connected():
            cursor = connection.cursor()
            sql = "INSERT INTO students (first_name, last_name, gender, subjects) VALUES (%s, %s, %s, %s)"
            values = (fname, lname, gender, subjects_str)
            cursor.execute(sql, values)
            connection.commit()
            print("Data inserted successfully!")

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

master = Tk()
master.title("Student Form")
master.geometry("400x300")

# --- Frame for personal info ---
frame1 = Frame(master, padx=10, pady=10, relief=RIDGE, borderwidth=2)
frame1.pack(padx=10, pady=10, fill=X)
Label(frame1, text="First Name:").grid(row=0, column=0, sticky=W, pady=2)
entry_fname = Entry(frame1)
entry_fname.grid(row=0, column=1, pady=2)
Label(frame1, text="Last Name:").grid(row=1, column=0, sticky=W, pady=2)
entry_lname = Entry(frame1)
entry_lname.grid(row=1, column=1, pady=2)

# --- Frame for gender selection ---
frame2 = Frame(master, padx=10, pady=10, relief=RIDGE, borderwidth=2)
frame2.pack(padx=10, pady=5, fill=X)
Label(frame2, text="Gender:").grid(row=0, column=0, sticky=W)
var_gender = IntVar()
Radiobutton(frame2, text="Male", variable=var_gender, value=1).grid(row=0, column=1)
Radiobutton(frame2, text="Female", variable=var_gender, value=2).grid(row=0, column=2)

# --- Frame for subjects list ---
frame3 = Frame(master, padx=10, pady=10, relief=RIDGE, borderwidth=2)
frame3.pack(padx=10, pady=5, fill=X)
Label(frame3, text="Subjects:").pack(anchor=W)
listbox = Listbox(frame3, selectmode=MULTIPLE, height=4)
listbox.pack(fill=X)
for subject in ["Python", "J2EE", "CS"]:
    listbox.insert(END, subject)

# --- Submit Button ---
Button(master, text="Submit", command=submit, fg="white", bg="green").pack(pady=10)

master.mainloop()
