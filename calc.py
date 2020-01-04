#!/usr/bin/env python3
'''
simple calculator
'''

import tkinter

class Calc:
    def __init__(self, master):
        self.master = master
        self.clear()
		
        self.master.title("Katy's Calculator")

        # create screen widget
        self.screen = tkinter.Text(master, state='disabled', width=20, height=4,background="blue", foreground="white", font="Courier 16")

        # position screen in window
        self.screen.grid(row=0,column=0,columnspan=6,padx=5,pady=5)
        self.screen.configure(state ='disabled')
        
        button1 = tkinter.Button(self.master, text='1', fg='white', bg='black', 
            command=lambda: self.click('1'), height=1, width=1) 
        button1.grid(row=2, column=1)
        
        button2 = tkinter.Button(self.master, text='2', fg='white', bg='black', 
            command=lambda: self.click('2'), height=1, width=1) 
        button2.grid(row=2, column=2)
        
       
        button3 = tkinter.Button(self.master, text='3', fg='white', bg='black', 
            command=lambda: self.click('3'), height=1, width=1) 
        button3.grid(row=2, column=3)
        
        buttondiv = tkinter.Button(self.master, text='/', fg='white', bg='black', 
            command=lambda: self.click('/'), height=1, width=1) 
        buttondiv.grid(row=2, column=4)
        
        button4 = tkinter.Button(self.master, text='4', fg='white', bg='black', 
            command=lambda: self.click('4'), height=1, width=1) 
        button4.grid(row=3, column=1)
        
        button5 = tkinter.Button(self.master, text='5', fg='white', bg='black', 
            command=lambda: self.click('5'), height=1, width=1) 
        button5.grid(row=3, column=2)
        
        button6 = tkinter.Button(self.master, text='6', fg='white', bg='black', 
            command=lambda: self.click('6'), height=1, width=1) 
        button6.grid(row=3, column=3)
        
        buttonmult = tkinter.Button(self.master, text='*', fg='white', bg='black', 
            command=lambda: self.click('*'), height=1, width=1) 
        buttonmult.grid(row=3, column=4)
        
        button7 = tkinter.Button(self.master, text='7', fg='white', bg='black', 
            command=lambda: self.click('7'), height=1, width=1) 
        button7.grid(row=4, column=1)
        
        button8 = tkinter.Button(self.master, text='8', fg='white', bg='black', 
            command=lambda: self.click('8'), height=1, width=1) 
        button8.grid(row=4, column=2)
        
        button9 = tkinter.Button(self.master, text='9', fg='white', bg='black', 
            command=lambda: self.click('9'), height=1, width=1) 
        button9.grid(row=4, column=3)
        
        buttonsub = tkinter.Button(self.master, text='-', fg='white', bg='black', 
            command=lambda: self.click('-'), height=1, width=1) 
        buttonsub.grid(row=4, column=4)
        
        buttondes = tkinter.Button(self.master, text='.', fg='white', bg='black', 
            command=lambda: self.click('.'), height=1, width=1) 
        buttondes.grid(row=5, column=1)
        
        button0 = tkinter.Button(self.master, text='0', fg='white', bg='black', 
            command=lambda: self.click('0'), height=1, width=1) 
        button0.grid(row=5, column=2)
        
        buttonequ = tkinter.Button(self.master, text='=', fg='white', bg='black', 
            command=lambda: self.click('='), height=1, width=1) 
        buttonequ.grid(row=5, column=3)
        
        buttonplus = tkinter.Button(self.master, text='+', fg='white', bg='black', 
            command=lambda: self.click('+'), height=1, width=1) 
        buttonplus.grid(row=5, column=4)
        
        buttonclear = tkinter.Button(self.master, text='C', fg='white', bg='black', 
            command=lambda: self.click('C'), height=1, width=1) 
        buttonclear.grid(row=1, column=5)
        
        	
		
    def click(self, button):
        #print(button)
        if button == 'C':
              self.clear()
        if self.state == 0:
            if button in set(['0','1','2','3','4','5','6','7','8','9',"."]):
                if button == ".":
                    if not "." in self.operand1:
                        self.operand1 = self.operand1 + button
                else:
                    self.operand1 = self.operand1 + button
            if button in set(['/','*','-','+']):
                self.state = 1
                self.operation = button
        elif self.state == 1:
            if button == '=':
                self.state = 2
                if self.operation == '+':
                    self.solution = str(float(self.operand1) + float(self.operand2))
                
                if self.operation == '-':
                    self.solution = str(float(self.operand1) - float(self.operand2))
                    
                if self.operation == '*':
                    self.solution = str(float(self.operand1) * float(self.operand2))
                    
                if self.operation == '/':
                    if float(self.operand2) == 0:
                        self.clear()
                        self.solution = 'ERROR: DIVIDE BY 0!'
                    else:
                        self.solution = str(float(self.operand1) / float(self.operand2))
        
            if button in set(['0','1','2','3','4','5','6','7','8','9',"."]):
                if button == ".":
                    if not "." in self.operand2:
                        self.operand2 = self.operand2 + button
                else:
                    self.operand2 = self.operand2 + button
                
                
        elif self.state == 2:
            if button in set(['0','1','2','3','4','5','6','7','8','9',"."]):
                self.clear()
                self.operand1 = self.operand1 + button
            
            if button in set(['/','*','-','+']):
                self.operand1 = self.solution
                self.state = 1
                self.operation = button
                self.operand2 = ""
                self.solution = ""
                
        self.display()        
        
        
        
		
    def clear(self):
        self.operand1 = ""
        self.operand2 = ""
        self.solution = ""
        self.operation = ""
        self.state = 0
        
    def display(self):
        text = "%20s\n%20s\n%20s\n%20s" % ( self.operand1, self.operation, self.operand2, self.solution)
        self.screen.configure(state='normal')
        self.screen.delete('1.0', tkinter.END)
        self.screen.insert(tkinter.END,text)
        self.screen.configure(state ='disabled')
        

def main():
    root = tkinter.Tk()
    calc = Calc(root)
    root.mainloop()

if __name__ == "__main__":
    main()