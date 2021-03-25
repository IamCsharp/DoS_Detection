#KIR18686921 Christopher Kirby
from tkinter import *
from DoS import dosAttack
from Detect import detection 

window = Tk()
window.title("DoS Detection Tool")

def runDoS():  
    dosAttack()

def detect_service():  
    detection()
    
Button(window, text="  Run Detection Script   ", pady=10, bd=4, command=detect_service ).pack()


window.mainloop()
