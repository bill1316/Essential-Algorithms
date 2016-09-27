# #suppose we have a basic class containing a single data field:
# class ListNode:
#     def __init__(self,data):
# #We can create several instances of this class ,each storing data of our choosing.In the following example , we create three instances ,each storing an interger value:
#         a=ListNode(11)
#         b=ListNode(52)
#         c=ListNode(18)


#Now suppose we add a second data field to the ListNode class:
class ListNode:
    def __init__(self,data=None, next=None):
        self.data=data
        self.next=next

    def __str__(self):
        return str(self.data)
#The three object would now have a second data field initialized with a null reference
        a.next=b
        b.next=c
        b=None
        c=None
        print(a.data)
        print(a.next.data)
        print(a.next.next.data)

a=ListNode(11)
b=ListNode(52)
c=ListNode(18)
#Traversing a linked list
def traversal(head):
    curNode=head
     while curNode is not None:
        print curNode.data
        curNode=curNode.next

#Searching a linked list
def unorderedSearch(head,target):
    curNode=head
    while curNode is not None and curNode.data !=target:
        curNode=curNode.next
    return curNode is not None


#Prepending Nodes
new=listNode(29)
newNode.next=head
head=newNode
#Removing a node from a linked list
predNode=None
curNode=head
while curNode is not None and curNode.data !=target:
    predNode=curNode
    curNode=curNode.next

if curNode is not None:
    if curNode is head:
        head=curNode.next
    else:
        predNode.next=curNode.next
