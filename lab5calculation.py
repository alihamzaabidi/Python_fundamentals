"""You need to create a simple calculator using GUI programing. The graphical interface should
allow the user to enter a number in a text field and either add it to or subtract it from a running
total. The running total should always be displayed. The user should be able to resit the
running total to zero using a button Resit. The user will need to input a new value and then
either press the button “+” to add the value to the running total or press “-” button to
decrement the value in the entry from the running total. Each time the buttons “+” or “-” are
pressed, the entry will be cleared and the running total will be updated. The GUI for the
calculator should look like the following:"""


import tkinter as tk

class calculter:
    def __init__(self):
        self.window_frame = tk.Tk() #created main frame
        self.window_frame.title("Simple Arthmatic Operation")
        self.window_frame.configure(bg="gray") #given colour by using bg
        # divided main frame into 3 parts (top,Middle,Bottom)
        self.top_window_frame = tk.Frame(self.window_frame)
        self.middle_window_frame = tk.Frame(self.window_frame)
        self.bottom_window_frame = tk.Frame(self.window_frame)
        #add two label and entry point in middle part 
        self.prompt_lable = tk.Label(self.middle_window_frame,text="Enter the value to be calculated:",bg="gray89")
        self.calculation_entry = tk.Entry(self.middle_window_frame,width= 10,bg='gray89')
        # given widgets for the frame 
        self.prompt_lable.pack(side="left")
        self.calculation_entry.pack(side="left")
        #add lable and display lable in top sub frame 
        self.display_frame = tk.Label(self.top_window_frame,text = "Total=",bg="gray89")
        self.result = tk.StringVar()
        self.result_frame = tk.Label(self.top_window_frame, textvariable=self.result,bg="gray89")
        # given widgets for the frame
        self.display_frame.pack(side="left")
        self.result_frame.pack(side="left")
        # added button in bottom sub frame 
        self.addtion_button = tk.Button(self.bottom_window_frame, text="+", command=self.addtion)
        self.sub_button = tk.Button(self.bottom_window_frame, text="-", command=self.subtraction)
        self.rest_botton = tk.Button(self.bottom_window_frame, text = "Reset",command=self.reset)
        # given widgets for the frame
        self.addtion_button.pack(side="left")
        self.sub_button.pack(side="left")
        self.rest_botton.pack(side="left")
        # pack all the sub frams 
        self.top_window_frame.pack()
        self.middle_window_frame.pack()
        self.bottom_window_frame.pack()
        self.total =0
        tk.mainloop()

    def addtion(self):
        number = self.calculation_entry.get() #get the values from calculation_entry
        if number:
            self.total += int(number) # adding 
            self.result.set(self.total)
            self.calculation_entry.delete(0, tk.END) #clear after add one entity

    def subtraction(self):
        number = self.calculation_entry.get() # this function is for subtracting values 
        if number:
            self.total = int(number) - self.total # minus
            self.result.set(self.total)
            self.calculation_entry.delete(0, tk.END)

    def reset(self): #This function clear all the entity which are in display 
        self.total = 0
        self.result.set(self.total)
        self.calculation_entry.delete(0)



calculator = calculter()


