# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MethodLinkList:
    def __init__( self ):
        self.headVal = None
        self.countLinkList = 0
    
    def displayLinkList( self ):
        current = self.headVal
        if( current == None ):
            print( "Value of this link is None" )
            return
        while( current.next != None ):
            print( "Value of this link", current.val )
            current = current.next
        if( current.next == None ):
            print( "Value of this link", current.val )
            
    def appendLinkList( self, data ):
        newNode = ListNode( data )
        current = self.headVal
        if( self.headVal == None ):
            self.headVal = newNode
            self.countLinkList += 1
            return
        while( current.next != None ):
            current = current.next
        current.next = newNode 
        self.countLinkList += 1  
        
    def reverseRemoveLinkList( self, indexNumber ):
        current = self.headVal
        # We select the position so we need to plus 1, but if we select the index you don't need to plus 
        positionRemove = self.countLinkList - indexNumber - 1
        currentPosition = 0
        while( currentPosition != positionRemove ):
            if( current.next != None ):
                current = current.next
                currentPosition += 1
            else:
                self.headVal = None
                return
        if( currentPosition == positionRemove ): 
            removeNode = current.next
            continueNode = removeNode.next
            current.next = continueNode
            
class AnsLinkList():    
    def __init__( self ):
        self.headOfLink = 0
        
    @staticmethod
    def countVariable( linkList ):
        countNum = 0
        while( linkList.next != None ):
            countNum += 1
            linkList = linkList.next
        if( linkList.next == None ):
            countNum += 1
        return countNum
    
    def removeLinkList( self, head, n ):
        
        current = head
        countNumElement = AnsLinkList.countVariable( head )
        positionRemove = countNumElement - n - 1
        currentPosition = 0
        
        if( ( positionRemove == -1 ) and ( n == countNumElement ) ):
            head = current.next
            return head
        
        while( currentPosition != positionRemove ):
            if( current.next != None ):
                current = current.next
                currentPosition += 1
            # This condition will correct when is only one element in link list
            elif( ( current.next == None ) and ( countNumElement == 1 ) ):
                head = None
                return head
        
        if( currentPosition == positionRemove ): 
            removeNode = current.next
            continueNode = removeNode.next
            current.next = continueNode
            
        return head
    
    @staticmethod
    def displayTheAnswer( ansOfLinkList ):
        current = ansOfLinkList
        if( current == None ):
            print( "Value of this link is None" )
            return
        while( current.next != None ):
            print( current.val )
            current = current.next
        if( current.next == None ):
            print( "Value of this link", current.val )
        
        
class Solution:
    def removeNthFromEnd( self, head, n ):
        '''
        '''
        answer = 0
        # First Link
        firstLink = MethodLinkList()
        for _ in head:
            firstLink.appendLinkList( _ )
        # firstLink.reverseRemoveLinkList( n )
        # firstLink.displayLinkList()
        
        # Another Link 
        ansLink = AnsLinkList()
        answer = ansLink.removeLinkList( firstLink.headVal, n )
        AnsLinkList.displayTheAnswer( answer )
        
        return answer
        
        
checkAns = Solution()
# checkAns.removeNthFromEnd( [1,2,3,4,5], 2 )
# checkAns.removeNthFromEnd( [1], 1 )
# checkAns.removeNthFromEnd( [1,2], 1 )
checkAns.removeNthFromEnd( [1,2], 2 )

# Quick answer for this question:
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next