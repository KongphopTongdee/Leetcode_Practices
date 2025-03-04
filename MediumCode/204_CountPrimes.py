class Solution:
    def __init__( self ):
        storeValue = 0
    
    def countPrimes( self, n ):
        answer = 0
        numPrime = 0
        for nums in range( 1, n ):
            # print( n )
            # print( nums )
            if( n % nums == 0 ):
                numPrime += 1
        
        # print( numPrime )
        
        if( numPrime == 2 ):
            answer = 0
        elif( numPrime > 2 ):
            answer = numPrime - 2
            
        print( answer )
            
        return answer
    
    def testCode( self ):
        answer = 6 % 2
        print( answer )
        return answer
    
checkAnswer = Solution()
checkAnswer.countPrimes( 10 )
# checkAnswer.countPrimes( 0 )
# checkAnswer.countPrimes( 1 )
# checkAnswer.testCode()
