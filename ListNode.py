#suppose we have a basic class containing a single data field:
class ListNode:
    def __init__(self,data):
#We can create several instances of this class ,each storing data of our choosing.In the following example , we create three instances ,each storing an interger value:
       a=ListNode(11)
       b=ListNode(52)
       c=ListNode(18)
#Now suppose we add a second data field to the ListNode class:
class ListNode:
    def __init__(self,data):
        self.data=data
        self.next=None
#The three object would now have a second data field initialized with a null refernce        
        a.next=b
        b.next=c
        b=None
        c=None
        print(a.data)
        print(a.next.data)
        print(a.next.next.data)
