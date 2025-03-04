# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution:
#     def __init__( self ):
#         self.answerValue = 0
#     def reverseNumber( self, valueReverse ):
#         return valueReverse[::-1]
    
#     def convertListToNum( self,valueConvert ):
#         return int( ''.join( map( str, valueConvert ) ) )
    
#     def convertNumToList( self,valueConvert ):
#         return list( map( int, str( valueConvert ) ) )
    
#     def sumNumber( self, n1, n2 ):
#         return n1 + n2
    
#     def addTwoNumbers( self, l1, l2 ):
#         firstValue = self.reverseNumber( l1 )
#         secondValue = self.reverseNumber( l2 )
#         firstValue = self.convertListToNum(firstValue)
#         secondValue = self.convertListToNum(secondValue)
#         answer = self.sumNumber( firstValue, secondValue )
#         answer = self.convertNumToList( answer )
#         self.answerValue = self.reverseNumber( answer )
#         return self.answerValue
    
#     def showOutput( self ):
#         print( self.answerValue )
    

# Answer = Solution()
# # Answer.addTwoNumbers( [ 2, 4, 3 ], [ 5, 6, 4 ] )
# # Answer.addTwoNumbers( [ 0 ], [ 0 ] )
# Answer.addTwoNumbers( [ 9, 9, 9, 9, 9, 9, 9 ], [ 9, 9, 9, 9 ] )
# Answer.showOutput()


# LeetCode Answer
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    
Solution.addTwoNumbers( [2,4,3], [5,6,4] )