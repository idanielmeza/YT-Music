from pytube import YouTube
from tkinter import *
from tkinter import messagebox
import os

def descarga():
    url =url_entrada.get()
    url2 = YouTube(url)
    url2.streams.filter(only_audio=True).first().download(r'C:/Musica/')
    messagebox.showinfo('Completado','Descarga Completada!')

wind= Tk()

wind.title('YT Music')
wind.resizable(0,0)
wind.iconbitmap('icon.ico')

imagen = PhotoImage(file='imagen.gif')
imagen= imagen.subsample(10)

frameYT = LabelFrame(wind).grid(row=0)
Label(frameYT,image=imagen).grid(row=1,column=0, rowspan=2)


Label(frameYT,text = 'Url : ', font=('Arial',15)).grid(row=1, column=1,columnspan=3)

url_entrada = Entry(frameYT)
url_entrada.grid(row=2,column=1, columnspan=3)
Label(frameYT).grid(row=3)
Button(frameYT,text = 'Descargar', command = lambda:[descarga(), os.startfile('C:/Musica')]).grid(row=4,column=1, columnspan=3)
Label(frameYT).grid(row=5)
Label(frameYT,text= 'Youtube Music Downloader by D-LEDEZMA', font=('Arial',8)).grid(row=6, column=2, columnspan=3)

wind.mainloop()

