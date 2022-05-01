# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getArr(node):
    arr = []
    while True:
        arr.append(node.val)
        if(node.next == None):
            break
        node = node.next
    arr.reverse()
    return arr


def sumTwoNumber(num1, num2):
    num1 = ''.join(map(str, num1))
    num2 = ''.join(map(str, num2))
    return int(num1) + int(num2)


def makeList(num):
    num = str(num)
    result = None
    for x in num:
        result = ListNode(int(x), next=result)
        print(result)
    return result


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = getArr(l1)
        num2 = getArr(l2)
        total = sumTwoNumber(num1, num2)
        return makeList(total)
