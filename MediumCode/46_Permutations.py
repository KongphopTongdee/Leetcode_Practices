#  # This code is from chat gpt
#     def generatePermutations( self, arr, idx = 0 ):
#         # Empty arr return not thing
#         if ( idx == len( arr ) ):
#             print( arr )
#             return 
        
#         # Loop for swap arr
#         for i in range( idx, len( arr ) ):
#             # Swap
#             arr[ idx ], arr[ i ] = arr[ i ], arr[ idx ]
#             # Recur for next index
#             self.generatePermutations( arr, idx + 1 )
#             # Swap back( backtracking )
#             arr[ idx ], arr[ i ] = arr[ i ], arr[ idx ]
            
# -------------------------------------------------------------------------------------------------------
            
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
class Solution:
    def __init__( self ):
        self.answer = []
    
    def changePositionIdx( self, ):
        
    
   
                    
    
    def permute( self, nums ):
        answer = self.changePositionIdx( nums )
    
checkAns = Solution()
checkAns.permute( [ 1, 2, 3 ] )
# checkAns.permute( [ 0, 1 ] )
# checkAns.permute( [ 1 ] )
