from tkinter import *

root=Tk()
root.title('Retail Billing System')
root.geometry('1270x685')
root.iconbitmap('iconbill.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg="gray20",fg='gold',bd=12,relief=RAISED)
headingLabel.pack(fill=X,pady=10)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')
customer_details_frame.pack(fill=X)

NameLabel=Label(customer_details_frame,text='Name',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
NameLabel.grid(row=0,column=0,padx=20)

nameEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
nameEntry.grid(row=0,column=1,padx=8)

PhoneLabel=Label(customer_details_frame,text='Phone Number',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
PhoneLabel.grid(row=0,column=2,padx=20,pady=2)

PhoneEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
PhoneEntry.grid(row=0,column=3,padx=8)

BillnumberLabel=Label(customer_details_frame,text='Bill Number',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
BillnumberLabel.grid(row=0,column=4,padx=20,pady=2)

billnumberEntry=Entry(customer_details_frame,font=('arial',15),bd=7,width=18)
billnumberEntry.grid(row=0,column=5,padx=8)

searchButton=Button(customer_details_frame,text='SEARCH',font=('arial',12,'bold'),bd=7,width=10)
searchButton.grid(row=0,column=6,padx=10)

productsFrame=Frame(root)
productsFrame.pack()

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')

root.mainloop()