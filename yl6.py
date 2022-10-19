def find_max( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
 
 
num = int(input('How many numbers: '))
 
lst = []
 
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
     
print("suurim number on :", find_max(lst))