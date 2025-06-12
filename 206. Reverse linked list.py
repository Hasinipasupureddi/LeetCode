class Solution(object):
    def reverseList(self, head):
        prev=None
        cur=head
        while cur is not None:
            nextnode=cur.next
            cur.next=prev
            prev=cur
            cur=nextnode
        self.head=prev
        return prev
