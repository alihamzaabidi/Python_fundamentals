#tuples
x1 = ("Gurdit","Singh",1,2,3)
print(x1,"\nThe type in input is =",type(x1))
print(len(x1))

#check the other case with tuples
ob1 = ("Gurdit",)
obj2 = ("Gurdit")
print("Type of obj1 is =",type(ob1),"\nType of obj2 is =",type(obj2))

#Some other function with tupple
#maximum values......!
x2 = (1,3,5,7,8,9)
print(max(x2), type(x2))
#minmum values in tuple.......!
print(min(x2), type(x2))
#sum of tuples.......!
print(sum(x2),type(x2))
#index values........!
res2 = x2.index(3)
print(res2)


    #list
y = ["Gurdit","Singh",4,6,8,2,3,4]
print(type(y))


#Some other function with list....!
l = [2,4,6,1,9,7,6,10]
print(l)
#insert....!
l.insert(1, "Gurdit")
print(l)
#sort
li = [3,4,5,2,8,9]
li.sort()
print(li)
li.reverse()
print(li)

#generate list
lit = list(range(2,15))
print(lit)

lit2 = list(range(2,20,4))
print(lit2)





#Example 1) Develop a Python function which either returns the float square of its parameter x if the parameter is a number, or prints the string "Sorry Dave, I'm afraid I can't do that" if the parameter is a string, and then returns 0.0.

def float_square(x):
    if x.isdigit():
        r = float(x)
        res = r ** 2.0
        return res
    else:
        print("Sorry Dave, I'm afraid I can't do that")
        return 0.0
    
x = input("Enter the value=")
obj = float_square(x)
print(obj)


# Example 2) Develop a Python program which prompts the user to input a number between 1 and 12, and which also calls this function to print out the times table requested. 
 
def time_table():
    while True:
        x = int(input("Enter the number between 1 to 12 = "))
        if x >=0 and x <=12:
            for i in range(1,11):
                res = x * i
                print(i,"*",x,"=",res)
        else:
            print("Please Enter the number between 1 to 12")
        
        nx = input("Do you want to continue [yes/no] = ")
        if nx == "no":
            break
        else:
            pass

time_table()























    
    

