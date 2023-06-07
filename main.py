from tkinter import*
from playsound import playsound
from gtts import gTTS
import os 

root = Tk()
root.title("Conversor Texto")
root.geometry('500x420')
root.maxsize(500, 420)
root.minsize(500, 420)
root.configure(bg='#1d1d1d')
def margem(altura):
    tela= Canvas(root,
                 width=500,
                 height=altura,
                 bg='#1d1d1d',
                 bd=0,
                 highlightthickness=0,
                 relief='ridge')
    tela.pack()
def botao(texto, comando, padx):
    botao = Button(root,
                   text=texto,
                   padx=padx,
                   pady=20,
                   command=comando,
                   fg='#FFFFFF',
                   activeforeground='#FFFFFF',
                   bg='#C69749',
                   activebackground='#C69749',
                   relief=FLAT, 
                    font=('Montserrat',12, 'bold') )  
    botao.pack() 
def inicia():
     texto_inserido = e.get()
     fala = gTTS(text=texto_inserido,lang='pt',tld='com.br' )
     arquivo_fala ='arquivo_fala.mp3'
     fala.save(arquivo_fala)
     playsound(arquivo_fala)
def resetar():
      e.delete(0, END)
      os.remove('arquivo_fala.mp3')
margem(20)
titulo = Label(root, 
               bg='#1d1d1d',
               fg='#FFFFFF',
                font=('Montserrat',
                      18,'bold' ),
                text='Conversor de Texto Para Fala' )
titulo.pack()
margem(30)
insere_texto = Label(root, 
      bg='#1d1d1d',
      fg='#FFFFFF',
       font=('Montserrat',
             18 ),
       text='Digite um Texto' )
insere_texto.pack()
margem(30)
e = Entry(root,
          width=25,
          borderwidth=4, 
          relief=FLAT,
          fg='#FFFFFF',
          bg='black',
          font=('Montserrat',
                21,'bold'),
                justify=CENTER)
e.pack()
margem(20)
botao_iniciar = botao('INICIAR', inicia, 37)
margem(20)
botao_reset = botao('Resetar', resetar, 30)
root.mainloop()