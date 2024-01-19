import numpy as np

def arrey():
    arrey_1 = []
    arrey_2 = []
    
    arrey_1_ = int(input("Enter the size of arrey 1 = "))
    for i in range(arrey_1_):
        arrey_element_1 = int(input("Enter the element for arrey 1 = "))
        arrey_1.append(arrey_element_1)
        
    print("This is arrey 1",arrey_1)
    
    ar_1 = np.array(arrey_1)
    print(ar_1)
    
    arrey_2_ = int(input("Enter the size of arrey 2 = "))
    for i in range(arrey_2_):
        arrey_element_2 = int(input("Enter the element for arrey 2 = "))
        arrey_2.append(arrey_element_2)
    
    print("This is arrey 2",arrey_2)
    
    ar_2 = np.array(arrey_2)
    print(ar_2) 
    
    # Make sure the size of arrey should be same
    addition = ar_1 + ar_2
    print("The value of addition of both arreys", addition)
    
    
arrey()