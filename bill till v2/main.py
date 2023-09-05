from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
from tkinter import *
from PIL import ImageTk,Image

def clear():
    cosmeticsTaxEntry.delete(0,END)
    DrinkTaxEntry.delete(0,END)
    groceryTaxEntry.delete(0,END)
    
    cosmeticspriceEntry.delete(0,END)
    DrinkpriceEntry.delete(0,END)
    grocerypriceEntry.delete(0,END)
    
    nameEntry.delete(0,END)
    PhoneEntry.delete(0,END)
    billnumberEntry.delete(0,END)
    
    textarea.delete(1.0,END)
    
def send_email():
    def send_gmail():
        try:
            ob=smtplib.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login(senderEntry.get(),PasswordEntry.get())
            message=email_textarea.get(1.0,END)
            reciever_address=recieverEntry.get()
            ob.sendmail(senderEntry.get(),recieverEntry.get(),message)
            ob.quit()
            messagebox.showinfo('Success','Bill is successfully sent',parent=root1)
        except:
            messagebox.showerror('Error','Something went wrong, Please try again',parent=root1)
            root1.destroy()
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        root1=Toplevel()
        root1.grab_set()
        root1.title('Send Gmail')
        root1.config(bg='gray20')
        root1.resizable(0,0)
        
        senderFrame=LabelFrame(root1,text='SENDER',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        senderFrame.grid(row=0,column=0,padx=40,pady=20)
        
        SenderLabel=Label(senderFrame,text="Sender's Email",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        SenderLabel.grid(row=0,column=0,padx=10,pady=8)
        
        senderEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        senderEntry.grid(row=0,column=1,padx=10,pady=8)
        
        PasswordLabel=Label(senderFrame,text="Password",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        PasswordLabel.grid(row=1,column=0,padx=10,pady=8)
        
        PasswordEntry=Entry(senderFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE,show='*')
        PasswordEntry.grid(row=1,column=1,padx=10,pady=8)
        
        recipientFrame=LabelFrame(root1,text='RECIPIENT',font=('arial',16,'bold'),bd=6,bg='gray20',fg='white')
        recipientFrame.grid(row=1,column=0,padx=40,pady=20)
        
        recieverLabel=Label(recipientFrame,text="Email Address",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        recieverLabel.grid(row=0,column=0,padx=10,pady=8)
        
        recieverEntry=Entry(recipientFrame,font=('arial',14,'bold'),bd=2,width=23,relief=RIDGE)
        recieverEntry.grid(row=0,column=1,padx=10,pady=8)
        
        messageLabel=Label(recipientFrame,text="Message",font=('arial',14,'bold'),bd=6,bg='gray20',fg='white')
        messageLabel.grid(row=1,column=0,padx=10,pady=8)
        
        email_textarea=Text(recipientFrame,font=('arial',16,'bold'),bd=2,relief=SUNKEN
                            ,width=42,height=11)
        email_textarea.grid(row=2,column=0,columnspan=2)
        email_textarea.delete(1.0,END)
        email_textarea.insert(END,textarea.get(1.0,END).replace('=','').replace('-','').replace('\t\t\t','\t\t'))
        
        
        sendButton=Button(root1,text='SEND',font=('arial',14,'bold'),
                          width=15,command=send_gmail)
        sendButton.grid(row=2,column=0,pady=20)
                
        root1.mainloop()
        
        
def print_bill():
    if textarea.get(1.0,END)=='\n':
        messagebox.showerror('Error','Bill is empty')
    else:
        file=tempfile.mktemp('.txt')
        open(file,'w').write(textarea.get(1.0,END))
        os.startfile(file,'print')
        


def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0] == billnumberEntry.get():
            f=open(f'bills/{i}', 'r')
            textarea.delete(1.0,END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','Invalid Bill number')
        
if not os.path.exists('bills'):
    os.mkdir('bills')

def save_bill():
    global billnumber
    result=messagebox.askyesno('Confirm','Do you want to save the bill')
    if result:
        bill_content=textarea.get(1.0,END)
        file=open(f'bills/ {billnumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill Number {billnumber} is saved successfully')
        billnumber=random.randint(500,1000)
        
billnumber=random.randint(500,1000)

def bill_area():
    if nameEntry.get()=='' or PhoneEntry.get()=='':
        messagebox.showerror('Error','Customer Details Are required')   
    elif cosmeticspriceEntry.get()=='' and grocerypriceEntry.get()=='' and DrinkpriceEntry.get()=='':
        messagebox.showerror('Error', 'No Products are selected')
    elif cosmeticspriceEntry.get()== 'R 0' and grocerypriceEntry.get()=='R 0' and DrinkpriceEntry.get()=='R 0':
        messagebox.showerror('Error', 'No Products are selected')
        textarea.delete(1.0,END)
    else:
        textarea.insert(END,'\t\t**Welcome Customer**\n')
        textarea.insert(END,f'\nBill Number: {billnumber}\n')
        textarea.insert(END,f'\nCustomer Name: {nameEntry.get()}\n')
        textarea.insert(END,f'\nCustomer Phone Number: {PhoneEntry.get()}\n')
        textarea.insert(END,'\n=======================================================\n')
        textarea.insert(END,'Product\t\t\tQuantity\t\t\tPrice\n')
        textarea.insert(END,'\n=======================================================\n')
        
        
        if bathsopaEntry.get()!='0':
            textarea.insert(END,f'\nBath Soap\t\t\t{bathsopaEntry.get()}\t\t\tR {soapprice}\n')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nFace Cream\t\t\t{facecreamEntry.get()}\t\t\tR {creamprice}\n')
        if facecreamEntry.get()!='0':
            textarea.insert(END,f'\nface Wash\t\t\t{FacewashEntry.get()}\t\t\tR {facewashprice}\n')
        if HairsprayEntry.get()!='0':
            textarea.insert(END,f'\nHair Spray\t\t\t{HairsprayEntry.get()}\t\t\tR {Hairsprayprice}\n')    
        if HairgelEntry.get()!='0':
            textarea.insert(END,f'\nHair Gel\t\t\t{HairgelEntry.get()}\t\t\tR {hairgelprice}\n')
        if BodylotionEntry.get()!='0':
            textarea.insert(END,f'\nBody Lotion\t\t\t{BodylotionEntry.get()}\t\t\tR {lotionprice}\n')
            
        if RiceEntry.get()!='0':
            textarea.insert(END,f'\nRice\t\t\t{RiceEntry.get()}\t\t\tR {riceprice}\n')
        if DaalEntry.get()!='0':
            textarea.insert(END,f'\nDaal\t\t\t{DaalEntry.get()}\t\t\tR {daalprice}\n')
        if SugarEntry.get()!='0':
            textarea.insert(END,f'\nSugar\t\t\t{SugarEntry.get()}\t\t\tR {sugarprice}\n')
        if OliEntry.get()!='0':
            textarea.insert(END,f'\nOil\t\t\t{OliEntry.get()}\t\t\tR {oilprice}\n')    
        if TeaEntry.get()!='0':
            textarea.insert(END,f'\nTea\t\t\t{TeaEntry.get()}\t\t\tR {teaprice}\n')
        if WheatEntry.get()!='0':
            textarea.insert(END,f'\nWheat\t\t\t{WheatEntry.get()}\t\t\tR {wheatprice}\n')    
          
        if CocacolaEntry.get()!='0':
            textarea.insert(END,f'\nCoca Cola\t\t\t{CocacolaEntry.get()}\t\t\tR {cocaprice}\n')
        if SpiritEntry.get()!='0':
            textarea.insert(END,f'\nSpirit\t\t\t{SpiritEntry.get()}\t\t\tR {spiritprice}')
        if LemonadeEntry.get()!='0':
            textarea.insert(END,f'\nLemonede\t\t\t{LemonadeEntry.get()}\t\t\tR {lemonadeprice}\n')
        if JuiceEntry.get()!='0':
            textarea.insert(END,f'\nJuice\t\t\t{JuiceEntry.get()}\t\t\tR {juiceprice}\n')    
        if ICETeaEntry.get()!='0':
            textarea.insert(END,f'\nIce Tea\t\t\t{ICETeaEntry.get()}\t\t\tR {iceteaprice}\n')
        if NectarEntry.get()!='0':
            textarea.insert(END,f'\nNectar\t\t\t{NectarEntry.get()}\t\t\tR {nectarprice}\n')  
        textarea.insert(END,'\n-------------------------------------------------------\n')    
        
        if cosmeticsTaxEntry.get()!='R0.0':
            textarea.insert(END,f'\nCosmetic Tax\t\t\t\t{cosmeticsTaxEntry.get()}')
        if groceryTaxEntry.get()!='R0.0':
            textarea.insert(END,f'\nGrocery Tax\t\t\t\t{groceryTaxEntry.get()}')
        if DrinkTaxEntry.get()!='R0.0':
            textarea.insert(END,f'\nDrink Tax\t\t\t\t{DrinkTaxEntry.get()}')
        textarea.insert(END,f'\n\nTotal Bill \t\t\t\t{totalbill}\n\n')
        save_bill()
        
#functionlity part
def total():
    global soapprice,creamprice,facewashprice,hairgelprice,Hairsprayprice,lotionprice
    global totalbill
    #cosmetics price calculations
    soapprice=int(bathsopaEntry.get())*20.00
    creamprice=int(facecreamEntry.get())*80.00
    facewashprice=int(FacewashEntry.get())*60.00
    Hairsprayprice=int(HairsprayEntry.get())*40.00
    hairgelprice=int(HairgelEntry.get())*50.99
    lotionprice=int(BodylotionEntry.get())*70.99
    
    totalcosmeticsprice=soapprice+creamprice+facewashprice+hairgelprice+Hairsprayprice+lotionprice
    cosmeticspriceEntry.delete(0,END)
    cosmeticspriceEntry.insert(0, f'R {totalcosmeticsprice}')
    cosmeticsTax=totalcosmeticsprice*0.15
    cosmeticsTaxEntry.delete(0,END)
    cosmeticsTaxEntry.insert(0, f'R {cosmeticsTax}')
    
    #grocery price calculations
    global riceprice,daalprice,wheatprice,sugarprice,teaprice,oilprice
    riceprice=int(RiceEntry.get())*120
    daalprice=int(DaalEntry.get())*90
    wheatprice=int(WheatEntry.get())*65
    sugarprice=int(SugarEntry.get())*64
    teaprice=int(TeaEntry.get())*40.50
    oilprice=int(OliEntry.get())*105
    
    totalgrocerysprice=riceprice+daalprice+wheatprice+sugarprice+teaprice+oilprice
    grocerypriceEntry.delete(0,END)
    grocerypriceEntry.insert(0, f'R {totalgrocerysprice}')
    groceryTax=totalgrocerysprice*0.15
    groceryTaxEntry.delete(0,END)
    groceryTaxEntry.insert(0, f'R {groceryTax}')
    
    #Drinks price calculations
    global cocaprice,spiritprice,juiceprice,lemonadeprice,nectarprice,iceteaprice
    cocaprice=int(CocacolaEntry.get())*23
    spiritprice=int(SpiritEntry.get())*22
    juiceprice=int(JuiceEntry.get())*30
    lemonadeprice=int(LemonadeEntry.get())*29.99
    nectarprice=int(NectarEntry.get())*19.99
    iceteaprice=int(ICETeaEntry.get())*15.00
    
    totaldrinksprice=cocaprice+spiritprice+juiceprice+lemonadeprice+nectarprice+iceteaprice
    DrinkpriceEntry.delete(0,END)
    DrinkpriceEntry.insert(0, f'R {totaldrinksprice}')
    DrinkTax=totaldrinksprice*0.15
    DrinkTaxEntry.delete(0,END)
    DrinkTaxEntry.insert(0, f'R {DrinkTax}')
    
    totalbill=totalcosmeticsprice+totalgrocerysprice+totaldrinksprice+cosmeticsTax+groceryTax+DrinkTax
    
root=Tk()
root.title('Retail Billing System')
root.geometry('2500x1000')
root.iconbitmap('pictures/iconbill.ico')
headingLabel=Label(root,text='Retail Billing System',font=('times new roman',30,'bold')
                   ,bg="gray20",fg='gold',bd=12,relief=RAISED)
headingLabel.pack(fill=X)

customer_details_frame=LabelFrame(root,text='Customer Details',font=('times new roman',15,'bold'),
                                  fg='white',bd=8,relief=RAISED,bg='gray20')
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

seacrhImg=PhotoImage(file='pictures/search.png')
searchButton=Button(customer_details_frame,image=seacrhImg,
                    font=('arial',12,'bold'),bd=7,width=32,command=search_bill)
searchButton.grid(row=0,column=6,padx=10)

productsFrame=Frame(root)
productsFrame.pack(fill=X)

cosmeticsFrame=LabelFrame(productsFrame,text='Cosmetics',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')
cosmeticsFrame.grid(row=0,column=0)

bathsoapLabel=Label(cosmeticsFrame,text='Bath Soap',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
bathsoapLabel.grid(row=0,column=0,pady=9,padx=10)

bathsopaEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
bathsopaEntry.grid(row=0,column=1,pady=9,padx=10)
bathsopaEntry.insert(0,0)

facecreamLabel=Label(cosmeticsFrame,text='Face Cream',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
facecreamLabel.grid(row=1,column=0,pady=9,padx=10)

facecreamEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
facecreamEntry.grid(row=1,column=1,pady=9,padx=10)
facecreamEntry.insert(0,0)

FacewashLabel=Label(cosmeticsFrame,text='Face Wash',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
FacewashLabel.grid(row=2,column=0,pady=9,padx=10)

FacewashEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
FacewashEntry.grid(row=2,column=1,pady=9,padx=10)
FacewashEntry.insert(0,0)

HairsprayLabel=Label(cosmeticsFrame,text='Hair Spray',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
HairsprayLabel.grid(row=3,column=0,pady=9,padx=10)

HairsprayEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
HairsprayEntry.grid(row=3,column=1,pady=9,padx=10)
HairsprayEntry.insert(0,0)

hairgelLabel=Label(cosmeticsFrame,text='Hair Gel',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
hairgelLabel.grid(row=4,column=0,pady=9,padx=10)

HairgelEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
HairgelEntry.grid(row=4,column=1,pady=9,padx=10)
HairgelEntry.insert(0,0)

BodylotionLabel=Label(cosmeticsFrame,text='Body Lotion',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
BodylotionLabel.grid(row=5,column=0,pady=9,padx=10)

BodylotionEntry=Entry(cosmeticsFrame,font=('times new roman',15,'bold'),width=10,bd=5)
BodylotionEntry.grid(row=5,column=1,pady=9)
BodylotionEntry.insert(0,0)

groceryFrame=LabelFrame(productsFrame,text='Grocery',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')
groceryFrame.grid(row=0,column=1)

OilLabel=Label(groceryFrame,text='Oil',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
OilLabel.grid(row=0,column=0,pady=9,padx=10)

OliEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
OliEntry.grid(row=0,column=1,pady=9,padx=10)
OliEntry.insert(0,0)

RiceLabel=Label(groceryFrame,text='Rice',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
RiceLabel.grid(row=1,column=0,pady=9,padx=10)

RiceEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
RiceEntry.grid(row=1,column=1,pady=9,padx=10)
RiceEntry.insert(0,0)

DaalLabel=Label(groceryFrame,text='Daal',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
DaalLabel.grid(row=2,column=0,pady=9,padx=10)

DaalEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DaalEntry.grid(row=2,column=1,pady=9,padx=10)
DaalEntry.insert(0,0)

SugarLabel=Label(groceryFrame,text='Sugar',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
SugarLabel.grid(row=3,column=0,pady=9,padx=10)

SugarEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SugarEntry.grid(row=3,column=1,pady=9,padx=10)
SugarEntry.insert(0,0)

TeaLabel=Label(groceryFrame,text='Tea',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
TeaLabel.grid(row=4,column=0,pady=9,padx=10)

TeaEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
TeaEntry.grid(row=4,column=1,pady=9,padx=10)
TeaEntry.insert(0,0)

WheatLabel=Label(groceryFrame,text='Wheat',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
WheatLabel.grid(row=5,column=0,pady=9,padx=10)

WheatEntry=Entry(groceryFrame,font=('times new roman',15,'bold'),width=10,bd=5)
WheatEntry.grid(row=5,column=1,pady=9)
WheatEntry.insert(0,0)

coldDrinkFrame=LabelFrame(productsFrame,text='Drinks',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')
coldDrinkFrame.grid(row=0,column=2)

CocacolaLabel=Label(coldDrinkFrame,text='Coca Cola',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
CocacolaLabel.grid(row=0,column=0,pady=9,padx=10)

CocacolaEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
CocacolaEntry.grid(row=0,column=1,pady=9,padx=10)
CocacolaEntry.insert(0,0)

SpiritLabel=Label(coldDrinkFrame,text='Spirit',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
SpiritLabel.grid(row=1,column=0,pady=9,padx=10)

SpiritEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
SpiritEntry.grid(row=1,column=1,pady=9,padx=10)
SpiritEntry.insert(0,0)

JuiceLabel=Label(coldDrinkFrame,text='Fruit Juice',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
JuiceLabel.grid(row=2,column=0,pady=9,padx=10)

JuiceEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
JuiceEntry.grid(row=2,column=1,pady=9,padx=10)
JuiceEntry.insert(0,0)

ICETeaLabel=Label(coldDrinkFrame,text='ICE Tea',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
ICETeaLabel.grid(row=3,column=0,pady=9,padx=10)

ICETeaEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
ICETeaEntry.grid(row=3,column=1,pady=9,padx=10)
ICETeaEntry.insert(0,0)

LemonadeLabel=Label(coldDrinkFrame,text='Lemonade',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
LemonadeLabel.grid(row=4,column=0,pady=9,padx=10)

LemonadeEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
LemonadeEntry.grid(row=4,column=1,pady=9,padx=10)
LemonadeEntry.insert(0,0)

NectarLabel=Label(coldDrinkFrame,text='Nectar',font=('times new roma',15,'bold'),bg='gray20',
                fg='white')
NectarLabel.grid(row=5,column=0,pady=9,padx=10)

NectarEntry=Entry(coldDrinkFrame,font=('times new roman',15,'bold'),width=10,bd=5)
NectarEntry.grid(row=5,column=1,pady=9)
NectarEntry.insert(0,0)

billframe= Frame(productsFrame,bd=8,relief=GROOVE)
billframe.grid(row=0,column=3,padx=10)

billareaLabel=Label(billframe,text='Bill Area',font=('time new roman',15,'bold'),bd=7,relief=GROOVE)
billareaLabel.pack(fill=X)

scrollbar=Scrollbar(billframe,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=18,width=55,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

billmenuFrame=LabelFrame(root,text='Bill Menu',font=('times new roman',15,'bold'),
                                  fg='gold',bd=8,relief=RAISED,bg='gray20')
billmenuFrame.pack(fill=X)

cosmeticspriceLabel=Label(billmenuFrame,text='Cosmetic Price',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
cosmeticspriceLabel.grid(row=0,column=0,pady=6,padx=10,sticky='w')

cosmeticspriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticspriceEntry.grid(row=0,column=1,pady=6,padx=10)

grocerypriceLabel=Label(billmenuFrame,text='Grocery Price',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
grocerypriceLabel.grid(row=1,column=0,pady=6,padx=10,sticky='w')

grocerypriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
grocerypriceEntry.grid(row=1,column=1,pady=6,padx=10)

DrinkpriceLabel=Label(billmenuFrame,text='Drink Price',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
DrinkpriceLabel.grid(row=2,column=0,pady=6,padx=10,sticky='w')

DrinkpriceEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DrinkpriceEntry.grid(row=2,column=1,pady=6,padx=10)

cosmeticsTaxLabel=Label(billmenuFrame,text='Cosmetic Tax',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
cosmeticsTaxLabel.grid(row=0,column=2,pady=6,padx=10,sticky='w')

cosmeticsTaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
cosmeticsTaxEntry.grid(row=0,column=3,pady=6,padx=10)

groceryTaxLabel=Label(billmenuFrame,text='Grocery Tax',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
groceryTaxLabel.grid(row=1,column=2,pady=6,padx=10,sticky='w')

groceryTaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
groceryTaxEntry.grid(row=1,column=3,pady=6,padx=10)

DrinkTaxLabel=Label(billmenuFrame,text='Drink Tax',font=('times new roma',10,'bold'),bg='gray20',
                fg='white')
DrinkTaxLabel.grid(row=2,column=2,pady=6,padx=10,sticky='w')

DrinkTaxEntry=Entry(billmenuFrame,font=('times new roman',15,'bold'),width=10,bd=5)
DrinkTaxEntry.grid(row=2,column=3,pady=6,padx=10)

buttonframe=Frame(billmenuFrame,bd=8,relief=RAISED)
buttonframe.grid(row=0,column=4,rowspan=3)

totalButton=Button(buttonframe,text='Total',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8, pady=10,command=total)
totalButton.grid(row=0,column=0,pady=20,padx=5)

billButton=Button(buttonframe,text='Bill',font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=8, pady=10,command=bill_area)
billButton.grid(row=0,column=1,pady=20,padx=5)

emailImg=PhotoImage(file='pictures/Email.png')
emailButton=Button(buttonframe,image=emailImg
                   ,bd=5,width=64, pady=10,command=send_email)
emailButton.grid(row=0,column=2,pady=20,padx=5)

printImg=PhotoImage(file='pictures/print.png')
printButton=Button(buttonframe,image=printImg
                   ,bd=5,width=64, pady=10,command=print_bill)
printButton.grid(row=0,column=3,pady=20,padx=5)

clearImg=PhotoImage(file='pictures/clear.png')
clearButton=Button(buttonframe,image=clearImg,font=('arial',16,'bold'),bg='gray20',fg='white'
                   ,bd=5,width=64, pady=10,command=clear)
clearButton.grid(row=0,column=4,pady=20,padx=5)

root.mainloop()