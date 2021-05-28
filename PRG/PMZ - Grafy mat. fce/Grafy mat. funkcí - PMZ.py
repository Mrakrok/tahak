
from tkinter import *
import pylab as pl 
import math as mt 


def Graf():
    x_min=float(vstup_xmin.get())
    x_max=float(vstup_xmax.get())
    if vyberF.get()==vyber_fce[0]:
        x_min=mt.radians(x_min)
        x_max=mt.radians(x_max)
        x=pl.arrange(x_min,x_max,0.1)
        y=pl.sin(x)
    elif vyberF.get()==vyber_fce[1]:
        x=pl.arrange(x_min,x_max,0.1)
        y=x**3
    else:
        x=pl.arrange(x_min,x_max,0.1)
        y=pl.sqrt(x)
    pl.plot(x,y)
    pl.show()






hlavni=Tk()

#seznam pro otion menu
vyber_fce=["f(x)=sin(x)","f(x)=x**3","f(x)=odmocnina z x"]

#proměnná pro Option menu
vyberF=StringVar()
vyberF.set(vyber_fce[0])

#vzhled aplikace
ram=Label(hlavni,text="Průběh matematické funkce",font="Calibri 10",bd=2,relief="ridge",pady=10,padx=10)
ram.pack(padx=5,pady=5)

popis_vyber=Label(ram,text="Výbšr funkce",font="calibri 10")
popis_vyber.grid(columnspan=2,sticky=W+E)
vyber=OptionMenu(ram,vyberF,vyber_fce)
vyber.grid(row=1,columnspan=2,sticky=W+E,pady=5)

popis_xmin=Label(ram,text="Min. hodnota x [stupně]",font="Calibri 10")
popis_xmin.grid(row=2)
vstup_xmin=Entry(ram,font="Calibri 10")
vstup_xmin.grid(row=3,pady=5)

popis_xmax=Label(ram,text="Max. hodnota x [stupně]",font="Calibri 10")
popis_xmax.grid(row=4)
vstup_xmax=Entry(ram,font="Calibri 10")
vstup_xmax.grid(row=5,pady=5)

graf=Button(ram,text="vykresli \ngraf",font="Calibri 10 bold",command=Graf)
graf.grid(row=2,column=1,rowspan=4,sticky=N+S,pady=5)




hlavni.mainloop()


