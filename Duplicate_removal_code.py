# Write a Python program to remove duplicates from a list.
def duplicates():

    list_1 = []
    
    list_size_1 = int(input("Enter the size of list 1 = "))
    for i in range(list_size_1):
        list_1_elements = int(input("Enter the element in list 1 = "))
        list_1.append(list_1_elements)
    print("list_1  is ", list_1)
    
    common_list_remove = []
    
    for i in list_1:
       if i not in common_list_remove:
           common_list_remove.append(i)
    print("This is total value without duplication" ,common_list_remove)
    
duplicates()