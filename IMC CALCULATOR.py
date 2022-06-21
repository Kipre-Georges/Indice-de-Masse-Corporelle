#MY DISCORD :Georges#4931

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
    RESULTAT.insert(0,res)

def reset():
    EPOIDS.delete(0,END)
    ETAILLE.delete(0,END)
    RESULTAT.delete(0,END)

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

validation=Button(IMC_WIN,text="Valider",font=my_font,bg=bg,command=go)
fermer=Button(IMC_WIN,text="Quitter",font=my_font,command=IMC_WIN.destroy)
reinit_=Button(IMC_WIN,text="Reinitialiser la fenêtre",font=my_font,command=reset)
validation.place(x=100,y=290)
fermer.place(x=100,y=350)
reinit_.place(x=100,y=410)

IMC_WIN.mainloop()
