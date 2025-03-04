# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class MethodLinkList:
#     def __init__( self ):
#         self.headVal = None
        
#     def listPrint( self ):
#         printVal = self.headVal
#         while printVal is not None:
#             print (printVal.val)
#             printVal = printVal.next
            
#     def append( self, data ):
#         newNode = ListNode( data )
#         if self.headVal is None:
#             self.headVal = newNode
#             return
#         lastNode = self.headVal
#          # This while is to find the last element, if it not the list element it will continue update the last node to the last element
#         while lastNode.next:
#             lastNode = lastNode.next
#         # Update to the last element
#         lastNode.next = newNode
        
#     def insertNumInLinkList( self, data ):
#         '''
#         '''
#         currentLinkList = self.headVal
#         try:
#             while( currentLinkList.next is not None ):
#                 if( ( currentLinkList.val <= data ) and ( currentLinkList.next.val > data ) ):
#                     newData = ListNode( data )
#                     nextData = currentLinkList.next
#                     currentData = currentLinkList
#                     newData.next = nextData
#                     currentData.next = newData
#                     break
#                 currentLinkList = currentLinkList.next
#             if( currentLinkList.next is None ):
#                 newData = ListNode( data )
#                 nextData = currentLinkList.next
#                 currentData = currentLinkList
#                 newData.next = nextData
#                 currentData.next = newData
#         except:
#             if( currentLinkList is None ):
#                 newData = ListNode( data )
#                 self.headVal = newData
            
            
        
# class Solution:
#     def mergeTwoLists( self, list1, list2 ):
#         '''
#         '''
    
#         list1LinkList = MethodLinkList()
        
#         if( ( len( list1 ) == 0 ) and ( len( list2 ) == 0 ) ):
#             list1LinkList = []
#             return list1LinkList
        
#         # Method for create the link list
#         for _ in list1:
#             list1LinkList.append( _ )
            
#         # list1LinkList.listPrint()
            
#         # Method for merged the link list
#         for numInList in list2:
#             list1LinkList.insertNumInLinkList( numInList )
               
#         list1LinkList.listPrint()
            
#         return list1LinkList
              
        
        
# checkAns = Solution()
# checkAns.mergeTwoLists( [ 1, 2, 4 ], [ 1, 3, 4 ] )              # Expected [ 1, 1, 2, 3, 4, 4 ]
# checkAns.mergeTwoLists( [], [] )                                # Expected []
# checkAns.mergeTwoLists( [], [ 0 ] )                             # Expected [ 0 ]



# Reference website for tutorial: https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm



# Solution of this exercise

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MethOfLinkList:
    def __init__( self, listOfLinkList ):
        self.headVal = None
        
        for _ in listOfLinkList:
            self.appendLinkList( _ )
        
    def appendLinkList( self, data ):
        current = self.headVal
        if( self.headVal == None ):
            newNode = ListNode( data )
            self.headVal = newNode
            return
        while( current.next != None ):
            current = current.next
        newNode = ListNode( data )
        current.next = newNode
        
    def returnLinkList( self ):
        return self.headVal
        
    def displayLinkList( self ):
        current = self.headVal
        while( current.next != None ):
            print( current.val )
            current = current.next
        if( current.next == None ):
            print( current.val )
        

class Solution:
    def mergeTwoLists( self, list1, list2 ):
        dummy = ListNode()
        tail = dummy
        # The method is compared every element in the list1 and list2
        # While in the list is not empty for compare the two
        while ( list1 and list2 ):    
            # Compare the value          
            if list1.val < list2.val:
                tail.next = list1
                # Update list1 pointer
                list1 = list1.next
            else:
                # List2 gonna be inserted
                tail.next = list2
                list2 = list2.next
            # Update the tail conner which node we insert into our list
            tail = tail.next
        
        # Find the non-empty list and inserted it the end of our result( only one of then can be non-null )
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
    
checkAns = Solution()
# checkAns.mergeTwoLists( [ 1, 2, 4 ], [ 1, 3, 4 ] )              # Expected [ 1, 1, 2, 3, 4, 4 ]
linkList1 = MethOfLinkList( [ 1, 2, 4 ] )
linkList1 = linkList1.returnLinkList()
linkList2 = MethOfLinkList( [ 1, 3, 4 ] )
linkList2 = linkList2.returnLinkList()
checkAns.mergeTwoLists( linkList1, linkList2 )              
# checkAns.mergeTwoLists( [], [] )                                # Expected []
# checkAns.mergeTwoLists( [], [ 0 ] )                             # Expected [ 0 ]