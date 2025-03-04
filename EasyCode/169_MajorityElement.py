class Solution:
    def __init__( self ):
        self.answer = 0
    
    # def majorityElement( self, nums ):
    #     if ( len( nums ) == 1 ):
    #         print( nums[0] )
    #         return nums[0]
        
    #     nums.sort()
    #     copyNums = nums.copy()
    #     copyNums = list( set( copyNums ) )
    #     for value in copyNums:
    #         if ( nums.count( value ) %2 == 0 ):
    #             self.answer = value
                
    #     print( self.answer )
    #     return self.answer
    
    def majorityElement( self, nums ):
        if ( len( nums ) == 1 ):
            print( nums[0] )
            return nums[0]
        
        storeValue = [ nums[0], ]
        for idx in range( 1, len( nums ) ):
            if nums[ idx ] in storeValue:
                print( nums[ idx ] )
                return nums[ idx ]
            else:
                storeValue.append( nums[ idx ] )           
        
    
checkAns = Solution()
checkAns.majorityElement( [3,2,3] )
checkAns.majorityElement( [2,2,1,1,1,2,2] )
checkAns.majorityElement( [1] )