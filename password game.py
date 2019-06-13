import tkinter as tk
from tkinter import messagebox
import pickle
import random
import time
LARGE_FONT=('Verdana',12,'bold')

class main_frame(tk.Tk):

    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        containers = tk.Frame(self)
        self.title('Password guessing game')
        self.resizable(0,0)
        containers.pack(side = 'top',fill='both',expand =True)
        containers.grid_rowconfigure(0,weight = 1)
        containers.grid_columnconfigure(0,weight = 1)

        self.frames = {}

        for F in (main_page,game,hint,hintingame):
            frame = F(containers,self)
            self.frames[F] = frame
            frame.grid(row=0,column=0,sticky = 'nsew')
        self.show_frame(main_page)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise()

class main_page(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        cl = tk.Canvas(self,bg = 'orange',height = 800,width = 700)
        cl.pack()

        loginbutton = tk.Button(self,text= 'Start', height = 1, width = 5, font =('Verdana',50,'bold'),
                                command = lambda:controller.show_frame(game)).place(x=235,y = 500)
        gamename = tk.Label(self,text = 'Password Guessing Game',font = ('Times New Roman',43,'bold',),
                            width= 19,height=2).place(x=30,y=50)
        
        l2 = tk.Label(self,bg = 'orange',text = 'Produced by Chance',font =('Times New Roman',18,'bold italic')).place(x=450,y=195)

        hintbutton = tk.Button(self,text = 'How to play this game',height = 2, width = 0,font = ('Times New Roman',15,'bold italic'),
                         command = lambda:controller.show_frame(hint)).place(x=255,y=300)



from tkinter import *
#global variables
tries = 10
hintcount = 0
emptylist = []

class game(tk.Frame):

    
    def __init__(self,parent,controller):

        def refresh():
            file = open('C:\pass.txt', 'r')
            pd = file.read()
            pdnocomma = list(pd.split(','))
            passwordslabel.configure(text = str(pd))
        
        def quittomp():
            result = messagebox.askquestion('Back to Main Page',message = 'Are you sure to quit the game?')
            if result == 'yes':
                controller.show_frame(main_page)
                
        def gotohint():
            controller.show_frame(hintingame)

        def getuserpassword1():
            global var
            var = userentry.get()
            file= open('C:\pass.txt', 'a')
            file.write(var+ ',')
            file.close()
            refresh()
            addvalue_but.destroy()
            custom_label.destroy()
            userentry.delete(0,'end')
            userentry.destroy()
            
        def getuserpassword():
            global var
            var = userentry.get()
            file= open('C:\pass.txt', 'a')
            file.write(var+ ',')
            file.close()
            refresh()

        def showuserpassword(event):
            global tries
            hint = random.choice(listforhint)
            var = inputentry.get()
            
            if var == correct:    
                bg1.place(x = 0, y = 0)  
                userentry.place(x = 300, y = 350)
                congrat.place(x = 145,y= 200)
                addvalue_but.place(x = 425,y = 350)
                custom_label.place(x = 78, y = 350)
                instruction.place(x = 165, y = 450)
                     
            if var != correct:
                inputentry.delete(0,'end')
                tries -= 1
                t.insert('insert',' Wrong! Let me give you a hint: ' + str(hint) + '\n')
                tries_label.configure(text = 'Your chances left: ' + str(tries))
                listforhint.remove(str(hint))
                if tries <= 0:
                    t.delete(1.0,END)
        
            if tries == 0 or len(listforhint) == 0:
                bg = Canvas(self,bg = 'black',height = 800,width = 700).pack()
                correct_password = Label(self,bg = 'black',text = 'Correct Password is : ' + str(correct), font = ('Times',21,'bold'),fg = 'white')
                correct_password.place(x = 165, y = 150)
                gg_label = Label(self,bg = 'black', text = 'Game Over',font = ('Times',50,'bold'),fg = 'white')
                gg_label.place(x = 165, y = 200)
                instruction2 = Label(self, bg = 'black', text = '(Close and Run the program to play again!)',font = ('fixesys',11,'bold'),fg = 'white')
                instruction2.place(x = 180, y = 300)
                   
        tk.Frame.__init__(self,parent)
        
        file = open('C:\pass.txt', 'r')
        pd = file.read()
        pdnocomma = list(pd.split(','))
        hintcount = 0
        correct = random.choice(pdnocomma)
        emptylist = []
        listforhint = list(correct)
    
        backtomain = Button(self,text = 'Back to main page', command=quittomp)
        backtomain.place(x =25,y = 10)
        hintbutton = Button(self,text = 'Hint', command = gotohint)
        hintbutton.place(x = 600, y = 10)
        t = Text(self,height = 12, width = 45)
        t.place(x = 150, y = 500)

        tries_label = Label(self, text = 'Your chances left: ' + str(tries),font =('Time News Roman',18,'bold'))
        tries_label.place(x = 200, y = 330)       
        tries_label.configure(text = 'Your chances left: ' + str(tries))

        separate_line = Label(self,text = '____________________________________________________________________________________________________________________________________________')
        separate_line.place(x = 0, y = 370)

        labelofentry = Label(self,text = 'Please enter your guess password:',font = ('Arial',13))
        labelofentry.place(x = 110, y = 400)
    
        inputentry = Entry(self)
        inputentry.place(x = 250, y = 430)
        
        inputnotice = Label(self,text = 'Press(Return)')
        inputnotice.place(x = 357, y =430)
        inputentry.bind('<Return>',showuserpassword)
        
        bg1 = Canvas(self, bg = 'yellow',height = 800,width = 700)
        
        userentry = Entry(self)
        passwords = Label(self, text = 'Current passwords are:', font = ('Time News Roman',10))
        passwords.place(x = 0, y = 80)
        passwordslabel = Label(self, bg = 'yellow' ,text = str(pd),
                     font =('Verdana',10,'bold'))
        passwordslabel.place(x = 0, y = 100)        
        refresh_but = Button(self,text='Refresh the list',command = refresh).place(x = 10, y = 200)         
        addvalue_but = Button(self,text = 'Enter', command = getuserpassword1)
        congrat = Label(self, bg = 'yellow', text = 'Congratuation!', font = ('News',50,'bold'),fg = 'red')
        instruction = Label(self, bg = 'yellow',text = '(Close and Run the program to play again!)',font = ('fixesys',17,'bold'))
        custom_label = Label(self,bg = 'yellow',text = 'Add your own password here: ', font = ('Verdana',10,'bold'))
   
        
class hintingame(tk.Frame):
    
    def __init__(self,parent,controller):
        def backtogame():
            controller.show_frame(game)
            
        tk.Frame.__init__(self,parent)
        
        hint = Label(self,text = 'Welcome to the hint by Chance! \n So in this game, a random password will be generated, \n you have a total of 10 chances to guess the password. \n After each failed try, 1 random letter will be provided. \n If you manage to guess it, you can add in custom password in the list!! \n Have fun guessing!',
                     font=("Helvetica", 16)).place(x =25, y = 200)
        quitbutton = Button(self, text = 'Back to game', command =backtogame).place(x = 25, y = 10)
        

class hint(tk.Frame):
    def __init__ (self,parent,controller):
               
        def quittomp():
            controller.show_frame(main_page)
                
        tk.Frame.__init__(self,parent)
        
        hint = Label(self,text = 'Welcome to the hint by Chance! \n So in this game, a random password will be generated, \n you have a total of 10 chances to guess the password. \n After each failed try, 1 random letter will be provided. \n If you manage to guess it, you can add in custom password in the list!! \n Have fun guessing!',
                     font=("Helvetica", 16)).place(x =25, y = 200)
        quitbutton = Button(self, text = 'Quit to main', command =quittomp).place(x = 25, y = 10)


app = main_frame()
app.mainloop()
                
