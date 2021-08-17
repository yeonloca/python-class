from tkinter import*

def process():
    print("안녕하세요?")

w = Tk()
button = Button(w, text="클릭하세요!",command=process)
button.pack()
w.mainloop()
