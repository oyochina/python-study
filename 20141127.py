from Tkinter import *
class App:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.helloA=Button(frame,text="Hello",command=self.hello)
        self.helloA.pack(side=LEFT)

        self.quit=Button(frame,text="Quit",fg="red",command=frame.quit)
        self.quit.pack(side=RIGHT)

    def hello(self):
        print "Hello,world!"

root=Tk()
root.wm_title("Hello")
root.wm_minsize(200,200)

app=App(root)

root.mainloop()
