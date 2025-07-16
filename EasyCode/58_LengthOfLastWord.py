# class Solution():
#     def __init__( self ):
#         self.answer = 0
        
#     def invertStr( self, inputStr ):
#         return inputStr[::-1] 
        
#     def searchLength( self, inputStr ):
#         countLength = 0
#         modeCount = 0
#         for idx in range( len( inputStr ) ):
#             if( ( inputStr[ idx ] == " " ) and ( modeCount == 0 ) ):
#                 continue
#             elif( ( inputStr[ idx ] != " " ) and ( modeCount == 0 ) ):
#                 modeCount = 1
#                 countLength = 1
#             elif( ( inputStr[ idx ] != " " ) and ( modeCount == 1 ) ):
#                 countLength += 1
#             elif( ( inputStr[ idx ] == " " ) and ( modeCount == 1 ) ):
#                 return countLength
        
#         return countLength
        
#     def main( self, inputStr ):
#         reverseStr = self.invertStr( inputStr )
#         lengthStr = self.searchLength( reverseStr )
#         return lengthStr
    
#     def lengthOfLastWord( self, s ):
#         self.answer = self.main( s )
#         return self.answer
    
# checkAns = Solution()
# checkAns.lengthOfLastWord( "Hello World" )
# checkAns.lengthOfLastWord( "   fly me   to   the moon  " )
# checkAns.lengthOfLastWord( "luffy is still joyboy" )

# -------------------------------------------------------------------------------------------------------
# LeetCode Answer

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()                               # string.strip() = remove the white space
        
        if not words:
            return 0
        
        return len(words[-1])
    
checkAns = Solution()
print( checkAns.lengthOfLastWord( "Hello World" ) )
print( checkAns.lengthOfLastWord( "   fly me   to   the moon  " ) )
print( checkAns.lengthOfLastWord( "luffy is still joyboy" ) )

