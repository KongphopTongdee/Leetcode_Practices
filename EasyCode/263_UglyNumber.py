class Solution:
    def __init__( self ):
        self.answer = None
        self.primeUglyNum = [ 2, 3, 5 ] 
        
    def checkPrimeNumber( self, value ):
        # Negative numbers, 0 and 1 are not primes
        if  value > 1:
  
            # Iterate from 2 to n // 2
            for i in range(2, int( value // 2 ) + 1 ):
      
                # If num is divisible by any number between
                # 2 and n / 2, it is not prime
                if ( value % i) == 0:
                    return False
            else:
                return True
        else:
            return False

        
    def isUgly( self, n ):
        storeDivine = []
        
        while( ( self.checkPrimeNumber( n ) == False ) and ( n != 1 ) ):
            for divineNum in self.primeUglyNum:
                if ( n % divineNum == 0 ):
                    n /= divineNum
                    n = int( n )
                    storeDivine.append( divineNum )
                    
        if( ( n not in self.primeUglyNum ) and ( n != 1 ) ):
            return False
        elif( n == 1 ):
            return True
        
        
checkAns = Solution()
checkAns.isUgly( 6 )
checkAns.isUgly( 1 )
checkAns.isUgly( 14 )
checkAns.isUgly( 8 )                       # Answer: true