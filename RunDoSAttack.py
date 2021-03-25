#KIR18686921 Christopher Kirby
from tkinter import *
from DoS import dosAttack
from Detect import detection 

window = Tk()
window.title("DoS Simulation Tool")

def runDoS():  
    dosAttack()

def detect_service():  
    detection()
    

Button(window, text="  Simulate DoS Attack  ", pady=10, bd=4, command=runDoS ).pack()

window.mainloop()
