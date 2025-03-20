# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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
    def genOwnPermutations( self, arr ):
        spareArr = arr.copy()
        numUse = 0
        answer = []
        storeAns = []
        processAns = []
        processAnsRem = []
        countArr = 0
        
        while( countArr < len( arr ) ):
            countArr += 1 
            numUse = spareArr[ 0 ]
            spareArr.pop( 0 )
            if( len( processAns ) == 0 ):
                processAns.append( numUse )
            elif( len( processAns ) >= 1 ):
                for i in range( 0, len( processAns ) + 1 ):
                    processAnsRem = processAns.copy()
                    processAns.insert( i, numUse )
                    storeAns.append( processAns )
                    processAns = processAnsRem.copy()
                    
        
        print( storeAns )
                    
    
    def permute( self, nums ):
        # self.generatePermutations( nums )
        self.genOwnPermutations( nums )
    
checkAns = Solution()
checkAns.permute( [ 1, 2, 3 ] )
# checkAns.permute( [ 0, 1 ] )
# checkAns.permute( [ 1 ] )
