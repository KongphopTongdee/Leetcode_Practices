# import numpy as np

# class Solution:
#     def convert( self, s, numRows ):
#         if( len( s ) <= numRows ):
#             return s
#         elif( numRows == 1 ):
#             return s
#         try:
#             n = ( len( s ) / ( ( 2 * numRows ) - 2 ) ) + 1
#             n = int( n ) 
#         except:
#             n = 10
#         numColumns = n * ( numRows - 1 )
#         arr = np.full( ( numRows, numColumns ), '~' )
        
#         columns = 0
        
#         for charFirstColumns in range(numRows):
#             arr[ charFirstColumns, columns ] = s[ charFirstColumns ]
        
#         countString = numRows
#         rows = numRows - 2
#         columns += 1
        
#         while countString <= ( len( s ) - 1):
#             if( columns % ( numRows - 1 ) == 0 ) :
#                 arr[ rows, columns ] = s[ countString ]
#                 rows += 1
#                 if ( rows > ( numRows - 1 ) ):
#                     columns += 1
#                     rows -= 2
#             else:
#                 arr[ rows, columns ] = s[ countString ]
#                 columns += 1
#                 rows -= 1
                
#             countString += 1
        
#         answer = ''
        
#         charPerRow = [row[row != '~'] for row in arr]
#         for row in range( len( charPerRow ) ):
#             answer += ''.join(charPerRow[row])
            
#         return answer












# Best Answer from LeetCode

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        answer = ''
        n = len(s)
        diff = 2 * (numRows - 1)
        diagonal_diff = diff
        second_index = 0
        index = 0
        for i in range(numRows):
            index = i
            while index < n:
                answer += s[index]
                if i != 0 and i != numRows - 1:
                    diagonal_diff = diff - 2 * i
                    second_index = index + diagonal_diff
                    if second_index < n:
                        answer += s[second_index]
                index += diff
        return answer

longestSubstring = Solution()
print( longestSubstring.convert( "PAYPALISHIRING", 3 ) )
print( longestSubstring.convert( "PAYPALISHIRING", 4 ) )
print( longestSubstring.convert( "A", 1 ) )
print( longestSubstring.convert( "A", 2 ) )
print( longestSubstring.convert( "AB", 1 ) )
print( longestSubstring.convert( "Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 2 ) )