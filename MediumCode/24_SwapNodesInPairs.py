class ListNode:
    def __init__( self, val = 0, next = None ):
        self.val = val
        self.next = next
        
class CreateLinkForTest:
    def __init__( self ):
        self.head = None
        
    def appendLinkList( self, num ):
        currentListNode = self.head
        
        if( self.head == None ):
            self.head = ListNode( val = num )
            return
        
        while( currentListNode.next != None ):
            currentListNode = currentListNode.next
        currentListNode.next = ListNode( val = num )
        
    
    def showLinkList( self ):
        currentListNode = self.head
        strLinkList = ''
        
        while( currentListNode.next != None ):
            # print( currentListNode.val )
            strLinkList += str( currentListNode.val )
            strLinkList += ' -> '
            currentListNode = currentListNode.next
        
        if( currentListNode.next == None ):
            # print( currentListNode.val )
            strLinkList += str( currentListNode.val )
            
        print( strLinkList )
  
    # Spare code for return the LinkList
    def returnOutLinkList( self ):
        return self.head

# Method for the answer 
class Solution:
    
    def __init__( self ):
        self.head = None
    
    # Staticmethod = change the function in the class into def function
    @staticmethod
    def checkLinkList( head ):
        currentHead = head
        number = 0
        while( currentHead.next != None ):
            number += 1
            currentHead = currentHead.next
            
        if( currentHead.next == None ):
            number += 1
            
        return number
    
    @staticmethod
    def showLinkList( linkForCheck ):
        currentListNode = linkForCheck
        strLinkList = ''
        
        while( currentListNode.next != None ):
            # print( currentListNode.val )
            strLinkList += str( currentListNode.val )
            strLinkList += ' -> '
            currentListNode = currentListNode.next
        
        if( currentListNode.next == None ):
            # print( currentListNode.val )
            strLinkList += str( currentListNode.val )
            
        print( strLinkList )
        
       ###################################################################### The last way ( Too much runtime ) 
    def appendLinkList( self, num ):
        currentListNode = self.head
        
        if( self.head == None ):
            self.head = ListNode( val = num )
            return
        
        while( currentListNode.next != None ):
            currentListNode = currentListNode.next
        currentListNode.next = ListNode( val = num )
        
        
    def appendInList( self, linkList ):
        listOfLink = []
        currentLink = linkList
        
        if( currentLink == None ):
            return listOfLink
        
        while( currentLink.next != None ):
            listOfLink.append( currentLink.val )
            currentLink = currentLink.next
        if( currentLink.next == None ):
            listOfLink.append( currentLink.val )
        
        return listOfLink
    
    def swapPairs( self, head ):
        listOfLinkList = self.appendInList( head )
        newListSwap = [ listOfLinkList[ idx + 1 ] if idx % 2 == 0 else listOfLinkList[ idx - 1 ] for idx in range( len( listOfLinkList ) ) ] 
        for value in newListSwap:
            self.appendLinkList( value )
           
        Solution.showLinkList( self.head )
        
        
        
       
        
        
        
        
        
    


def listSeperate( listTest ):
    classLinkList = CreateLinkForTest()
    
    for number in listTest:
        classLinkList.appendLinkList( number )
        
    #   Show link list
    classLinkList.showLinkList()
    
    return classLinkList.head









changeToLinkList = listSeperate( [ 1, 2, 3, 4 ] )
# changeToLinkList = listSeperate( [ ] )
# changeToLinkList = listSeperate( [ 1 ] )

getAns = Solution()
# getAns.swapPairs( [ 1, 2, 3, 4 ] )            # Expect [ 2, 1, 4, 3 ]
getAns.swapPairs( changeToLinkList )

# getAns.swapPairs( [ ] )                       # Expect [ ]
# getAns.swapPairs( changeToLinkList )

# getAns.swapPairs( [ 1 ] )                     # Expect [ 1 ]
# getAns.swapPairs( changeToLinkList )
