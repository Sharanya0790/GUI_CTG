from tkinter import * 
from tkinter.ttk import * 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

root = Tk()
root.title("Data Analysis tool")  
root.geometry("1200x1200")
root.columnconfigure(index=0, weight=2)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.columnconfigure(index=3, weight=1)
root.columnconfigure(index=4, weight=1)
root.columnconfigure(index=5, weight=1)
root.columnconfigure(index=6, weight=1)
root.columnconfigure(index=7, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)
root.rowconfigure(index=3, weight=1)
root.rowconfigure(index=4, weight=12)
root.rowconfigure(index=5, weight=12)
root.rowconfigure(index=6, weight=12)
root.rowconfigure(index=7, weight=1)
root.rowconfigure(index=8, weight=1)

label = Label(root, text ="Selection area",font=30)
label.grid(row=0,column=3,columnspan=2)

VINsel = Label(root, text ="VIN selection",font=12)
VINsel.grid(row=2,column=0)
VINentry = Entry(root)
VINentry.grid(row=3,column=0)

Fromsel = Label(root, text ="From",font=12)
Fromsel.grid(row=2,column=1)
Fromselentry = Entry(root)
Fromselentry.grid(row=3,column=1)

Tosel = Label(root, text ="To",font=12)
Tosel.grid(row=2,column=2)
Toselentry = Entry(root)
Toselentry.grid(row=3,column=2)

def is_checked(Checkbutton):
    df= pd.read_csv("D:\\Data\\rawdata.csv",encoding='latin1')
    header = list(df.columns.values)

    df1=df[df.ignition_status==1]
    print(df1.head())
    
    Param = df['engine_speed']
    plt.hist(Param, bins=[0,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000])
    plt.xlabel("Engine rpm")
    plt.show()
    print("I have executed")

def paramsel():
    root1= Tk()
    root1.title("Parameter Selection")  
    root1.geometry("600x600")

    Checkbutton1 = IntVar()  
    Checkbutton2 = IntVar()  
    Checkbutton3 = IntVar()
  
    Button1 = Checkbutton(root1, text = "Enginespeed", 
                          variable = x[0],
                          onvalue = 1,
                          offvalue = 0, command=is_checked(x[0]))
    print(type(Checkbutton1))
    Button1.grid(row=1,column=1)
    Button2 = Checkbutton(root1, text = "Vehiclespeed",
                          variable = x[1],
                          onvalue = 1,
                          offvalue = 0)
    Button2.grid(row=2,column=1)
    Button3 = Checkbutton(root1, text = "Gear position",
                          variable = x[2],
                          onvalue = 1,
                          offvalue = 0)  
    Button3.grid(row=3,column=1)
    submit = Button(root1,text="Submit",command=root1.destroy)
    submit.grid(row=20, column=1)


Parametersel = Label(root, text="Select Parameter",font=12)
Parametersel.grid(row=2, column=6)
parambut = Button(root,text="Select",command=paramsel)
parambut.grid(row=3, column=6)



#Paramselentry = Entry(root)


"""mb=  Menubutton ( root, text="CheckComboBox")
mb.grid(row=3,column=6)
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu

Item0 = IntVar()
Item1 = IntVar()
Item2 = IntVar()

mb.menu.add_checkbutton ( label="Item0",onvalue= True, offvalue= False, variable=Item0)
mb.menu.add_checkbutton ( label="Item1",onvalue= True, offvalue= False, variable=Item1)
mb.menu.add_checkbutton ( label="Item2",onvalue= True, offvalue= False, variable=Item2)"""



plotsel=Label(root, text="Plot selection",font=12)
plotsel.grid(row=1,column=4,columnspan=2)
plotrowsel=Label(root, text="No of rows",font =12)
plotrowsel.grid(row=2,column=4)
Plotrowselentry = Entry(root)
Plotrowselentry.grid(row=3,column=4)

plotcolsel = Label(root, text="No of cols",font=12)
plotcolsel.grid(row=2,column=5)
Plotcolselentry = Entry(root)
Plotcolselentry.grid(row=3,column=5)

plotsel = Label(root, text="Plot type",font=12)
plotsel.grid(row=2,column=3)
Option_sel = StringVar(root,"Select an Option")
#Option_sel.set("Select an Option")
Options = ["Histogram","Scatter plot","Line chart","Pie chart","Bar chart"]
Plotselentry = OptionMenu(root,Option_sel,*Options)
sel_option = Option_sel.get()
print("Selected",Option_sel.get())
Plotselentry.grid(row=3,column=3)

def downloadfunc(sel_option):
    Text1 = Text(root)
    Sampletext= "Plot can be seen here"
    Text1.grid(row=3,column=1,columnspan=6,rowspan=3)
    print("Executing now")
    #Text1.insert(root,Sampletext)
    if sel_option == "Histogram":
        print("You have selected Histogram")
        
    elif sel_option == "Scatter plot":
        print("You have selected Scatter plot")
    elif sel_option == "Line chart":
        print("You have selected Line chart")
    elif sel_option == "Pie chart":
        print("You have selected Pie chart")
    elif sel_option == "Bar chart":
        print("You have selected Bar chart")
    
def downloadplotfunc():
    Text2 = Text(root, bg="yellow")
    Sampletext= "Plot can be seen here1"
    Text2.grid(row=3,column=1,columnspan=6,rowspan=3)
    
downloadbut = Button(root, text="Download",command= downloadfunc(sel_option))
downloadbut.grid(row=2,column=7)

downloadbut2 = Button(root, text="Download and plot", command= downloadplotfunc)
downloadbut2.grid(row=3,column=7)


root.mainloop()