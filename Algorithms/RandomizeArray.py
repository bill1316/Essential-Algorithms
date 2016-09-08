'''
RandomizeArray(String: array[])
Integer: max_i = <Upper bound of array>
For i = 0 To max_i - 1
// Pick the item for position i in the array.
Integer: j = <pseudorandom number between i and max_i inclusive>
<Swap the values of array[i] and array[j]>
Next i
End RandomizeArray
'''


def randomize(list): 
    max_i = list[len(list) - 1] 
    print(list)
    print(max_i)
    print(len(list))
    i = 0
    for i in range(len(list)):
        j = random.randint(i,(len(list) - 1))
        temp = list[i]
        list[i] = list[j]
        list[j] = temp
    return list
