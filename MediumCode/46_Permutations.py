class Solution:
    def __init__(self):
        self.answer = []
    
    # This code is from chat gpt
    def generatePermutations( self, arr, idx = 0 ):
        # Empty arr return not thing
        if ( idx == len( arr ) ):
            print( arr )
            return 
        
        # Loop for swap arr
        for i in range( idx, len( arr ) ):
            # Swap
            arr[ idx ], arr[ i ] = arr[ i ], arr[ idx ]
            # Recur for next index
            self.generatePermutations( arr, idx + 1 )
            # Swap back( backtracking )
            arr[ idx ], arr[ i ] = arr[ i ], arr[ idx ]
            
        
    #Writing own code...
    
    def permute( self, nums ):
        self.generatePermutations( nums )
    
checkAns = Solution()
checkAns.permute( [ 1, 2, 3 ] )
# checkAns.permute( [ 0, 1 ] )
# checkAns.permute( [ 1 ] )