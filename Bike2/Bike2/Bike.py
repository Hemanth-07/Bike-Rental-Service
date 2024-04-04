import tkinter as tk
import sys
from tkinter import Frame,Button,Label,Entry,PhotoImage,Text,WORD,Toplevel
import re
from PIL import ImageTk, Image
window=tk.Tk()
window.title('BIKE DETAILS MANAGEMENT SYSTEM')
frame=Frame(window)
bike_id=0

f=open("bike_file.txt",'r+')
for line in f:
    bike_id+=1


#photo=Label(image=pic)
#photo.pack()
img = ImageTk.PhotoImage(Image.open("bikee.jpg"))
l=Label(image=img)
l.pack()
mlabel=Label(text='Bike Renting Details').pack()
def win1():
    top=Toplevel()
    top.title('Insert Bike Details')
    key=Create(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=42,y=340)
    top.mainloop()

def win2():
    top = Toplevel()
    top.title('Search Bike')
    key = Search(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=42,y=170)
    top.mainloop()
def win3():
    top = Toplevel()
    top.title('Delete Bike')
    key = Delete(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=42,y=170)
    top.mainloop()

def win4():
    top = Toplevel()
    top.title('Edit Bike Details')
    key = Edit(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=50,y=300)
    top.mainloop()

def win5():
    top = Toplevel()
    top.title('Display Bike Details')
    key = Display(top)
    top.geometry('500x500')
    button = Button(top, text="Home", command=top.destroy,fg='black',bg='white')
    button.place(x=450,y=340)
    top.mainloop()



button1=Button(height=2,width=30)
button1['text']='Insert Bike Details'
button1['command']=win1
button1.place(x=200,y=90)

button1=Button(height=2,width=30)
button1['text']='Search Bike'
button1['command']=win2
button1.place(x=200,y=180)

button1=Button(height=2,width=30)
button1['text']='Delete Bike'
button1['command']=win3
button1.place(x=200,y=270)

button1=Button(height=2,width=30)
button1['text']='Edit Bike'
button1['command']=win4
button1.place(x=200,y=360)

button1=Button(height=2,width=30)
button1['text']='Display Bikes'
button1['command']=win5
button1.place(x=200,y=450)

class Create(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text']='Enter Bike Name:'
        self.bikname.grid(column=0,row=3)
        self.bname=Entry(self)
        self.bname.grid(column=0,row=4)
        self.bikcomp = Label(self)
        self.bikcomp['text'] = 'Enter Bike Company:'
        self.bikcomp.grid(column=0,row=5)
        self.bcomp = Entry(self)
        self.bcomp.grid(column=0,row=6)
        self.bikorigin = Label(self)
        self.bikorigin['text'] = 'Enter Bike Origin:'
        self.bikorigin.grid(column=0, row=9)
        self.borigin = Entry(self)
        self.borigin.grid(column=0, row=10)
        self.bikprice = Label(self)
        self.bikprice['text'] = 'Enter Bike Price:'
        self.bikprice.grid(column=0,row=7)
        self.bprice = Entry(self)
        self.bprice.grid(column=0,row=8)
        self.button = Button(self)
        self.button['text']='Submit'
        self.button['command']=self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=11, column=9)
        self.button.grid(column=0,row=15)
    def get_data(self):
        global bike_id
        bikedetails=get_bike_details()
        bikename = self.bname.get()
        bikeIndex = search_bike(bikedetails, bikename)
        if bikeIndex>=0:
            self.msg.insert(0.0, "Bike name already exists:")
        else:
            bike_id =bike_id+ 1
            f = open('bike_file.txt', 'a+')
            f.write("{bike_id}|{bname}|{bcomp}|{borigin}|{bprice}$\n".format(bike_id=bike_id, bname=self.bname.get(), bcomp=self.bcomp.get(), borigin=self.borigin.get(), bprice=self.bprice.get()))
            self.msg.insert(0.0, "your bike id is:" + str(bike_id ))
        print('success')

class Search(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Bike Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text'] = 'Search'
        self.button['command'] = self.search_bike
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def search_bike(self):
        global bike_id
        bikedetails = get_bike_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        bikeIndex = search_bike(bikedetails, bname)
        if(bikeIndex >= 0):
            self.msg.insert(0.0, "bike name is: " + bname + "\nyour bike id is:" + str(bikedetails[bikeIndex][0]) + '\n')
        else:
            self.msg.insert(0.0, "record not found"'\n')

class Delete(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Bike Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text'] = 'Delete'
        self.button['command'] = self.delete_bike
        self.button.grid(column=0, row=11)
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.grid(row=3, column=1)
    def delete_bike(self):
        global bike_id
        bikedetails = get_bike_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        bikeIndex = search_bike(bikedetails, bname)
        if bikeIndex >= 0:
            del bikedetails[bikeIndex]
            bike_id-=1
            save_bike_data(bikedetails)
            self.msg.insert(0.0, "bike deleted"'\n')
        else:
            self.msg.insert(0.0, "bike not found"'\n')
        return

def get_bike_details():
    f = open("bike_file.txt", 'r').read()
    f = re.split("[" + "\\".join("$\\n") + "]", f)[:-2]
    f = filter(None, f)
    bikeDetails = [re.split("[" + "\\".join("|") + "]", bike) for bike in f]
    return bikeDetails

def save_bike_data(bike_details):
    bike_details.append([])
    s="$\n".join(['|'.join(bikes) for bikes in bike_details])
    savefile=open("bike_file.txt", 'w')
    savefile.write(s)
    return s

def search_bike(bikedetails, bname):
    bikeIndex = -1
    for index, bikes in enumerate(bikedetails):
        if bname == bikes[1]:
            bikeIndex = index
    return bikeIndex

class Edit(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.bikname = Label(self)
        self.bikname['text'] = 'Enter Bike Name:'
        self.bikname.grid(column=0, row=1)
        self.bname = Entry(self)
        self.bname.grid(column=0, row=2)
        self.button = Button(self)
        self.button['text']='edit'
        self.button['command']=self.edit_widgets
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.button.grid(column=0, row=13)
    def edit_widgets(self):
        self.bikcomp = Label(self)
        self.bikcomp['text'] = 'Enter Bike Company:'
        self.bikcomp.grid(column=0, row=5)
        self.bcomp = Entry(self)
        self.bcomp.grid(column=0, row=6)
        self.bikorigin = Label(self)
        self.bikorigin['text'] = 'Enter Bike Origin:'
        self.bikorigin.grid(column=0, row=9)
        self.borigin = Entry(self)
        self.borigin.grid(column=0, row=10)
        self.bikprice = Label(self)
        self.bikprice['text'] = 'Enter Bike Price:'
        self.bikprice.grid(column=0, row=7)
        self.bprice = Entry(self)
        self.bprice.grid(column=0, row=8)
        self.button = Button(self)
        self.button['text'] = 'Edit'
        self.button['command'] = self.get_data
        self.msg = Text(self, width=30, height=5, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.button.grid(column=0, row=13)
    def get_data(self):
        global bike_id
        bikedetails = get_bike_details()
        bname = self.bname.get()
        self.msg.delete('1.0', tk.END)
        bikeIndex = search_bike(bikedetails, bname)
        if (bikeIndex >= 0):
            bikedetails[bikeIndex] = [str(bike_id),self.bname.get(),self.bcomp.get(), self.borigin.get(), self.bprice.get()]
            save_bike_data(bikedetails)
            print(bikedetails)
            self.msg.insert(0.0, "the bike record edited is:" + str(bike_id))
        else:
            self.msg.insert(0.0, "record not found"'\n')

def list_to_json(bike_details):
    bike_details_json = []
    for bike in bike_details:
        bikeObj = {}
        bikeObj['id'] = bike[0]
        bikeObj['bname'] = bike[1]
        bikeObj['bcomp'] = bike[2]
        bikeObj['borigin'] = bike[3]
        bikeObj['bprice'] = bike[4]
        bike_details_json.append(bikeObj)
    return bike_details_json

def json_to_str_table(bike_details):
    table_content = "ID\t\tBike_Name\t\tBike_Company\t\tBike_Origin\t\tBike_Price\n"
    for bike in bike_details:
        table_content += "{bike_id}\t\t{bname}\t\t{bcomp}\t\t{borigin}\t\t{bprice}\n".format(bike_id=bike['id'],bname=bike['bname'], bcomp=bike['bcomp'], borigin=bike['borigin'], bprice=bike['bprice'])
    return table_content

class Display(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.msg = Text(self, width=90, height=10, wrap=WORD)
        self.msg.insert(0.0, " ")
        self.msg.grid(row=12, column=1)
        self.msg['command']=self.display_bikes()
    def display_bikes(self):
        global bike_id
        bikedetails = get_bike_details()
        bikedetails=list_to_json(bikedetails)
        bikedetails=json_to_str_table(bikedetails)
        self.msg.insert(0.0, "the bike record details are: \n\n" + str(bikedetails)+'\n')

window.mainloop()
