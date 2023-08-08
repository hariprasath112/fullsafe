import tkinter
from tkinter import ttk
from tkinter import *
import sv_ttk
from ctypes import windll
from datetime import datetime,date,timedelta
from tkcalendar import DateEntry
import checker
from tkinter.scrolledtext import ScrolledText

windll.shcore.SetProcessDpiAwareness(1)


root=tkinter.Tk()
root.title("fullsafe")

frame=ttk.Frame(root)
frame.pack()


#entry config frame
entryDateFrame=ttk.LabelFrame(frame,text="Entry Configuration")
entryDateFrame.grid(row=0,column=0, sticky=W+E)
#___________________________________________________________________________________________________________________________
#label for first row entry date and month
entryMonth=ttk.Label(entryDateFrame,text="Entry Month")
entryMonth.grid(row=0,column=0,padx=30,pady=10)
entryYear=ttk.Label(entryDateFrame,text="Entry Year")
entryYear.grid(row=0,column=1,padx=30,pady=10)
#input boxes for entry date and month - second row
entryMonthEntry=ttk.Combobox(entryDateFrame,state="readonly",values=["January","Febuary","March","April","May","June","July","August","September","October","Novemeber","December"])
entryMonthEntry.grid(row=1,column=0,padx=30,pady=10)
entryMonthEntry.current((int(datetime.now().strftime('%m'))-2))
entryYearEntry=ttk.Entry(entryDateFrame)
entryYearEntry.insert(0,(date.today().replace(day=1) - timedelta(days=1)).year)
entryYearEntry.grid(row=1,column=1,padx=30,pady=10)
#function to get entry month and year
def getConfig():
    global entryMonthEntry,entryYearEntry
    temp1=entryMonthEntry.get()
    temp2=entryYearEntry.get()
    invoiceDateEntry.configure(month=temp1,year=temp2)

#___________________________________________________________________________________________________________________________
#invoice frame
invoiceFrame=ttk.LabelFrame(frame,text="Invoice Details")
invoiceFrame.grid(row=1,column=0, sticky=W+E)
#invoiceNO details
invoiceNo=ttk.Label(invoiceFrame,text="Invoice No.")
invoiceNo.grid(row=0,column=0,padx=30,pady=10, sticky="ew")
invoiceNoEntry=ttk.Entry(invoiceFrame)
invoiceNoEntry.grid(row=0,column=1,padx=30,pady=10, sticky="ew")
invoiceNoEntry.focus_set()
#invoiceDate
invoiceDate=ttk.Label(invoiceFrame,text="Invoice Date")
invoiceDate.grid(row=1,column=0,padx=30,pady=10, sticky="ew")
invoiceDateEntry=DateEntry(invoiceFrame,showothermonthdays=False,showweeknumbers=False,date_pattern='dd/mm/yyyy')
invoiceDateEntry.grid(row=1,column=1,padx=30,pady=10, sticky="ew")
invoiceNoEntry.bind('<Return>',lambda e: invoiceDateEntry.focus_set())
#___________________________________________________________________________________________________________________________
#gstin
gstNo=ttk.Label(invoiceFrame,text="GST No.")
gstNo.grid(row=2,column=0,padx=30,pady=10, sticky="ew")
gstNoEntry=ttk.Entry(invoiceFrame)
gstNoEntry.grid(row=2,column=1,padx=30,pady=10, sticky="ew")
invoiceDateEntry.bind('<Return>',lambda e: gstNoEntry.focus_set())
#---------------------------------------------------
gstName=tkinter.StringVar()
gstAddress=tkinter.StringVar()
def retreiveGstNo(event=None):
    global gstNum,gstAddress
    gstNumber=gstNoEntry.get()
    checker.check(gstNumber)
    gstName.set(checker.name)   #for bName
    gstAddress.set(checker.add)    #for bAdd

#button that onclick call func
gstGetButton=ttk.Button(invoiceFrame,command=retreiveGstNo,text="✓")
gstGetButton.grid(row=2,column=2, sticky="e")
def lambdaCall():
    retreiveGstNo()
    productEntry.focus_set()
gstNoEntry.bind('<Return>',lambda e: lambdaCall())
#gstGetButton.bind('<Return>',gstGetButton.invoke())   gstGetButton.focus_set() and 
#-------------------------------------------------------
bName=ttk.Label(invoiceFrame,text="Business Name")
bName.grid(row=3,column=0,padx=30,pady=10, sticky="ew")
bNameEntry=ttk.Entry(invoiceFrame,textvariable=gstName)
bNameEntry.grid(row=3,column=1,padx=30,pady=10, sticky="ew")

bAdd=ttk.Label(invoiceFrame,text="Business Address")
bAdd.grid(row=4,column=0,padx=30,pady=10, sticky="ew")
bAddEntry=ttk.Entry(invoiceFrame,textvariable=gstAddress)
bAddEntry.grid(row=4,column=1,padx=30,pady=10, sticky="ew")
#___________________________________________________________________________________________________________________________
#product frame
productFrame=ttk.LabelFrame(frame,text="Product Details")
productFrame.grid(row=2,column=0, sticky=W+E)
#productbox
product=ttk.Label(productFrame,text="Product Name")
product.grid(row=0,column=0,padx=30,pady=10, sticky="ew")
productEntry=ttk.Entry(productFrame,width=35)
productEntry.grid(row=0,column=1,padx=30,pady=10, sticky="ew")
gstGetButton.bind('<Return>',lambda e: productEntry.focus_set())
#gstNoEntry=
#hsn
hsn=ttk.Label(productFrame,text="HSN")
hsn.grid(row=1,column=0,padx=30,pady=10, sticky="ew")
hsnEntry=ttk.Entry(productFrame)
hsnEntry.grid(row=1,column=1,padx=30,pady=10, sticky="w")
productEntry.bind('<Return>',lambda e: hsnEntry.focus_set())
#subtotal
sub=ttk.Label(productFrame,text="Sub Total")
sub.grid(row=2,column=0,padx=30,pady=10, sticky="ew")
subEntry=ttk.Entry(productFrame)
subEntry.grid(row=2,column=1,padx=30,pady=10, sticky="w")
hsnEntry.bind('<Return>',lambda e: subEntry.focus_set())
#extra
extraFrame=tkinter.LabelFrame(productFrame,borderwidth=0,highlightthickness=0)
extraFrame.grid(row=3,column=0, sticky=W+E)
extra=ttk.Label(extraFrame,text="Additional")
extra.grid(row=0,column=0,padx=30,pady=10, sticky="ew")
extraEntry=ttk.Entry(extraFrame,width=13)
extraEntry.grid(row=0,column=1,padx=30,sticky="w")

#tax display
taxFrame=tkinter.LabelFrame(productFrame,borderwidth=0,highlightthickness=0)
taxFrame.grid(row=3,column=1, sticky=W+E)
taxLabel=ttk.Label(taxFrame,text="Tax Amount")
taxLabel.grid(row=0,column=0,padx=30,pady=10, sticky="ew")
taxEntry=ttk.Entry(taxFrame)
taxEntry.grid(row=0,column=1, sticky="w")

#tax selector
taxSelectFrame=tkinter.LabelFrame(productFrame,border=0,highlightthickness=0)
taxSelectFrame.grid(row=4,column=0,sticky=W+E)
taxTypeEntry=ttk.Combobox(taxSelectFrame,width=7,state="readonly",values=["CGST\SGST","IGST"])
taxTypeEntry.grid(row=4,column=0,padx=30,pady=10)
taxTypeEntry.current(0)
taxSelectEntry=ttk.Combobox(taxSelectFrame,width=5,state="readonly",values=["0%","5%","10%","12%","14%","18%","24%","28%"])
taxSelectEntry.grid(row=4,column=1,padx=30,pady=10)
taxSelectEntry.current(5)

#grand total
totalFrame=tkinter.LabelFrame(productFrame,border=0,highlightthickness=0)
totalFrame.grid(row=4,column=1, sticky=W+E)
totalLabel=ttk.Label(totalFrame,text="Grand Total")
totalLabel.grid(row=0,column=0,padx=30,pady=10, sticky="ew")
totalEntry=ttk.Entry(totalFrame)
totalEntry.grid(row=0,column=1, sticky="w")
subEntry.bind('<Return>',lambda e: totalEntry.focus_set())

#button function
def enterFunc():
    x=34

def submitCaller():
    enterButton.focus_set()
    enterFunc()
#buttons
buttonFrame=tkinter.LabelFrame(productFrame,border=0,highlightthickness=0)
buttonFrame.grid(row=5,column=0, sticky=W+E)
clearButton=ttk.Button(buttonFrame,text="Clear")
clearButton.grid(row=0,column=0,padx=15)
redoButton=ttk.Button(buttonFrame,text="Reuse")
redoButton.grid(row=0,column=1,padx=15)

enterButton=ttk.Button(productFrame,command=enterFunc,text="Submit")
enterButton.grid(row=5,column=1,sticky='ns',pady=20)
totalEntry.bind('<Return>',lambda e: submitCaller())


sv_ttk.set_theme("dark") #sets theme
root.mainloop()
