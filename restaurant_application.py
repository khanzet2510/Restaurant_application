from tkinter import*
from tkinter import ttk
import random
from datetime import date
import time
import csv

  
root = Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
root.config(bg="mint cream")
Tops = Frame(root,width = 1800,height=50,relief=SUNKEN,bg="mint cream")
Tops.pack(side=TOP)

f1 = Frame(root,width = 900,height=700,relief=SUNKEN,bg="mint cream")
f1.pack(side=LEFT)
#-----------TreeView------------
lblinfo = Label(Tops, font=( 'aria' ,20,'bold' ),text="List of Order",fg="dark green",anchor=CENTER,bg="mint cream")
lblinfo.grid(row=2,column=6)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text="List of Bill",fg="mint cream",anchor=CENTER,bg="mint cream")
lblinfo.grid(row=2,column=5)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text="List of Bill",fg="mint cream",anchor=CENTER,bg="mint cream")
lblinfo.grid(row=2,column=4)
my_tree=ttk.Treeview()
my_tree['columns']=("Name","Price","Qnty")
my_tree.column("#0",width=30,minwidth=25)
my_tree.column("Name",anchor=W, width=120)
my_tree.column("Price",anchor=CENTER, width=80)
my_tree.column("Qnty",anchor=CENTER,width=80)

my_tree.heading("#0",text="No.",anchor=CENTER)
my_tree.heading("Name",text="Meals",anchor=W)
my_tree.heading("Price",text="Price",anchor=CENTER)
my_tree.heading("Qnty",text="Qnty",anchor=CENTER)
my_tree.pack(padx=10,pady=15,fill=Y)
#------TreeBill-----
my_bill=ttk.Treeview()
my_bill['columns']=("Order No.","Cus.Name","Status","Cost")
my_bill.column("#0",width=30,minwidth=25)
my_bill.column("Order No.",anchor=W, width=70)
my_bill.column("Cus.Name",anchor=W, width=110)
my_bill.column("Status",anchor=CENTER, width=100)
my_bill.column("Cost",anchor=CENTER,width=60)

my_bill.heading("#0",text="No.",anchor=CENTER)
my_bill.heading("Order No.",text="Order No.",anchor=W)
my_bill.heading("Cus.Name",text="Cus.Name",anchor=CENTER)
my_bill.heading("Status",text="Status",anchor=CENTER)
my_bill.heading("Cost",text="Cost",anchor=CENTER)
my_bill.pack(fill=Y)
#------------------TIME--------------
localtime=time.asctime(time.localtime(time.time()))
datetime=date.today()
#-----------------INFO TOP------------
lblinfo = Label(Tops, font=( 'aria' ,30, 'bold' ),text="Restaurant Management System",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblinfo.grid(row=0,column=0)
lblinfo = Label(Tops, font=( 'aria' ,20, ),text=localtime,fg="dark green",anchor=W,bg="mint cream")
lblinfo.grid(row=1,column=0)

#---------------FUNCTION-----------
def Ref():
    x=random.randint(11111, 99999)
    randomRef = str(x)
    rand.set(randomRef)
    cof =float(Fries.get())
    colunch= float(Lunch.get())
    cob= float(Burger.get())
    cofi= float(Filet.get())
    cochee= float(Cheese_burger.get())
    codr= float(Drinks.get())

    costoffries = cof*25
    costoflunch = colunch*40
    costofburger = cob*35
    costoffilet = cofi*50
    costofcheeseburger = cochee*50
    costofdrinks = codr*35
    
    costofmeal =str('%.2f'% (costoffries +  costoflunch + costofburger + costoffilet + costofcheeseburger + costofdrinks))
    PayTax=((costoffries +  costoflunch + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.05)
    Totalcost=(costoffries +  costoflunch + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
    Ser_Charge=((costoffries +  costoflunch + costofburger + costoffilet + costofcheeseburger + costofdrinks)*0.05)
    Service=str('%.2f'% Ser_Charge)
    OverAllCost=str( PayTax + Totalcost + Ser_Charge)
    PaidTax=str('%.2f'% PayTax)

    Service_Charge.set(Service)
    cost.set(costofmeal)
    Tax.set(PaidTax)
    Subtotal.set(costofmeal)
    Total.set(OverAllCost)
header=['Oder No.\t', 'Cus Name\t', 'Cost\t','Date\t']
f= open(f"D:/03-Đại học/02-Học Kì 2-2022/Kỹ Thuật lập trình/04-Finalterm/bills_of_date_{datetime}.csv","a+" )
writer=csv.writer(f)
writer.writerow(header)

l=[]
def qexit():
    root.destroy()
    roo=Tk()
    roo.geometry("700x500")
    f2 = Frame(roo,width = 100,height=300,relief=SUNKEN,bg="mint cream")
    f2.pack(side=TOP)
    roo.title(f"Checking Bill of {datetime}")
    roo.config(bg="mint cream")   
    total_bill=ttk.Treeview()
    total_bill['columns']=("Order No.","Cus.Name","Cost")
    total_bill.column("#0",width=30,minwidth=25)
    total_bill.column("Order No.",anchor=W, width=120)
    total_bill.column("Cus.Name",anchor=W, width=120)
    total_bill.column("Cost",anchor=W, width=80)
    
    total_bill.heading("Order No.",text="Order No.",anchor=W)
    total_bill.heading("Cus.Name",text="Cus. Name",anchor=W)
    total_bill.heading("Cost",text="Cost",anchor=CENTER)
    total_bill.pack(fill=X)
    lblTotal = Label(f2,text="---------------------",fg="mint cream",bg="mint cream")
    lblTotal.grid(row=0,columnspan=2)
    lblTotal = Label(f2,text="---------------------",fg="mint cream",bg="mint cream")
    lblTotal.grid(row=2,columnspan=2)
    btn_quit=Button(f2,padx=1,pady=8, bd=8 ,fg="black",font=('ariel' ,8,'bold'),width=10, text="QUIT", bg="dark sea green",command=roo.destroy)
    btn_quit.grid(row=1, column=1)    
    roo.mainloop()   
    f= open(f"C:/Final/BillList/bills_of_date {datetime}.csv","r",encoding = "utf-8-sig" )
    reader=csv.reader(f) 
    for row in reader:
        row1=row[1]
    total_bill.insert(parent=" ", index='end',values=("1",'3','3')) 
    f.close()  
def reset():
    name.set("")
    rand.set("")
    Fries.set(0)
    Lunch.set(0)
    Burger.set(0)
    Filet.set(0)
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set(0)
    Tax.set("")
    cost.set("")
    Cheese_burger.set(0)
    my_tree.delete(*my_tree.get_children())
def printbill():
    f=open(f"C:\\Final\\PrintBill\\bill {rand.get()}.txt","a+" )
    line=f"Bill no.{rand.get()}\n"
    lines=f"Date:{localtime}\n"
    line0=f"Customer's Name:{name.get()}\n"+"\n"
    line1=f"Fries:\t\t\t{Fries.get()}\n"
    line2=f"Lunch Meal:\t\t{Lunch.get()}\n"
    line3=f"Burger:\t\t\t{Burger.get()}\n"
    line4=f"Pizza Meal:\t\t{Filet.get()}\n"
    line5=f"Chese Burger:\t\t{Cheese_burger.get()}\n"
    line6=f"Drinks:\t\t\t{Drinks.get()}\n"+"\n"
    line7="---------------------------\n"
    line8=f"Total:\t\t\t${Total.get()}\n"
    f.write(line+lines+line0+line1+line2+line3+line4+line5+line6+line7+line8)
    f.close()
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=15)
    f=open(f"C:\\Final\\PrintBill\\bill {rand.get()}.txt","r" )
    for x in f: 
        pdf.cell(60, 10, txt=x, ln=1, align='L')
    pdf.output(f"C:\\Final\\PrintBill_PDF\\bill {rand.get()}.pdf")
    my_tree.insert(parent='',index='end',iid=0,text="1",values=("Fries Meal","$25",f"{Fries.get()}"))
    my_tree.insert(parent='',index='end',iid=1,text="2",values=("Lunch Meal","$35",f"{Lunch.get()}"))
    my_tree.insert(parent='',index='end',iid=2,text="3",values=("Burger Meal","$25",f"{Burger.get()}"))
    my_tree.insert(parent='',index='end',iid=3,text="4",values=("Pizza Meal","$25",f"{Filet.get()}"))
    my_tree.insert(parent='',index='end',iid=4,text="5",values=("Chese Burger","$25",f"{Cheese_burger.get()}"))
    my_tree.insert(parent='',index='end',iid=5,text="6",values=("Drinks","$25",f"{Drinks.get()}"))
    my_bill.insert(parent='',index='end',values=(rand.get(),name.get(),"Processing",f"${Total.get()}"))
    l.append([f'{rand.get()}',f'{name.get()}',f'{Total.get()}',f'{datetime}'])
    f= open(f"C:/Final/BillList/bills_of_date {datetime}.csv","a",encoding = "utf-8-sig" )
    writer=csv.writer(f)
    for i in l:
        writer.writerow(i)
    
def update_item():
    selected = my_bill.focus()
    temp = my_bill.item(selected, 'values')
    sal_up = "Finished"
    my_bill.item(selected, values=(temp[0],temp[1], sal_up, temp[3]))
def deletebill():
    i=my_bill.selection()
    my_bill.delete(i)
#----------Setup Values---------------------
name=StringVar()
rand = StringVar()
Fries = IntVar()
Lunch = IntVar()
Burger =IntVar()
Cheese_burger = IntVar()
Filet =IntVar()
Drinks = IntVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Tax = StringVar()
cost = StringVar()
#----------Insert Label--------------------
lblcus = Label(f1, font=( 'aria' ,16, 'bold' ),text="Customer Name",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblcus.grid(row=0,column=0)
txtcus = Entry(f1,font=('ariel' ,16,'bold') , textvariable=name,bd=6,insertwidth=4,bg="dark sea green" ,justify='left',width=56)
txtcus.place(x=186,y=5)

lblreference = Label(f1, font=( 'aria' ,16, 'bold' ),text="Order No.",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblreference.grid(row=1,column=0)
txtreference = Entry(f1,font=('ariel' ,16,'bold'), textvariable=rand , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtreference.grid(row=1,column=1)

lblfries = Label(f1, font=( 'aria' ,16, 'bold' ),text="Fries Meal",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblfries.grid(row=2,column=0)
txtfries = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Fries , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtfries.grid(row=2,column=1)

lblLunch = Label(f1, font=( 'aria' ,16, 'bold' ),text="Lunch Meal",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblLunch.grid(row=3,column=0)
txtLunch = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Lunch , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtLunch.grid(row=3,column=1)

lblburger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Burger Meal",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblburger.grid(row=4,column=0)
txtburger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Burger , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtburger.grid(row=4,column=1)

lblFilet = Label(f1, font=( 'aria' ,16, 'bold' ),text="Pizza Meal",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblFilet.grid(row=5,column=0)
txtFilet = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Filet , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtFilet.grid(row=5,column=1)

lblCheese_burger = Label(f1, font=( 'aria' ,16, 'bold' ),text="Cheese burger",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblCheese_burger.grid(row=6,column=0)
txtCheese_burger = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Cheese_burger , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtCheese_burger.grid(row=6,column=1)

#--------------------------------------------------------------------------------------
lblDrinks = Label(f1, font=( 'aria' ,16, 'bold' ),text="Drinks",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblDrinks.grid(row=1,column=2)
txtDrinks = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Drinks , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtDrinks.grid(row=1,column=3)

lblcost = Label(f1, font=( 'aria' ,16, 'bold' ),text="cost",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblcost.grid(row=2,column=2)
txtcost = Entry(f1,font=('ariel' ,16,'bold'), textvariable=cost , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtcost.grid(row=2,column=3)

lblService_Charge = Label(f1, font=( 'aria' ,16, 'bold' ),text="Service Charge",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblService_Charge.grid(row=3,column=2)
txtService_Charge = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Service_Charge , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtService_Charge.grid(row=3,column=3)

lblTax = Label(f1, font=( 'aria' ,16, 'bold' ),text="Tax",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblTax.grid(row=4,column=2)
txtTax = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Tax , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtTax.grid(row=4,column=3)

lblSubtotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Subtotal",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblSubtotal.grid(row=5,column=2)
txtSubtotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Subtotal , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtSubtotal.grid(row=5,column=3)

lblTotal = Label(f1, font=( 'aria' ,16, 'bold' ),text="Total",fg="dark green",bd=10,anchor='w',bg="mint cream")
lblTotal.grid(row=6,column=2)
txtTotal = Entry(f1,font=('ariel' ,16,'bold'), textvariable=Total , bd=6,insertwidth=4,bg="dark sea green" ,justify='right')
txtTotal.grid(row=6,column=3)

#-----------------------------------------buttons------------------------------------------
lblTotal = Label(f1,text="---------------------",fg="mint cream",bg="mint cream")
lblTotal.grid(row=7,columnspan=3)

btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="dark sea green",command=Ref)
btnTotal.grid(row=8, column=2)

btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="dark sea green",command=reset)
btnreset.grid(row=8, column=1)

btnprint=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRINT", bg="dark sea green",command=printbill)
btnprint.grid(row=10, column=2)

lblTotal = Label(f1,text="---------------------",fg="mint cream",bg="mint cream")
lblTotal.grid(row=9,columnspan=3)

btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="EXIT", bg="dark sea green",command=qexit)
btnexit.grid(row=10, column=1)

btnupdate=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="UPDATE", bg="dark sea green",command=update_item)
btnupdate.grid(row=8, column=3)

btndel=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="DELETE", bg="dark sea green",command=deletebill)
btndel.grid(row=10, column=3)

root.mainloop()
