# Example 1) Type conversion using inbuilt function
nu = int(input("Enter the Integer value = "))
flot = float(input("Enter The float values = "))
strg = input("Enter the string = ")

print("***The value you have entered ****")
print("Integer Value = ", nu,"=",type(nu),"\n", "Float Value = ",flot,"=",type(flot),"\n","String Value",strg,"=",type(strg))
print("")
while True:
    alcn = "**** What would you like to do type conversion **** \n String to integers = st \n String to Float = sf \n Integer to float = if \n Float to Integer = fi \n Converting Number into String = ns \n Converting Float into String = fs"
    print()
    print(alcn)
    action = input("Enter Your Choice Alliance = ")
    if action == "st":
        print("Type casting of value before conversion =",strg,"=",type(strg))
        ou = int(strg)
        print("Type casting of value before conversion =",ou,"=", type(ou))
    if action == "sf":
        print("Type casting of value before conversion =",strg,"=", type(strg))
        ou1 = float(strg)
        print("Type casting of value before conversion =",ou1,"=", type(ou1))
    if action == "if":
        print("Type casting of value before conversion =",nu,"=",type(nu))   
        ou2 = float(nu)
        print("Type casting of value before conversion =",ou2,"=",type(ou2))
    if action == "fi":
        print("Type casting of value before conversion =",flot,"=",type(flot))
        ou3 = int(flot)
        print("Type casting of value before conversion =",ou3,"=",type(ou3))
    if action == "ns":
        print("Type casting of value before conversion =",nu,"=",type(nu))
        ou4 = str(nu)
        print("Type casting of value before conversion =",ou4,"=",type(ou4))
    if action == "fs":
        print("Type casting of value before conversion =",flot,"=",type(flot))
        ou5 = str(flot)
        print("Type casting of value before conversion =",ou5,"=",type(ou5))
    nxt = input("Do you want to continue type conversion [yes/no]=")
    if nxt=="no":
        break
    else:
        pass  

# Example 1.2 `Using %s to interpolate a string inside a string
print("Example 1.2 `Using %s to interpolate a string inside a string")
srt = input("Please Enter Your Name = ")
out = "Hi %s. Thanks for chosing Birmingham City University" % srt
print(out)

# Example 1.3 Experiment with getting %d, %f and %s  int, float and string interpolations the wrong way around compared to the literal or variable values. E.G. see what happens when you evaluate

print("Experiment with getting %d, %f and %s  int, float and string interpolations the wrong way around compared to the literal or variable values. E.G. see what happens when you evaluate")

# interpolate of ints integer placeholder
print("interpolate of ints integer placeholder")

flon = 78.88899
ion = "The value of float %d turncate into integer value" % flon
print(ion)

# interpolation of float placeholder for integer

iton = 12
fltno = "The value of integer %f into float value" % iton
print(fltno)

# %.4 f reserved 4 digit precision 
iton = 16
fltno = "The value of integer %.4f into float value" % iton
print(fltno)

#Example 1.4
# % 10.4 f / 10 space is reserved for float with 4 digit precision 
iton = 13
fltno = "The value of integer %10.4f into float value" % iton
print(fltno)

# Try a selection of mismatched conversions and observe the results
# if we used %.4 d that will consider first 4 values before . dot if value is single digit then it add 0 in front 
test1 = 75.4855686
ou8 = "Try some float %.4d handling" % test1
print(ou8)


#Example 1.5 Experiment with putting a number between % and d, f or s when interpolating a value into a string e.g. %10s . Then try putting a dot before the number  e.g. %.10s . Then try putting numbers both sides of the dot. e.g. %10.2f . 

# %.2s will consider only two alphabet of string
stt = "Hi my name is %.2s and i'm student of BCU " % "Gurdit singh"
print(stt)       

# %11.6 11 space is reserved for string  6 digit for precions 
stt = "Hi my name is %11.6s and i'm student of BCU " % "Gurdit singh"
print(stt)    

# % 10.4 f / 10 space is reserved for float with 4 digit precision 
iton1 = 90
fltno = "The value of integer %10.4f into float value" % iton1
print(fltno)

# %.4 f reserved 4 digit precision 
iton = 13
fltno = "The value of integer %.4f into float value" % iton
print(fltno)


test1 = 1313.13
ou8 = "Try some float %.4d handling" % test1
print(ou8)


test1 = 75.4855686
ou8 = "Try some float %6.4d handling" % test1
print(ou8)


#2	Define simple Python functions with input and output

def percentage(x,y):
    c = (x/y)*100
    print(c)

n = int(input("Enter the total marks in subject ="))
t = int(input("Enter the total subject ="))
to = t*100
percentage(n,to)



#2.2 define and test a function called rectarea() which returns the area of a rectangle. It must take 2 parameters, w for the width, and h for the height of the rectangle. (Use a comma (,) to delimit the w and h function parameters.)

def areaofrectangular(w,h):
    area = w*h
    print("The width of area is",we, "and the height of area is ",he,"area of rectangular is = %.3f" %area)

we = float(input("Enter the area of width = "))
he = float(input("Enter the area of height = "))
areaofrectangular(we,he)



#Example 3 Use of branching alternative paths of code execution using if-elif-else structure.

nu = int(input("Enter how old is car ="))

if (nu <= 2):
    print("brand new condition")
elif (nu > 2 and nu <= 5):
    print("Good condition")
elif (nu >5 and nu <= 10):
    print("Fine Condition")
else:
    print("bad condition")
    
#Example 4 Experiment by testing logical and Boolean expressions using the Python command line

# and operation logical, boolean expressoin >= 

age = 19
adult = True

if (age >=18 and adult):
    print("Its adult")
else:
    print("not adult")

# or operation logical, boolean expressoin >= 

age = 11
adult = False
if (age >= 5 or adult):
    print("Its student")
else:
    print("Not a student")








