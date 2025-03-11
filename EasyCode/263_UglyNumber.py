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
        newN = n
        
        # Error this time was the n before input and n output was the same so the loop continue run
        while( ( self.checkPrimeNumber( n ) == False ) and ( n != 1 ) and ( n != -1 ) ):
            for divineNum in self.primeUglyNum:
                if ( n % divineNum == 0 ):
                    n /= divineNum
                    n = int( n )
                    print( "n on process: ", n )
                    storeDivine.append( divineNum )
                    newN = n
            # if( newN == n ):
            #     break
                    
        print( "Final n: ", n )
        
        if( ( self.checkPrimeNumber( n ) == True ) and ( n not in self.primeUglyNum ) ):
            self.answer = False
        elif( n == -1 ):
            self.answer = False
        elif( n == 1 ):
            self.answer = True
        
        if( n in storeDivine[ 0:len( storeDivine ) ]  ):
            self.answer = True
        
        print( self.answer )
        return self.answer
        
        
checkAns = Solution()
# checkAns.isUgly( 6 )                                    # Answer: True
# checkAns.isUgly( 1 )                                    # Answer: True
# checkAns.isUgly( 14 )                                   # Answer: False
# checkAns.isUgly( 8 )                                    # Answer: True
# checkAns.isUgly( -2147483648 )                          # Answer: False
checkAns.isUgly( -51799 )                               # Answer: 

