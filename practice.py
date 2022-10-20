
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


    #The function accepts the number, beginning of range, and end of range (inclusive) as arguments.

    #Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.


#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
  #The function accepts the number n, the number of rows to print

    #Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.
    #  Each number is the two numbers above it added together.

triangle = [[1],[1,1]]

def pascal(n):
    #               #If the row is less than 1 then the row doesnt exist and is invalif

    if n < 1:
        print( "Invalid row")
                    #If the row is equal to 1 then print the first element in the triangle
    elif n == 1:
        print(triangle[0])
                    #
    else:
                    #If row is 
        row_number = 2
                        #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
                         #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
                        #first number is 1
        if i == 0:
          row.append(1)
                        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
                        #last number is 1
        else:
          row.append(1)
          triangle.append(row)
          row_number += 1

                        #print triangle
    for row in triangle:
      print(row)

pascal(0)


pascal(2)

pascal(4)