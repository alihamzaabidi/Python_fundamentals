import tkinter

class temconverter:
    def __init__(self):
        self.window_frame = tkinter.Tk() #create main window
        self.window_frame.title("Temperature Converter")
        self.window_frame.configure(bg="gray")
        self.top_frame = tkinter.Frame(self.window_frame) #create three frames in the main window, that will group different widgets
        self.mid_frame = tkinter.Frame(self.window_frame)
        self.bottom_frame = tkinter.Frame(self.window_frame)
        
        
        #create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text = "Enter Temperature in Celsius")
        self.temo_entry = tkinter.Entry(self.top_frame, width = 15)
    
        
        #pack the widgets in the top frame
        self.prompt_label.pack(side = "left")
        self.temo_entry.pack(side = "left")
        
        #create widgets for mid frame
        self.desc_label = tkinter.Label(self.mid_frame, text = "Converted Temperature in Fahrenheit: ")
        #create a StringVar object that will store the converted temperature
        self.result = tkinter.StringVar()
        #create a label that will be used to display the result
        self.result_label = tkinter.Label(self.mid_frame, textvariable = self.result)
        
        #pack the widgets for mid frame
        self.desc_label.pack (side = "left")
        self.result_label.pack (side = "left")

    #create widgets for the bottom frame
        self.calc_button = tkinter.Button(self.bottom_frame, text = "Convert", command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame, text = "Quit", command = self.window_frame.destroy)

    #pack the buttons for bottom window

        self.calc_button.pack(side = "left")
        self.quit_button.pack(side = "left")

    #pack the frames
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        #enter tkinter mainloop
        tkinter.mainloop()
    
    def convert(self):
        #get the celsius value
        celsius = float(self.temo_entry.get())
        #convert celsius into fahrenheit
        fahrenheit = (9/5) * celsius + 32
       
        self.result.set(fahrenheit)
        
        
#create an instance of Temp_Converter_GUI
gui = temconverter()
