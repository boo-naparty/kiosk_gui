from tkinter import *

class Test():
   def __init__(self):
       self.root = Tk()
       self.label=Label(self.root,
                           text = "Label")
       self.buttonForget = Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.pack_forget())
       self.buttonRecover = Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.pack())       
       
       self.buttonForget.pack()
       self.buttonRecover.pack()
       self.label.pack(side="bottom")
       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
app = Test()