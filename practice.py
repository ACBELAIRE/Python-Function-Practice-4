
#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(a,b,c):
        print (max([a,b,c]))

max_num(1231,134,23)


#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
        #if the list is empty return 0
    if len(list) == 0:
        return 0
        #multiplication will start with the first number in the list
    prod = list[0]
        # is the length of the list is greater than onem iterated thru each item in the list  from the first to the end 
        # make the product equal to  the first element times by each element of x as it iterates
    if len(list)> 1:
        for x in list[1:]:
            prod = prod * x
        #after it is completed iteration return the product of the list
    return prod

print(mult_list([5,7,8,10,14]))


#Write a Python function called rev_string() to reverse a string.

def rev_string(str):
    return str[::-1]

print(rev_string('Hello'))
print(rev_string('It is a String Reversed'))

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(a,b,c):
    if a >= b and a <= c :
        return True
    else:
        return False

print(num_within(3,6,9))
print(num_within(1,-1,2))
