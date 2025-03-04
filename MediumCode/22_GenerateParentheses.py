# class Solution:
#     def generateParenthesis( self, n: int ) -> list[ str ]:
#         '''
#         '''
#         answer = []
#         invertAns = []
#         collectAns = []
        
#         startBracket = self.generateBasic( n )
#         endBracket = self.limitBracket( n )
#         collectAns.append( startBracket )
        
#         while( startBracket != endBracket ):
#             previousBracket = startBracket
#             startBracket = self.algorithmsExtract( startBracket ) 
#             collectAns.append( startBracket )
#             invertBraket = self.algorithmsInvert( startBracket )
#             invertAns.append( invertBraket )
#             if( startBracket == endBracket ):
#                 for _ in range( n - 2 ):
#                     previousBracket = self.algorithmsAppendBack( previousBracket )
#                     collectAns.append( previousBracket )
#                     invertBraket = self.algorithmsInvert( previousBracket )
#                     invertAns.append( invertBraket )

#         setInvertAns = set( invertAns )
#         setCollectAns = set( collectAns )
#         compareAns = setInvertAns - setCollectAns
#         compareAns = list( compareAns )
        
#         answer.extend( setCollectAns )
#         answer.extend( compareAns )

#         return answer
        
#     def limitBracket( self, numBracket ):
#         '''
#         '''
#         strAns = []
#         for _ in range( numBracket ):
#             strAns.append( "()" )
#         strAns = ''.join( strAns )
#         return strAns
        
#     def generateBasic( self, numBracket ):
#         '''
#         '''
#         listOut = []
#         for iteration in range( 2 ):
#             for _ in range( numBracket ):
#                 if iteration == 0:
#                     listOut.append( '(' )
#                 elif iteration == 1:
#                     listOut.append( ')' )
#         listOut = ''.join( listOut )
        
#         return listOut  
    
#     def algorithmsInvert( self, inputStrInvert ):
#         '''
#         '''
#         flipString = ""
#         inputStrInvert = inputStrInvert[::-1]
#         for charBracket in inputStrInvert:
#             if charBracket == "(":
#                 flipString += ")"
#             elif charBracket == ")":
#                 flipString += "("    
#         return flipString
    
#     def algorithmsExtract( self, inputStrExtract ):
#         '''
#         ''' 
#         left = 0
#         right = left + 1
#         inputList = list( inputStrExtract )
#         while ( right < len( inputList ) ):
#             if ( inputList[ left ] == "(" and inputList[ right ] == "(" ) :
#                 left += 1
#                 right += 1
#             else:
#                 inputList.pop( right )
#                 inputList.pop( left )
#                 inputList.append( "(" )
#                 inputList.append( ")" )
#                 break

#         inputString = ''.join( inputList )
#         return inputString
    
#     def algorithmsAppendBack( self, inputStrBack ):
#         '''
#         '''
#         inputList = list( inputStrBack )
#         right = len( inputList ) - 1 
#         left = right - 1 
#         stack = 0
        
#         while( left >= 0 ):
#             if( inputList[ right ] == ")" and inputList[ left ] == "(" and stack == 0 ):
#                 inputList.pop( len( inputList ) - 1 )
#                 inputList.pop( len( inputList ) - 1 )
#                 stack += 1
#                 right -= 2
#                 left -= 2
#             elif( inputList[ right ] == ")" and inputList[ left ] == ")" ):
#                 inputList.insert( right, "()" )
#                 break
#             else:
#                 left -= 1
#                 right -= 1
            
#         inputList = ''.join( inputList )
#         return inputList
    
# checkAns = Solution()
# print( 'The answer is ', checkAns.generateParenthesis( 3 ) )                    # Expected ["((()))","(()())","(())()","()(())","()()()"]
# print( 'The answer is ', checkAns.generateParenthesis( 4 ) )                    # Expected ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print( 'The answer is ', checkAns.generateParenthesis( 1 ) )                    # Expected ["()"]
# # When 1 <= n <= 8


# Solution of this question 
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # only add open paranthesis if open < n
        # only add a closing paranthesis if closed < open
        # valid IIF open == closed == n
        
        stack = []
        res = []
        
        def backtrack( openN, closedN ):
            # If the parenthesis is on the limit return out
            if openN == closedN == n:
                # if it append in stack completly, so put in the result next 
                res.append( "".join( stack ) )
                return
            
            if openN < n:
                # If the open parathesis is less than the limit of n, you can have choice to add more open parathsis
                stack.append( "(" )
                # Called the backtrack function agian to check next iteration, but you need to tell the function that we are already add more open parenthesis
                backtrack( openN + 1, closedN )
                # We gonna update the stack because we pass only the number of open parathesis and close parathesis, so the algorithms will not know. But the stack is global valiable, so after we doing something done we need to pop it out for cleaning up.
                stack.pop()
                
            if closedN < openN:
                # If the close parathesis is less than the open parathesis, you can have choice to add more close parathsis
                stack.append( ")" )
                # Called the backtrack function agian to check next iteration, but you need to tell the function that we are already add more close parenthesis
                backtrack( openN, closedN + 1 )
                # We gonna update the stack because we pass only the number of open parathesis and close parathesis, so the algorithms will not know. But the stack is global valiable, so after we doing something done we need to pop it out for cleaning up.
                stack.pop()
            
        backtrack( 0, 0 )
        return res
    
    
checkAns = Solution()
print( 'The answer is ', checkAns.generateParenthesis( 3 ) )                    # Expected ["((()))","(()())","(())()","()(())","()()()"]
# print( 'The answer is ', checkAns.generateParenthesis( 2 ) )                    # Expected 
# print( 'The answer is ', checkAns.generateParenthesis( 5 ) )                    # Expected 
# print( 'The answer is ', checkAns.generateParenthesis( 6 ) )                    # Expected 
# print( 'The answer is ', checkAns.generateParenthesis( 7 ) )                    # Expected 
# print( 'The answer is ', checkAns.generateParenthesis( 8 ) )                    # Expected 
# print( 'The answer is ', checkAns.generateParenthesis( 4 ) )                    # Expected ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]
# print( 'The answer is ', checkAns.generateParenthesis( 1 ) )                    # Expected ["()"]
# When 1 <= n <= 8