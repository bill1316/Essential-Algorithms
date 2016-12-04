numbers=[1,4,543,22,345,23423425424,53,2,6,7,8,9,32,33,34,35,36,56,58,]
even=[]
odd=[]
while len(numbers)>0:
    number=numbers.pop()
    if(number %2==0):
        even.append(number)
    else:
        odd.append(number)
print "Even numbers=",even
print "Odd Numbers=",odd
