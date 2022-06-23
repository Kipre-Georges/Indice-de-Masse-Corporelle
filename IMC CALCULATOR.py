
from fileinput import close
from http.client import OK
from math import*
import re
from tkinter import*
import tkinter
from webbrowser import get

from colorama import reinit

def go():
    FPOIDS=EPOIDS.get()
    FTAILLE=ETAILLE.get()
    res=eval(FPOIDS)/eval((FTAILLE))**2
    RESULTAT.insert(0,res.__round__(1))
    if res<18.5:
        DIAGNOSTIC.insert(0,"Dénutrition")
    elif res>=18.5 and res<25:
        DIAGNOSTIC.insert(0,"Normal")
    elif res>=25 and res<30:
        DIAGNOSTIC.insert(0,"Surpoids")
    elif res>=30 and res<35:
        DIAGNOSTIC.insert(0,"Obésité modérée")
    elif res>=35 and res<40:
        DIAGNOSTIC.insert(0,"Obésité sévère")
    elif res>=40:
        DIAGNOSTIC.insert(0,"Obésité morbide")



def reset():
    EPOIDS.delete(0,END)
    ETAILLE.delete(0,END)
    RESULTAT.delete(0,END)
    DIAGNOSTIC.delete(0,END)

IMC_WIN=Tk()
IMC_WIN.geometry("960x540")
IMC_WIN.title("IMC CALCULATOR")

my_font=("Arial",20)
bg="white"

POIDS=Label(IMC_WIN,text="Poids en (kg) : ",font=my_font,bg=bg)
POIDS.place(x=100,y=80)
EPOIDS=Entry(IMC_WIN,font=my_font,bg=bg)
EPOIDS.place(x=450,y=80)

TAILLE=Label(IMC_WIN,text="Entrez votre taille en (m) : ",font=my_font, bg=bg)
TAILLE.place(x=100,y=150)
ETAILLE=Entry(IMC_WIN,font=my_font, bg =bg)
ETAILLE.place(x=450,y=150)

resultat=Label(IMC_WIN,text="Resultat : ",font=my_font, bg=bg)
resultat.place(x=100,y=220)
RESULTAT=Entry(IMC_WIN,font=my_font,bg=bg)
RESULTAT.place(x=450,y=220)


diagnostic=Label(IMC_WIN,text="Diagnostic : ",font=my_font, bg=bg)
diagnostic.place(x=100,y=290)
DIAGNOSTIC=Entry(IMC_WIN,font=my_font,bg=bg)
DIAGNOSTIC.place(x=450,y=290)

validation=Button(IMC_WIN,text="Valider",font=my_font,bg=bg,command=go)
fermer=Button(IMC_WIN,text="Quitter",font=my_font,command=IMC_WIN.destroy)
reinit_=Button(IMC_WIN,text="Reinitialiser la fenêtre",font=my_font,command=reset)

validation.pack(side=BOTTOM,padx=0,pady=0)
fermer.pack(side=BOTTOM,padx=0,pady=0)
reinit_.pack(side=BOTTOM,padx=0,pady=0)

IMC_WIN.mainloop()
