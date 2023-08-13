from cProfile import Profile
from pstats import SortKey,Stats
import tkinter
from tkinter import ttk
from tkinter import*
import sv_ttk,ctypes as ct
from ctypes import windll
from datetime import datetime,date,timedelta
from tkcalendar import DateEntry
import openpyxl
from openpyxl.styles import Alignment
import os,sys,openpyxl,subprocess
from tkinter import messagebox
import ntkutils
from openpyxl.styles.alignment import Alignment
from openpyxl.workbook import Workbook
from openpyxl.styles import Font,PatternFill,Border,Side
windll.shcore.SetProcessDpiAwareness(1)
basedir=os.path.dirname(__file__)
_R='fullsafe'
_Q='Product Name'
_P='Invoice Date'
_O='readonly'
_N='#adb5bd'
_M='.xlsx'
_L='Purchase_'
_K='D:\\fullsafe\\'
_J='dark'
_I='IGST'
_H='assets\\mode.txt'
_G='assets\\options.txt'
_F='A1'
_E=None
_D='\\'
_C='<Return>'
_B='w'
_A='ew'
def check(gstin):
	A='csrftoken';import requests;from bs4 import BeautifulSoup;global url,inputName,csrfName;url='https://www.knowyourgst.com/gst-number-search/';inputName='gstnum';csrfName='csrfmiddlewaretoken';client=requests.session();global name;name='';client.get(url)
	if client.get(url).status_code!=200:name+='[GET URL Failure]'
	if A in client.cookies:csrftoken=client.cookies[A]
	else:csrftoken=client.cookies['csrf']
	data={inputName:gstin,csrfName:csrftoken};r=client.post(url,data=data,headers=dict(Referer=url))
	if r.content:0
	else:name+='[Content retrival failure]'
	try:
		soup=BeautifulSoup(r.text,'html.parser');table=soup.find('table',class_='striped highlight questionlist').find_all('tr');data=[]
		for tr in table:data.append([td.text for td in tr.find_all('td')])
		reqData=[]
		for i in range(len(data)):tempList=data[i];reqData.append(tempList[1])
		global add;name=str(reqData[0]);add=str(reqData[6].split(',')[0])
	except:name+='[Parsing Failure]'
def openBook(path):P='Total Tax';O='O2';N='O1';M='M3';L='K3';K='I3';J='K1';I='H1';H='E1';G='center';F='E7E6E6';E='SimSun';D='solid';C='000000';B='thin';A='D0CECE';book=openpyxl.Workbook();sheet=book.active;f=open(resource_path(_G),'r');title=f.read();header1=[title,'','','','PURCHASE','','',entryMonthEntry.get().upper(),'','',entryYearEntry.get(),'','',P,'',''];header2=['','','','','','','','','','','','','','Total Purchase','',''];heading=['Invoice No',_P,'GSTIN',"Seller's Name",'Address',_Q,'HSN Code','Gross Value',_I,'','CGST','','SGST','',P,'Total Invoice Value'];sheet.append(header1);sheet.append(header2);sheet.append(heading);sheet[_F].border=Border(bottom=Side(border_style=B,color=C));sheet[H].border=Border(bottom=Side(border_style=B,color=C));sheet[I].border=Border(bottom=Side(border_style=B,color=C));sheet[J].border=Border(bottom=Side(border_style=B,color=C));sheet.merge_cells('A1:D2');sheet.merge_cells('E1:G2');sheet.merge_cells('H1:J2');sheet.merge_cells('K1:M2');sheet.merge_cells('O1:P1');sheet.merge_cells('O2:P2');sheet.merge_cells('I3:J3');sheet.merge_cells('K3:L3');sheet.merge_cells('M3:N3');sheet.row_dimensions[1].height=20;sheet.row_dimensions[2].height=20;sheet.column_dimensions['A'].width=15;sheet.column_dimensions['B'].width=18;sheet.column_dimensions['C'].width=23;sheet.column_dimensions['D'].width=40;sheet.column_dimensions['E'].width=20;sheet.column_dimensions['F'].width=25;sheet.column_dimensions['G'].width=18;sheet.column_dimensions['H'].width=20;sheet.column_dimensions['I'].width=10;sheet.column_dimensions['J'].width=15;sheet.column_dimensions['K'].width=10;sheet.column_dimensions['L'].width=15;sheet.column_dimensions['M'].width=10;sheet.column_dimensions['N'].width=15;sheet.column_dimensions['O'].width=17;sheet.column_dimensions['P'].width=22;sheet[_F].alignment=Alignment(horizontal=G,vertical=G);sheet[H].alignment=Alignment(horizontal=G,vertical=G);sheet[I].alignment=Alignment(horizontal=G,vertical=G);sheet[J].alignment=Alignment(horizontal=G,vertical=G);sheet[K].alignment=Alignment(horizontal=G);sheet[L].alignment=Alignment(horizontal=G);sheet[M].alignment=Alignment(horizontal=G);sheet[_F].font=Font(name=E,size=36,bold=True);sheet[H].font=Font(name=E,size=36);sheet[I].font=Font(name=E,size=36);sheet[J].font=Font(name=E,size=36);sheet[_F].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet[H].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet[I].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet[J].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet['N1'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['N2'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet[N].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet[O].fill=PatternFill(fill_type=D,start_color=F,end_color=F);sheet['N1'].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet['N2'].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet[N].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet[O].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet['P1'].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet['P2'].border=Border(left=Side(border_style=B,color=C),right=Side(border_style=B,color=C),top=Side(border_style=B,color=C),bottom=Side(border_style=B,color=C));sheet['A3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['B3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['C3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['D3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['E3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['F3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['G3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['H3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet[K].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['J3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet[L].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['L3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet[M].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['N3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['O3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['P3'].fill=PatternFill(fill_type=D,start_color=A,end_color=A);sheet['A3'].font=Font(name=E);sheet['B3'].font=Font(name=E);sheet['C3'].font=Font(name=E);sheet['D3'].font=Font(name=E);sheet['E3'].font=Font(name=E);sheet['F3'].font=Font(name=E);sheet['G3'].font=Font(name=E);sheet['H3'].font=Font(name=E);sheet[K].font=Font(name=E);sheet['J3'].font=Font(name=E);sheet[L].font=Font(name=E);sheet['L3'].font=Font(name=E);sheet[M].font=Font(name=E);sheet['N3'].font=Font(name=E);sheet['O3'].font=Font(name=E);sheet['P3'].font=Font(name=E);sheet[N]='=SUM(O4:O100)';sheet[O]='=SUM(P4:P100)';book.save(path)
root=tkinter.Tk()
f=open(_H,'r')
themeSet=f.read()
if themeSet==_J:ntkutils.dark_title_bar(root)
root.title(_R)
def resource_path(relative_path):
	try:base_path=sys._MEIPASS2
	except Exception:base_path=os.path.abspath('.')
	return os.path.join(base_path,relative_path)
tk_title=_R
root.iconbitmap(resource_path('assets\\logo.ico'))
def openFile():
	month=entryMonthEntry.get();year=entryYearEntry.get();bookpath=month+'_'+year;path=_K+year+_D+month+_D;Path=path+_L+bookpath+_M
	if os.path.exists(Path):os.startfile(Path)
	else:messagebox.showerror('File Error','Sumbit atleast one entry for the file to be created')
def optionsName():
	args=[_G];f=subprocess.call(args,shell=True);f=open(_G,'r');month=entryMonthEntry.get();year=entryYearEntry.get();bookpath=month+'_'+year;path=_K+year+_D+month+_D;Path=path+_L+bookpath+_M
	if os.path.exists(Path):wb=openpyxl.load_workbook(Path);sh=wb.active;f=open(resource_path(_G),'r');sh[_F]=f.read();wb.save(Path)
def theme():
	global themeSet;ask=messagebox.askquestion('Application restart','All data entered now in the fields will be lost. Data sumbitted will not be lost.')
	if ask=='yes':
		f=open(_H,_B)
		if themeSet==_J:f.write('light');f=open(_H,'r');themeSet=f.read();python=sys.executable;os.execl(python,python,*sys.argv)
		else:f.write(_J);f=open(_H,'r');themeSet=f.read();python=sys.executable;os.execl(python,python,*sys.argv)
		sv_ttk.set_theme(themeSet)
	else:0
optionFrame=ttk.Frame(root)
optionFrame.pack(anchor=W,side=tkinter.TOP)
lab1=tkinter.Button(optionFrame,text='File',border=0,fg=_N,command=openFile).pack(side=tkinter.LEFT,padx=(5,7),pady=(0,6))
lab2=tkinter.Button(optionFrame,text='Options',border=0,fg=_N,command=optionsName).pack(side=tkinter.LEFT,padx=(0,7),pady=(0,6))
lab3=tkinter.Button(optionFrame,text='View',border=0,fg=_N,command=theme).pack(side=tkinter.LEFT,pady=(0,6),padx=(0,7))
parent=ttk.Frame(root)
parent.pack(side=tkinter.TOP,anchor=N)
frame=ttk.Frame(parent)
frame.grid(row=0,column=0,sticky=N)
entryDateFrame=ttk.LabelFrame(frame,text='Entry Configuration')
entryDateFrame.grid(row=0,column=0,sticky=N)
entryMonth=ttk.Label(entryDateFrame,text='Entry Month')
entryMonth.grid(row=0,column=0,padx=30,pady=10)
entryYear=ttk.Label(entryDateFrame,text='Entry Year')
entryYear.grid(row=0,column=1,padx=30,pady=10)
entryMonthEntry=ttk.Combobox(entryDateFrame,state=_O,values=['January','Febuary','March','April','May','June','July','August','September','October','Novemeber','December'])
entryMonthEntry.grid(row=1,column=0,padx=30,pady=10)
entryMonthEntry.current(int(datetime.now().strftime('%m'))-2)
entryYearEntry=ttk.Entry(entryDateFrame)
entryYearEntry.insert(0,(date.today().replace(day=1)-timedelta(days=1)).year)
entryYearEntry.grid(row=1,column=1,padx=30,pady=10)
invoiceFrame=ttk.LabelFrame(frame,text='Invoice Details')
invoiceFrame.grid(row=1,column=0,sticky=E+W)
invoiceNo=ttk.Label(invoiceFrame,text='Invoice No.')
invoiceNo.grid(row=0,column=0,padx=30,pady=10,sticky=_A)
invoiceNoEntry=ttk.Entry(invoiceFrame)
invoiceNoEntry.grid(row=0,column=1,padx=30,pady=10,sticky=_A)
invoiceNoEntry.focus_set()
invoiceDate=ttk.Label(invoiceFrame,text=_P)
invoiceDate.grid(row=1,column=0,padx=30,pady=10,sticky=_A)
invoiceDateEntry=DateEntry(invoiceFrame,showothermonthdays=False,showweeknumbers=False,date_pattern='dd/mm/yyyy',month=int(datetime.now().strftime('%m'))-1,year=(date.today().replace(day=1)-timedelta(days=1)).year)
invoiceDateEntry.grid(row=1,column=1,padx=30,pady=10,sticky=_A)
invoiceNoEntry.bind(_C,lambda e:invoiceDateEntry.focus_set())
gstNo=ttk.Label(invoiceFrame,text='GST No.')
gstNo.grid(row=2,column=0,padx=30,pady=10,sticky=_A)
gstNoEntry=ttk.Entry(invoiceFrame)
gstNoEntry.grid(row=2,column=1,padx=30,pady=10,sticky=_A)
invoiceDateEntry.bind(_C,lambda e:gstNoEntry.focus_set())
gstName=tkinter.StringVar()
gstAddress=tkinter.StringVar()
def retreiveGstNo(event=_E):global gstNum,gstAddress;gstNumber=gstNoEntry.get();check(gstNumber);gstName.set(name);gstAddress.set(add)
gstGetButton=ttk.Button(invoiceFrame,command=retreiveGstNo,text='✓')
gstGetButton.grid(row=2,column=2,sticky='e')
def lambdaCall():retreiveGstNo();productEntry.focus_set()
gstNoEntry.bind(_C,lambda e:lambdaCall())
bName=ttk.Label(invoiceFrame,text='Business Name')
bName.grid(row=3,column=0,padx=30,pady=10,sticky=_A)
bNameEntry=ttk.Entry(invoiceFrame,textvariable=gstName)
bNameEntry.grid(row=3,column=1,padx=30,pady=10,sticky=_A)
bAdd=ttk.Label(invoiceFrame,text='Business Address')
bAdd.grid(row=4,column=0,padx=30,pady=10,sticky=_A)
bAddEntry=ttk.Entry(invoiceFrame,textvariable=gstAddress)
bAddEntry.grid(row=4,column=1,padx=30,pady=10,sticky=_A)
productFrame=ttk.LabelFrame(frame,text='Product Details')
productFrame.grid(row=2,column=0,sticky=N)
product=ttk.Label(productFrame,text=_Q)
product.grid(row=0,column=0,padx=30,pady=10,sticky=_A)
productEntry=ttk.Entry(productFrame)
productEntry.grid(row=0,column=1,padx=30,pady=10,sticky=_B)
gstGetButton.bind(_C,lambda e:productEntry.focus_set())
hsn=ttk.Label(productFrame,text='HSN')
hsn.grid(row=1,column=0,padx=30,pady=10,sticky=_A)
hsnEntry=ttk.Entry(productFrame)
hsnEntry.grid(row=1,column=1,padx=30,pady=10,sticky=_B)
productEntry.bind(_C,lambda e:hsnEntry.focus_set())
sub=ttk.Label(productFrame,text='Sub Total')
sub.grid(row=2,column=0,padx=30,pady=10,sticky=_B)
subEntry=ttk.Entry(productFrame)
subEntry.grid(row=2,column=1,padx=30,pady=10,sticky=_B)
hsnEntry.bind(_C,lambda e:subEntry.focus_set())
extraFrame=tkinter.LabelFrame(productFrame,borderwidth=0,highlightthickness=0)
extraFrame.grid(row=3,column=0,sticky=W+E)
extra=ttk.Label(extraFrame,text='Additional')
extra.grid(row=0,column=0,padx=(30,10),pady=10,sticky=_A)
extraEntry=ttk.Entry(extraFrame,width=13)
extraEntry.grid(row=0,column=1,padx=30,sticky=_B)
taxVar=tkinter.StringVar()
totVar=tkinter.StringVar()
taxFrame=tkinter.LabelFrame(productFrame,borderwidth=0)
taxFrame.grid(row=3,column=1,sticky=W+E)
taxLabel=ttk.Label(taxFrame,text='Tax Amount')
taxLabel.grid(row=0,column=0,padx=(15,5),pady=10,sticky=_B)
taxEntry=ttk.Entry(taxFrame,text=taxVar)
taxEntry.grid(row=0,column=1,sticky=_B,padx=(0,15))
tempTax=_E
def subFunc():
	global tempTax,taxVar
	if extraEntry.get()!='':temp=float(subEntry.get())+float(extraEntry.get())
	else:temp=float(subEntry.get())
	tempTax=temp*float(taxSelectEntry.get()[:-1])/100;taxVar.set(tempTax);totVar.set(temp+tempTax);totalEntry.focus_set()
extraEntry.bind(_C,lambda e:subFunc())
taxSelectFrame=tkinter.LabelFrame(productFrame,border=0,highlightthickness=0)
taxSelectFrame.grid(row=4,column=0,sticky=W+E)
taxTypeEntry=ttk.Combobox(taxSelectFrame,width=9,state=_O,values=['CGST\\SGST',_I])
taxTypeEntry.grid(row=4,column=0,padx=30,pady=10)
taxTypeEntry.current(0)
taxSelectEntry=ttk.Combobox(taxSelectFrame,width=3,state=_O,values=['0%','5%','10%','12%','14%','18%','24%','28%'])
taxSelectEntry.grid(row=4,column=1,padx=0,pady=10)
taxSelectEntry.current(5)
totalFrame=tkinter.LabelFrame(productFrame,border=0)
totalFrame.grid(row=4,column=1,sticky=W+E)
totalLabel=ttk.Label(totalFrame,text='Total')
totalLabel.grid(row=0,column=0,padx=30,pady=10,sticky=_B)
totalEntry=ttk.Entry(totalFrame,text=totVar)
totalEntry.grid(row=0,column=1,sticky=_B,padx=(5,1))
subEntry.bind(_C,lambda e:subFunc())
def enterFunc():enterFunction()
def cleaner():invoiceNoEntry.delete(0,tkinter.END);gstNoEntry.delete(0,tkinter.END);bNameEntry.delete(0,tkinter.END);bAddEntry.delete(0,tkinter.END);productEntry.delete(0,tkinter.END);hsnEntry.delete(0,tkinter.END);subEntry.delete(0,tkinter.END);extraEntry.delete(0,tkinter.END);taxEntry.delete(0,tkinter.END);totalEntry.delete(0,tkinter.END);invoiceNoEntry.focus_set()
def reuse():enterFunc();invoiceNoEntry.delete(0,tkinter.END);productEntry.delete(0,tkinter.END);hsnEntry.delete(0,tkinter.END);subEntry.delete(0,tkinter.END);extraEntry.delete(0,tkinter.END);taxEntry.delete(0,tkinter.END);totalEntry.delete(0,tkinter.END);invoiceNoEntry.focus_set()
def submitCaller():enterFunc();cleaner()
buttonFrame=tkinter.LabelFrame(productFrame,border=0,highlightthickness=0)
buttonFrame.grid(row=5,column=0,sticky=W+E)
clearButton=ttk.Button(buttonFrame,text='Clear',command=cleaner)
clearButton.grid(row=0,column=0,padx=15)
reuseButton=ttk.Button(buttonFrame,text='Submit & Reuse',command=reuse)
reuseButton.grid(row=0,column=1,padx=15)
enterButton=ttk.Button(productFrame,command=submitCaller,text='Submit')
enterButton.grid(row=5,column=1,sticky='ns',pady=20)
totalEntry.bind(_C,lambda e:enterButton.focus_set())
enterButton.bind(_C,lambda e:submitCaller())
def enterFunction():
	A='-';getInvoiceNo=invoiceNoEntry.get();getInvoiceDate=invoiceDateEntry.get();getGstNo=gstNoEntry.get();getName=bNameEntry.get();getAdd=bAddEntry.get();getProduct=productEntry.get();getHSN=hsnEntry.get();getSub=subEntry.get();getTaxType=taxTypeEntry.get();getTaxPercent=taxSelectEntry.get();getTotal=totalEntry.get();month=entryMonthEntry.get();year=entryYearEntry.get();bookpath=month+'_'+year;path=_K+year+_D+month+_D;Path=path+_L+bookpath+_M
	if not os.path.exists(path):os.makedirs(path)
	if not os.path.exists(Path):openBook(Path)
	temp1,temp2,percent1,percent2=_E,_E,_E,_E
	if not extraEntry.get()=='':temp=float(subEntry.get())+float(extraEntry.get());igst=temp*float(getTaxPercent[:-1])/100;gst=temp*float(getTaxPercent[:-1])/200
	else:igst=float(getSub)*float(getTaxPercent[:-1])/100;gst=float(getSub)*float(getTaxPercent[:-1])/200
	tempGst=igst
	if getTaxType==_I:temp2=A;percent1=getTaxPercent;percent2=A;gst=A
	else:temp1=A;percent1=A;percent2=str(int(getTaxPercent[:-1])/2)+'%';igst=A
	list=[getInvoiceNo,getInvoiceDate,getGstNo,getName,getAdd,getProduct,getHSN,getSub,percent1,igst,percent2,gst,percent2,gst,tempGst,float(getTotal)];book=openpyxl.load_workbook(Path);sheet=book.active;sheet.append(list);book.save(Path)
sv_ttk.set_theme(themeSet)
root.mainloop()
