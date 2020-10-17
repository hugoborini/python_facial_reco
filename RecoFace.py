from indentifyLib import *
from tkinter import *
from pprint import pprint

window = Tk()
window.title("python reco")
window.geometry("600x300")

def createInput(message) :
    input_str =  StringVar()
    input_ui = Entry(window, textvariable=input_str, width=30)
    label = Label(window, text=message)
    input_ui_label = [input_ui, label]
    return input_ui_label


path_label_known = createInput("path_to_img")



find=Button(window, text='find occurence', command=lambda : img_reco("Database", f'{path_label_known[0].get()}'))

def createall() :
    path_label_known[1].pack() 
    path_label_known[0].pack()
    find.pack()
    
    


createall()
window.mainloop()
