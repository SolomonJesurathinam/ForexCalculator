from tkinter import *

master = Tk()
master.wm_attributes("-topmost", 1)

master.title("Forex Calculator")
ac_balance = StringVar()
risk = StringVar()
pip = StringVar()

def validate_float(var):
    new_value = var.get()
    try:
        new_value == '' or float(new_value)
        validate_float.old_value = new_value
    except:
        var.set(validate_float.old_value)

validate_float.old_value = ''  # Define function attribute.


Label(master, text="Account Balance").grid(row=0,column=0)
ac_balance.trace('w', lambda nm, idx, mode, var=ac_balance: validate_float(var))
Entry(master,textvariable=ac_balance).grid(row=1,column=0)

Label(master, text="Risk").grid(row=0,column=1)
risk.trace('w', lambda nm, idx, mode, var=risk: validate_float(var))
Entry(master,textvariable=risk).grid(row=1,column=1)

Label(master, text="Pip").grid(row=0,column=2)
pip.trace('w', lambda nm, idx, mode, var=pip: validate_float(var))
Entry(master,textvariable=pip).grid(row=1,column=2)

Label(master,text="EURUSD").grid(row=2,column=0)
text_eur =  Text(master,height=1,width=20)
text_eur.grid(row=3,column=0)
text_eur.insert(END,"0.0001")
text_eur.config(state=DISABLED)

Label(master,text="Lot").grid(row=2,column=1)
text_lot = Text(master,height=1,width=20)
text_lot.grid(row=3,column=1)
text_lot.config(state=DISABLED)

Label(master,text="Amount").grid(row=2,column=2)
text_amount = Text(master,height=1,width=20)
text_amount.grid(row=3,column=2)


def print_content():
    account_bal = float(ac_balance.get())
    risk_value = float(risk.get())
    pip_value = float(pip.get())

    text_amount.delete("1.0",END)
    text_amount.insert(END,(account_bal*risk_value)/100)

    text_lot.config(state=NORMAL)
    Lot_value = ((((account_bal*risk_value)/100)/0.0001)/pip_value)/100000
    text_lot.delete("1.0",END)
    text_lot.insert(END,Lot_value)
    text_lot.config(state=DISABLED)


b1 = Button(master, text="Calculate", command=print_content)
b1.grid(row=4, column=1)

def calculate_risk():
    account_bal = float(ac_balance.get())
    amount1 = float(text_amount.get(1.0,END))

    risk_value = (amount1*100)/account_bal
    risk.set(risk_value)

    risk_value = float(risk.get())
    pip_value = float(pip.get())

    text_lot.config(state=NORMAL)
    Lot_value = ((((account_bal * risk_value) / 100) / 0.0001) / pip_value) / 100000
    text_lot.delete("1.0", END)
    text_lot.insert(END, Lot_value)
    text_lot.config(state=DISABLED)



b2 = Button(master, text="Amt Calc",command=calculate_risk)
b2.grid(row=4,column=2)

master.mainloop()