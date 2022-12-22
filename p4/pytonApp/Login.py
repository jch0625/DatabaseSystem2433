import tkinter as tk
import pymysql

window = tk.Tk()
window.title("My App")
window.geometry("800x1200")

label = tk.Label(text="Please Log in!", font=("Aerial 30 bold italic"))
label.pack(pady=30)

tk.Label(text="Account name: ").place(x=200,y=100)
entry0 = tk.Entry(window)
entry0.place(x=350,y=100)

tk.Label(text="Password: ").place(x=200,y=150)
entry1 = tk.Entry(window)
entry1.place(x=350,y=150)

def login():
    try:
        user =  entry0.get()
        pss = entry1.get()
        res = get_by_key_acct(user, pss)
        id = res['AccountID']
        # window1 = tk.Tk()
        # window1.title("Info")
        # window1.geometry("800x1200")
        rescon = get_by_key_Contract(id)
        connum = rescon['ManagerContract_Num']
        conamount = rescon['Con_Amount']
        type = rescon['Contract_type']
        stat = rescon['Con_Status']
        condate = rescon['Start_date'].strftime("%m/%d/%Y")
        resacccus = get_by_key_cusacc(id)
        SSN = resacccus["Customer_ssn"]
        rescus = get_by_key_cus(SSN)
        fname = rescus['Cus_Fname']
        lname = rescus['Cus_Lname']
        phone = rescus['Cus_phone']
        tk.Label(text="Hello " + fname + ' ' + lname).place(x=150, y=420)
        tk.Label(text="Your Contract Details: ").place(x=150, y=450)
        tk.Label(text="Your Agent Details: ").place(x=150, y=470)
        tk.Label(text="Your Contract Number:  " + str(connum) + "       Your Contract Amount:  $" + str(conamount)  ).place(x=150, y=490)
        tk.Label(text="Your Contract Status:  " + stat + "      Your Contract Plan type: " + type).place(x=150, y=510)
        tk.Label(text="Your Phone number is: " + str(phone)).place(x=150, y=540)

    except:
        print("Invalid Information")
        tk.Label(text="Invalid Information ").place(x=350, y=230)

button = tk.Button(text="Log in",command=login).place(x=350,y=200)

def get_connection():
    usr = "root"
    pw = "jchjchjch"
    h = "localhost"

    conn = pymysql.connect(
        user=usr,
        password=pw,
        host=h,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return conn

def get_by_key_acct(a,b):
    sql = f'''SELECT * FROM dbms.ACCOUNT WHERE Account_name = %s AND PW = %s'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql, args = (a,b))
    result = cur.fetchone()
    return result

def get_by_key_Contract(a):
    sql = f'''SELECT * FROM dbms.ManagerContract WHERE AccountID = %s'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql, args = (a))
    result = cur.fetchone()
    return result

def get_by_key_cusacc(a):
    sql = f'''SELECT * FROM dbms.Customer_Account WHERE Account_id = %s'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql, args = (a))
    result = cur.fetchone()
    return result

def get_by_key_cus(a):
    sql = f'''SELECT * FROM dbms.Customer WHERE Customer_ssn = %s'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql, args = (a))
    result = cur.fetchone()
    return result


window.mainloop()
