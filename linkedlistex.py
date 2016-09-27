class Node:
    def __init__(self,value=None, next=None):
        self.value=value
        self.next=next

    def __str__(self):
       return str(self.value)

#create nodes
mynode1=Node("first")
mynode2=Node("second")
mynode3=Node("third ")
mynode4=Node("fourth")
mynode5=Node("fifth")
myNodes=mynode1,mynode2,mynode3,mynode4,mynode5
print myNodes



#link them
mynode1.next=mynode2
mynode2.next=mynode3


#Iterate through list
def Iterate(iterating):
    while (iterating):
        print iterating.value
        iterating=iterating.next
    return iterating

Iterate(mynode1)


#Iterate Cell
def FindCell(iterating,target):
    while(iterating):
        if(iterating==target):
            print iterating
        iterating=iterating.next
    return iterating

FindCell(mynode1,mynode3)


#find the cell before

def FindCellBefore( iterate, target)
// If the list is empty, the target value isn't
present.
If (top == null) Return null
// Search for the target value.
While (top.Next != null)
If (top.Next.Value == target) Then Return top
top = top.Next
End While
// If we get this far, the target is not in the
list.
Return null
End FindCellBefore


#Using Sentinels


Cell: FindCellBefore(Cell: top, Value: target)
// Search for the target value.
While (top.Next != null)
If (top.Next.Value == target) Then Return top
top = top.Next
End While
// If we get this far, the target is not in the
list.
Return null
End FindCellBefore

#Adding Cells at the Beginning

AddAtBeginning(Cell: top, Cell: new_cell)
new_cell.Next = top.Next
top.Next = new_cell
End AddAtBeginning


#Adding Cells at the End

AddAtEnd(Cell: top, Cell: new_cell)
// Find the last cell.
While (top.Next != null)
top = top.Next
End While
// Add the new cell at the end.
top.Next = new_cell
new_cell.Next = null
End AddAtEnd

#Inserting Cells After Other Cells
after_me:
InsertCell(Cell: after_me, Cell: new_cell)
new_cell.Next = after_me.Next
after_me.Next = new_cell
End InsertCell

#Deleting Cells

DeleteAfter(Cell: after_me)
after_me.Next = after_me.Next.Next
End DeleteAfter


#Doubly Linked Lists
InsertCell(Cell: after_me, Cell: new_cell)
// Update Next links.
new_cell.Next = after_me.Next
after_me.Next = new_cell
// Update Prev links.
new_cell.Next.Prev = new_cell
new_cell.Prev = after_me
End InsertCell

#Sorted Linked Lists
// Insert a cell into a sorted singly linked list.
InsertCell(Cell: top, Cell: new_cell)
// Find the cell before where the new cell
belongs.
While (top.Next != null) And (top.Next.Value <
new_cell.Value)
top = top.Next
End While
// Insert the new cell after top.
new_cell.Next = top.Next
top.Next = new_cell
End InsertCell
