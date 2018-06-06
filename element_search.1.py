'''
Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) 
and another number. 

The function decides whether or not the given number is inside the list
and returns (then prints) an appropriate boolean.

Extra: use binary search.


listb = [1, 3, 5, 30, 42, 43, 500]
n = 3

while len(listb) > 1:
    mid_len = len(listb) // 2
    middle_element = listb[mid_len]
    if n == middle_element:
        print("Achei.")
        break
    else:
        if n < middle_element:
            listb = listb[0: mid_len]
            print(f"Nova lista n <:{listb}")
        elif n > middle_element:
            listb = listb[mid_len:]
            print(f"Nova lista n >: {listb}")

print(f"O número digitado foi {n}.")
print(f"O número restante na lista é {listb}.")
'''