import sys
sys.path.append('D:\Computing AI')
from functions import areaofcircle as aoc
from functions import areaofrectangular as aor

while True:
    alc = "***This code will find area of rectrangular and area of circle*** \n 1) Enter 1 for find area of circle \n 2) Enter 2 for find area of rectangular."
    print()
    print(alc)
    userinput = input("Enter your choice please =")
    if userinput == "1":
        we = float(input("Enter the area of width = "))
        he = float(input("Enter the area of height = "))
        aor(we,he)
    if userinput == "2":
        r = float(input("Enter the radius ="))
        aoc(r)
    n = input("Do you want to continue type conversion [yes/no]=")
    if n=="no":
        break
    else:
        pass  