class Solution:
    def __init__( self ):
        self.answer = 0
        
    def singleNumber( self, nums ):
        nums.sort()
        copyInput = nums.copy()
        constantValue = list( set( copyInput ) )
        for value in constantValue:
            if ( nums.count( value ) == 1 ):
                self.answer = value
                
        print( self.answer )
        return self.answer
        
checkAns = Solution()
checkAns.singleNumber( [2,2,1] )
checkAns.singleNumber( [4,1,2,1,2] )
checkAns.singleNumber( [1] )

# Sort runtime and memory
def singleNumber( nums ):
    result = 0
    for n in nums:
        result ^= n             # same as: result = result ^ value -> ^ mean or
        
    print( result )
    return result