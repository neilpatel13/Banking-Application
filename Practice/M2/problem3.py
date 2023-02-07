a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    # TODO add new code here to print the desired result
    
    print(f"{[abs(x) for x in arr]}") 


    #print(f"{[str(x*-1) for x in arr]}")
    #print(f"{[x*-1 for x in arr]}")


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)



#
#temp= []
#for num in arr:
 #       if arr[num] < 0:
  #          arr[num]*-1
   #         temp[num].append(arr[num])
    #print(f"{[abs(x) for x in temp]}") """
    #"""for num in arr:
     #   if arr[num] lt 0:
      #      arr[num] *-1"""
"""
for i in arr:
        if type(arr) is str:
            print(f"{[str(x*-1) for x in arr]}")
        elif type(arr) is float:
            print(f"{[float(x*-1) for x in arr]}")
        elif type(arr) is int:
            print(f"{[int(x*-1) for x in arr]}")
"""