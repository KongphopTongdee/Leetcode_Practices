# answer = "     -32"
# # answer = int( answer )
# # print(answer)
# for i in answer:
#     if( i.isdigit() == True ):
#         print(True)
#     else:
#         print(False)

# import numpy as np
# testans = -999999999999999999999999999999999
# if ( testans < -(2**31) ):
#     ans = -(2**31)
# print(ans)

# answer = 'words and +-987'
# for i in answer:
#     if( i.isalpha() == True ):
#         print( 'Checking alphabet', True )
#     else:
#         print( 'Checking alphabet', False )
# for i in answer:
#     if( i.isdigit() == True ):
#         print( 'Checking integer', True )
#     else:
#         print( 'Checking integer', False )

# test = '+-12'
# testAns = int( test )
# print(testAns)


# testList = ['Space', 'Space', 'Space', 'Mark', True, 'Space', True, True, True]

# if( ( testList[ 0 ] == 'Space' ) and ( testList[ 0 - 1 ] == True ) and ( 0 != 0 ) ):
#     print(True)
        
# a = (7, 4, 9)
        
# ans = sum(a)
# print(ans)

# from itertools import combinations

# original_list = [1, 2, 3, 4, 5, 6]

# # Generate all combinations of 3 elements
# combinations_list = list( combinations( original_list, 3 ) )

# print( 'The amount of combination',len(combinations_list) )

# print(combinations_list)

# num = [0,0,0,0,0,0]

# indexNums = [ i for i in range( len( num ) ) ]

# print(indexNums)




# original_list = [[1, 2, 3], [2, 1, 3], [4, 5, 6], [6, 5, 4], [7, 8, 9]]

# # Convert each sublist to a tuple and use a set to keep track of unique tuples
# unique_set = set(tuple(sorted(sublist)) for sublist in original_list)

# # Convert back to a list of lists
# unique_list = [list(sublist) for sublist in unique_set]

# print(unique_list)







# from itertools import permutations

# original_list = [[1, 2, 3], [2, 1, 3], [4, 5, 6], [6, 5, 4], [7, 8, 9]]

# # Convert each sublist to a tuple and use a set to keep track of unique tuples
# unique_set = set(tuple(sublist) for sublist in permutations(original_list[0]))

# # Convert back to a list of lists
# unique_list = [list(sublist) for sublist in unique_set]

# print(unique_list)

# testList = [[1,2],[3,4],[5,6]]
# for i in testList[0]:
#     print(i)

# testList = [ 1, 2, 3, 4, 3, 2, 1, 4, 5]
# reveseList = testList[::-1]
# print(reveseList)



# my_list = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# # Find the highest value in the list
# max_value = max(my_list)
# # Find the index of the highest value
# index_of_max_value = my_list.index(max_value)
# print("Highest value:", max_value)
# print("Index of highest value:", index_of_max_value)


# test = [ 1,2,3,4,5,6 ]

# for i in range(len(test)):
#     if( test[ i ] == 2 or test[ i ] == 4 ):
#         print( f'{test[i]}:',True)
#     else:
#         print(f'{test[i]}:',False)

# stack = [ '()', '8' ]
# print( stack[-1] )

# test = "(())()"

# def flipTheBracket( inputString ):
#     flipString = ""
#     inputString = inputString[::-1]
#     for charBracket in inputString:
#         if charBracket == "(":
#             flipString += ")"
#         elif charBracket == ")":
#             flipString += "("
            
#     return( flipString )
    
# print( flipTheBracket( test ) )

# test = "((()))"

# print( test )

# left = 0
# right = left + 1
# testList = list( test )
# # print( testList )

# while ( right < len( testList ) ):
#     if ( testList[ left ] == "(" and testList[ right ] == "(" ) :
#         left += 1
#     else:
#         testList.pop( right )
#         testList.pop( left )
#         testList.append( "(" )
#         testList.append( ")" )
#         break

# ans = ''.join( testList )
# print( ans )




# test = "((()))()()"

# def algorithmsAppendBack( inputStrBack ):
#     '''
#     '''
#     inputList = list( inputStrBack )
#     right = len( inputList ) - 1 
#     left = right - 1 
#     stack = 0
    
#     while( left >= 0 ):
#         if( inputList[ right ] == ")" and inputList[ left ] == "(" and stack == 0 ):
#             inputList.pop( len( inputList ) - 1 )
#             inputList.pop( len( inputList ) - 1 )
#             stack += 1
#             right -= 2
#             left -= 2
#         elif( inputList[ right ] == ")" and inputList[ left ] == ")" ):
#             inputList.insert( right, "()" )
#             break
#         else:
#             left -= 1
#             right -= 1
        
#     inputList = ''.join( inputList )
#     return inputList
 
# print( test )
# print( algorithmsAppendBack( test ) )     


# test1 = "((()))" 
# test2 = "(())()"
# test3 = "()()()"

# if( "(())" in test3 ):
#     print( "Yes" )
# else:
#     print( "No" )

# test2 = [ "(","(","()",")",")" ]
# test2 = ''.join(test2)
# print( test2 )

# testList = list( test )
# print('First testList',testList)
# testList.pop(len( testList ) - 1)
# testList.pop(len( testList ) - 1)
# print('Second testList',testList)

# listNaKrub = [ 6, 5, 4, 3, 2, 1 ]
# listNaKrub.insert( 2, "Hello" )
# print(listNaKrub)

# Python Singly link list

# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None

# list1 = SLinkedList()
# list1.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")
# # Link first Node to second node
# list1.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

#####################################################################################################
# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None

#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#         # Print the currnt value
#          print (printval.dataval)
#          # Update the print value to print next
#          printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# # Link first Node to second node
# list.headval.nextval = e2

# # Link second Node to third node
# e2.nextval = e3

# list.listprint()

#####################################################################################################
# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None

# class SLinkedList:
#    def __init__(self):
#       self.headval = None
# # Print the linked list
#    def listprint(self):
#       printval = self.headval
#       while printval is not None:
#          print (printval.dataval)
#          printval = printval.nextval
#    def AtBegining(self,newdata):
#         NewNode = Node(newdata)

#         # Update the new nodes next val to existing node
#         NewNode.nextval = self.headval
#         self.headval = NewNode

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Wed")

# list.headval.nextval = e2
# e2.nextval = e3

# list.AtBegining("Sun")
# list.listprint()

#####################################################################################################
# class Node:
#    def __init__(self, dataval=None):
#       self.dataval = dataval
#       self.nextval = None
# class SLinkedList:
#     def __init__(self):
#         self.headval = None

#     # Function to add node
#     def Inbetween(self,middle_node,newdata):
#         if middle_node is None:
#             print("The mentioned node is absent")
#             return

#         NewNode = Node(newdata)
#         NewNode.nextval = middle_node.nextval
#         middle_node.nextval = NewNode

#     # Print the linked list
#     def listprint(self):
#         printval = self.headval
#         while printval is not None:
#             print (printval.dataval)
#             printval = printval.nextval

# list = SLinkedList()
# list.headval = Node("Mon")
# e2 = Node("Tue")
# e3 = Node("Thu")

# list.headval.nextval = e2
# e2.nextval = e3

# list.Inbetween(list.headval.nextval,"Fri")

# list.listprint()

#####################################################################################################
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Example usage:
# if __name__ == "__main__":
#     # Create a new singly linked list
#     sll = SinglyLinkedList()

#     # Append some elements to the list
#     sll.append(1)
#     sll.append(2)
#     sll.append(3)
#     sll.append(4)

#     # Display the elements in the list
#     sll.display()

#####################################################################################################
# # Write by myself
# class Node:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
# class TestMethodLinkList:
#     def __init__( self, head=None ):
#         self.headVal = head
        
#     def printLink( self ):
#         current = self.headVal
#         # Get in current and read every next data
#         while current.next != None:
#             print( current.val )
#             # Get the next value on the Node to continue the link list
#             current = current.next
            
#     def convertListToLinkList( self, list1 ):
#         '''
#         '''
#         def append( data ):
#             newNode = Node( data )
#             if self.headVal is None:
#                 self.headVal = newNode
#                 return
#             lastNode = self.headVal
#             # This while is to find the last element, if it not the list element it will continue update the last node to the last element
#             while ( lastNode.next != None ):
#                 lastNode = lastNode.next
#             # Update to the last element
#             lastNode.next = newNode
        
#         for _ in list1:
#             answer = append( _ )

#         return answer
    
#     def insertNumberLinkList( self, data ):
#         '''
#         '''
#         currentLinkList = self.headVal
#         while( currentLinkList.next is not None ):
#             # print( currentLinkList.val )
#             # if( ( currentLinkList.val < data ) and ( currentLinkList.next.val >= data ) ):
#             if( ( currentLinkList.val <= data ) and ( currentLinkList.next.val > data ) ):
#                 newData = Node( data )
#                 nextData = currentLinkList.next
#                 currentData = currentLinkList
#                 newData.next = nextData
#                 currentData.next = newData
#                 break
#             currentLinkList = currentLinkList.next
#         if( currentLinkList.next is None ):
#             newData = Node( data )
#             nextData = currentLinkList.next
#             currentData = currentLinkList
#             newData.next = nextData
#             currentData.next = newData
        

# test1 = Node( 0 )
# test2 = Node( 5 )
# test3 = Node( 10 )
# test4 = Node( 15 )
# test5 = Node( 20 )

# testList = [ 0, 5, 10, 15, 20 ]
# testList2 = [ 3, 4, 9, 12, 17 ]


# # Test to merge the data and address in singly link list
# # testMerge = TestMethodLinkList()
# # test1.next = test2
# # test2.next = test3
# # test3.next = test4
# # test4.next = test5
# # testMerge.headVal = test1
# # testMerge.printLink()

# # Test to convert list into singly link list
# testMerge = TestMethodLinkList()
# testMerge.convertListToLinkList( testList )
# for _ in testList2:
#     testMerge.insertNumberLinkList( _ )
# testMerge.printLink()
    

# # They print in to 2 number because they get the first element and last element

# listTest = []

# if( len(listTest) == 0 ):
#     print( True )
# else:
#     print( False )

# testValue = ["a","b","c"]
# print(str(testValue[0::]))

# car = [ 'birds', 'ants', 'dogs', 'cats' ]
# removeOut = [ 'dogs' ,'cats' ]
# # answer = car.remove( removeOut[0::] )
# del car[removeOut]
# print(car)


# def singleNumber( nums ):
#     result = 0
#     for n in nums:
#         result ^= n             # same as: result = result ^ value -> ^ mean or
        
#     print( result )
#     return result

# Explanation:
# 10 in binary: 1010
# 6 in binary: 0110
# Bitwise XOR (^) compares each bit:
# 1 ^ 0 → 1
# 0 ^ 1 → 1
# 1 ^ 1 → 0
# 0 ^ 0 → 0
# Result: 1100 (which is 12 in decimal)

# singleNumber( [2,2,1] )
# singleNumber( [4,1,2,1,2] )
# singleNumber( [1] )

