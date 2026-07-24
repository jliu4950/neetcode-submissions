from collections import defaultdict
class ListNode:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.pre=None
        self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.dic=defaultdict(int)
        self.head=ListNode(-1,-1)
        self.tail=ListNode(-1,-1)
        self.head.next=self.tail
        self.tail.pre=self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        p=self.dic[key]
        self.remove(p)
        self.add_to_tail(p)

        return p.val

    def put(self, key: int, value: int) -> None:#put 一个已有 key，也算最近访问。
        #if exist
        if key in self.dic:
            p=self.dic[key]
            p.val=value 
            self.remove(self.dic[key])
            self.add_to_tail(self.dic[key])
            return #否则后面会继续创建节点
        #if out of capacity
        if len(self.dic)==self.capacity:
            del self.dic[self.head.next.key]
            self.remove(self.head.next)
        #put new
        p=ListNode(key,value)
        self.dic[key]=p
        self.add_to_tail(p)

    def remove(self,p):
        next_p=p.next
        pre_p=p.pre

        pre_p.next=next_p
        next_p.pre=pre_p

        p.next=None
        p.pre=None

    def add_to_tail(self,p):
        pre_p=self.tail.pre
        p.pre=pre_p
        p.next=self.tail
        pre_p.next=p
        self.tail.pre=p