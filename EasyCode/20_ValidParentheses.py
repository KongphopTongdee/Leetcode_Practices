# class Solution:
#     def isValid(self, s: str) -> bool:
#         ''' Create the 2 pointer code for search the same bracket and delete it
#         '''
#         # listOfS = list( s )
#         # left = 0
#         # right = len( s ) - 1
       
#         # while ( left < right ):
            
#         #     if( listOfS[ left ] == "("  and listOfS[ right ] == ")" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
#         #     elif( listOfS[ left ] == ")"  and listOfS[ right ] == "(" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
            
#         #     elif( listOfS[ left ] == "["  and listOfS[ right ] == "]" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
#         #     elif( listOfS[ left ] == "]"  and listOfS[ right ] == "[" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
            
#         #     elif( listOfS[ left ] == "{"  and listOfS[ right ] == "}" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
#         #     elif( listOfS[ left ] == "}"  and listOfS[ right ] == "{" ):
#         #         listOfS.pop( right )
#         #         listOfS.pop( left )
#         #         # Update the right value again for new loop
#         #         right = len( listOfS ) - 1
                
#         #     else:
#         #         right -= 1
       
#         # ans = self.checkTheAnswer( listOfS )
    
#         # return ans
    
#     # def checkTheAnswer( self, answer ):
#     #     '''
#     #     '''
#     #     if( len( answer ) != 0 ):
#     #         return False
#     #     else:
#     #         return True
    
#         ans = False
#         listOfS = list( s )
#         fixPointer = 0
#         rightPointer = fixPointer + 1
        
#         while( fixPointer < rightPointer ):
#             if( len( listOfS ) <= 1 ):
#                 break
#             elif( listOfS[ fixPointer ] == "("  and listOfS[ rightPointer ] == ")" ):
#                 listOfS.pop( rightPointer )
#                 listOfS.pop( fixPointer )
#                 fixPointer = 0
#                 rightPointer = fixPointer + 1
#             elif( listOfS[ fixPointer ] == "{"  and listOfS[ rightPointer ] == "}" ):
#                 listOfS.pop( rightPointer )
#                 listOfS.pop( fixPointer )
#                 fixPointer = 0
#                 rightPointer = fixPointer + 1
#             elif( listOfS[ fixPointer ] == "["  and listOfS[ rightPointer ] == "]" ):
#                 listOfS.pop( rightPointer )
#                 listOfS.pop( fixPointer )
#                 fixPointer = 0
#                 rightPointer = fixPointer + 1
#             else:
#                 fixPointer += 1
#                 rightPointer += 1
#                 if ( rightPointer > len( listOfS ) - 1 ):
#                     break
                
            
#         ans = self.checkTheAnswer( listOfS )
            
#         return ans
    
#     def checkTheAnswer( self, answer ):
#         '''
#         '''
#         if( len( answer ) != 0 ):
#             return False
#         else:
#             return True
        
    
# checkAns = Solution()
# print( checkAns.isValid( "()" ) )                   # Expectation True
# print( checkAns.isValid( "()[]{}" ) )               # Expectation True
# print( checkAns.isValid( "(]" ) )                   # Expectation False
# print( checkAns.isValid( "([)]" ) )                 # Expectation False
# print( checkAns.isValid( "{[]}" ) )                 # Expectation True
# print( checkAns.isValid( "((" ) )                   # Expectation False


# Solution with quick algorithms

class Solution(object):
    def isValid(self, s):
        stack = [] # create an empty stack to store opening brackets
        for c in s: # loop through each character in the string
            if c in '([{': # if the character is an opening bracket
                stack.append(c) # push it onto the stack
            else: # if the character is a closing bracket
                # Stack[-1]: mean select the last element of the list
                if not stack or ( c == ')' and stack[-1] != '(' ) or ( c == '}' and stack[-1] != '{' ) or ( c == ']' and stack[-1] != '[' ):
                    return False # the string is not valid, so return false
                # The pop function will pop the last element in the list
                stack.pop() # otherwise, pop the opening bracket from the stack
        return not stack # if the stack is empty, all opening brackets have been matched with their corresponding closing brackets,
                         # so the string is valid, otherwise, there are unmatched opening brackets, so return false
                         
checkAns = Solution()
# print( checkAns.isValid( "()" ) )                   # Expectation True
# print( checkAns.isValid( "()[]{}" ) )               # Expectation True
# print( checkAns.isValid( "(]" ) )                   # Expectation False
# print( checkAns.isValid( "([)]" ) )                 # Expectation False
# print( checkAns.isValid( "{[]}" ) )                 # Expectation True
print( checkAns.isValid( "((" ) )                   # Expectation False