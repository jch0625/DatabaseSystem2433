import tkinter as tk
import joblib
import pandas as pd
import pymysql
from datetime import date
from pymongo import MongoClient
import certifi
client = MongoClient( "mongodb+srv://dbms:jchjchjch@dbns.swthwi3.mongodb.net/?retryWrites=true&w=majority", tlsCAFile = certifi.where())
db = client["dbmsfinal"]
collection = db["dbms"]

qtamount = 0
plan = ""

# load model
rf = joblib.load("model/rfc_ml_model.m")
rf1 = joblib.load("model/cad_rfc_ml_model.m")
rf2 = joblib.load("model/dm_rfc_ml_model.m")
rf3 = joblib.load("model/htn_rfc_ml_model.m")
rf4 = joblib.load("model/ane_rfc_ml_model.m")
rf5 = joblib.load("model/pe_rfc_ml_model.m")

# Create the main window
window = tk.Tk()
window.title("Quote and create account")
window.geometry("800x1200")

# main_frame = tk.Frame(window)
# main_frame.pack(fill="both", expand=1)
# my_canvas = tk.Canvas(main_frame)
# my_canvas.pack(side="left",fill="both", expand=1)
# sb = tk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview())
# sb.pack(side="right", fill="y")
#
# my_canvas.configure(yscrollcommand=sb.set)
# my_canvas.bind('<configure>', lambda e:my_canvas.configure(scrollregion=my_canvas.bbox("all")))


# Add a label
label = tk.Label(text="Start your quotes!", font=("Aerial 30 bold italic"))
label.pack(pady=30)
age = 0

tk.Label(text="age: ").place(x=50,y=100)
entry0 = tk.Entry(window)
entry0.place(x=170,y=100)

tk.Label(text="blood pressure: ").place(x=400,y=100)
entry1 = tk.Entry(window)
entry1.place(x=540,y=100)

tk.Label(text="specific gravity: ").place(x=50,y=120)
entry2 = tk.Entry(window)
entry2.place(x=170,y=120)

tk.Label(text="albumin: ").place(x=400,y=120)
entry3 = tk.Entry(window)
entry3.place(x=540,y=120)

tk.Label(text="sugar: ").place(x=50,y=140)
entry4 = tk.Entry(window)
entry4.place(x=170,y=140)

tk.Label(text="red blood cells: ").place(x=400,y=140)
entry5 = tk.Entry(window)
entry5.place(x=540,y=140)

tk.Label(text="pus cell: ").place(x=50,y=160)
entry6 = tk.Entry(window)
entry6.place(x=170,y=160)

tk.Label(text="pus cell clumps: ").place(x=400,y=160)
entry7 = tk.Entry(window)
entry7.place(x=540,y=160)

tk.Label(text="bacteria: ").place(x=50,y=180)
entry8 = tk.Entry(window)
entry8.place(x=170,y=180)

tk.Label(text="blood glucose random: ").place(x=400,y=180)
entry9 = tk.Entry(window)
entry9.place(x=540,y=180)

tk.Label(text="blood urea: ").place(x=50,y=200)
entry10 = tk.Entry(window)
entry10.place(x=170,y=200)

tk.Label(text="serum creatinine: ").place(x=400,y=200)
entry11 = tk.Entry(window)
entry11.place(x=540,y=200)

tk.Label(text="sodium: ").place(x=50,y=220)
entry12 = tk.Entry(window)
entry12.place(x=170,y=220)

tk.Label(text="potassium: ").place(x=400,y=220)
entry13 = tk.Entry(window)
entry13.place(x=540,y=220)

tk.Label(text="hemoglobin: ").place(x=50,y=240)
entry14 = tk.Entry(window)
entry14.place(x=170,y=240)

tk.Label(text="packed cell volume: ").place(x=400,y=240)
entry15 = tk.Entry(window)
entry15.place(x=540,y=240)

tk.Label(text="W-B cell count: ").place(x=50,y=260)
entry16 = tk.Entry(window)
entry16.place(x=170,y=260)

tk.Label(text="R-B cell count: ").place(x=400,y=260)
entry17 = tk.Entry(window)
entry17.place(x=540,y=260)

tk.Label(text="Insurance plan: ").place(x=100,y=300)

choices = ['Basic', 'Standard', 'Premium']
variable = tk.StringVar(window)
variable.set('Standard')

w = tk.OptionMenu(window, variable, *choices)
w.place(x=200,y=300)


# Add a button
def on_button_clicked():
    global qtamount
    global plan
    # Get the user's input from the Entry widget
    age = entry0.get()
    bp = entry1.get()
    sg = entry2.get()
    al = entry3.get()
    su = entry4.get()
    rbc = entry5.get()
    pc = entry6.get()
    pcc = entry7.get()
    ba = entry8.get()
    bgr = entry9.get()
    bu = entry10.get()
    sc = entry11.get()
    sod = entry12.get()
    pot = entry13.get()
    hemo = entry14.get()
    pcv = entry15.get()
    wc = entry16.get()
    rc = entry17.get()
    df = pd.DataFrame([age,	bp,	sg,	al,	su,	rbc,pc,	pcc,ba,	bgr,bu,	sc,	sod,pot,hemo,pcv,wc,rc])
    res = rf.predict(df.T)
    res1 = rf1.predict(df.T)
    res2 = rf2.predict(df.T)
    res3 = rf3.predict(df.T)
    res4 = rf4.predict(df.T)
    res5 = rf5.predict(df.T)
    plan = variable.get()
    planrate = 1
    if (plan == "Standard"):
        planrate = 1.2
    elif (plan == "Premium"):
        planrate = 1.5

    qot = planrate * (100 + res[0]*200 + res1[0]*100 + res2[0]*100+ res3[0]*100+ res4[0]*100+ res5[0]*100)
    qtamount = round(qot, 3)
    print("$" + str(qtamount))
    tk.Label(text="Your quote is: $"+ str(qtamount)).place(x=540, y=330)
    collection.insert_one({"age":age,'bp':bp,'sg':sg,'al':al,'su':su,'rbc':rbc,'pc':pc,'pcc':pcc,'ba':ba,'bgr':bgr,'bu':bu,'sc':sc,'sod':sod,'pot':pot,'hemo':hemo,'pcv':pcv,'wc':wc,'rc':rc})


button = tk.Button(text="Submit", command=on_button_clicked).place(x=340,y=330)

#per
tk.Label(text="First Name: ").place(x=50,y=360)
entry18 = tk.Entry(window)
entry18.place(x=170,y=360)
#per
tk.Label(text="Last Name: ").place(x=400,y=360)
entry19 = tk.Entry(window)
entry19.place(x=540,y=360)
#acc
tk.Label(text="Address: ").place(x=50,y=380)
entry20 = tk.Entry(window)
entry20.place(x=170,y=380)
#acc
tk.Label(text="City: ").place(x=400,y=380)
entry21 = tk.Entry(window)
entry21.place(x=540,y=380)
#acc
tk.Label(text="State: ").place(x=50,y=400)
entry22 = tk.Entry(window)
entry22.place(x=170,y=400)
#acc
tk.Label(text="Zip: ").place(x=400,y=400)
entry23 = tk.Entry(window)
entry23.place(x=540,y=400)
#per
tk.Label(text="Phone Number: ").place(x=50,y=420)
entry24 = tk.Entry(window)
entry24.place(x=170,y=420)
#per
tk.Label(text="SSN: ").place(x=400,y=420)
entry25 = tk.Entry(window)
entry25.place(x=540,y=420)

#acc
tk.Label(text="Account Name: ").place(x=50,y=440)
entry26 = tk.Entry(window)
entry26.place(x=170,y=440)

#acc
tk.Label(text="Password: ").place(x=400,y=440)
entry27 = tk.Entry(window)
entry27.place(x=540,y=440)

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

def insertvalue_cus(Customer_ssn, Cus_Fname, Cus_Lname, Cus_phone):
    sql = f'''INSERT INTO dbms.Customer(Customer_ssn, Cus_Fname, Cus_Lname, Cus_phone) VALUES (%s,%s,%s,%s)'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql,args=(Customer_ssn,Cus_Fname, Cus_Lname, Cus_phone))
    conn.commit()
    result = cur.lastrowid

def insertvalue_acc(Account_name,StartDate ,Address,City,State ,Zip ,PW):
    sql = f'''INSERT INTO dbms.Account(Account_name,StartDate ,Address,City,State ,Zip ,PW) VALUES (%s,%s,%s,%s,%s,%s,%s)'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql,args=(Account_name,StartDate ,Address,City,State ,Zip ,PW))
    conn.commit()
    result = cur.lastrowid

def insertvalue_contract(Con_Amount,AccountId, Con_Status,Start_date,Contract_type):
    sql = f'''INSERT INTO dbms.ManagerContract(Con_Amount,AccountId, Con_Status,Start_date,Contract_type) VALUES (%s,%s,%s,%s,%s)'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql,args=(Con_Amount,AccountId, Con_Status,Start_date,Contract_type))
    conn.commit()
    result = cur.lastrowid

def insertvalue_Cus_Acc(Customer_ssn,Account_id):
    sql = f'''INSERT INTO dbms.Customer_Account(Customer_ssn,Account_id) VALUES (%s,%s)'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql,args=(Customer_ssn,Account_id))
    conn.commit()
    result = cur.lastrowid


def get_by_key_acct(a):
    sql = f'''SELECT AccountId FROM dbms.ACCOUNT WHERE Account_name = %s'''
    conn = get_connection()
    cur = conn.cursor()
    res = cur.execute(sql, args = (a))
    result = cur.fetchone()
    return result

def Create_acc():
    today = date.today()
    Fname = entry18.get()
    Lname = entry19.get()
    Address = entry20.get()
    City = entry21.get()
    State = entry22.get()
    Zip = entry23.get()
    Phone = entry24.get()
    SSN = entry25.get()
    AccName = entry26.get()
    Pw = entry27.get()
    insertvalue_cus(SSN, Fname, Lname, Phone)
    insertvalue_acc(AccName,today ,Address,City,State ,Zip ,Pw)
    id = get_by_key_acct(AccName)
    insertvalue_contract(qtamount,id['AccountId'], "Active", today,plan)
    insertvalue_Cus_Acc(SSN,id['AccountId'])
    tk.Label(text="Account Created").place(x=400, y=500)

button = tk.Button(text="Create Account", command=Create_acc).place(x=400,y=480)



# Run the main loop


window.mainloop()



