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
        newN = [ 0,0,  ]
        
        if ( n <= 0 ):
            return False
            
        if ( n == 1 ):
            return True
        
        while( ( self.checkPrimeNumber( n ) == False ) and ( newN[ len( newN ) - 2 ] != n ) ):
            for divineNum in self.primeUglyNum:
                if ( n % divineNum == 0 ):
                    n /= divineNum
                    n = int( n )
                    storeDivine.append( divineNum )
            # Update n to new value
            newN.append( n )
        
        print( "store storeDivine: ", storeDivine )
        print( "n before check condition: ", n )
            
        # check condition ugly number
        if( n >= 1 ):
            if( n in self.primeUglyNum ):
                return True
            elif( n == 1 ):
                self.answer = True
            else:
                return False
                
                
                    
        return self.answer
        
        
checkAns = Solution()
# print( checkAns.isUgly( 6 )  )
# print( checkAns.isUgly( 1 )  )
# print( checkAns.isUgly( 14 ) )
# print( checkAns.isUgly( 8 )  )
# print( checkAns.isUgly( -2147483648 ) )
# print( checkAns.isUgly( 65536 ) )
# print( checkAns.isUgly( -51799 )  )
# print( checkAns.isUgly( 98 )   )
print( checkAns.isUgly( n = 1332185066 )   )                # Runtime Error but complete

# checkAns.isUgly( 6 )                                      # Answer: True
# checkAns.isUgly( 1 )                                      # Answer: True
# checkAns.isUgly( 14 )                                     # Answer: False
# checkAns.isUgly( 8 )                                      # Answer: True
# checkAns.isUgly( -2147483648 )                            # Answer: False
# checkAns.isUgly( 65536 )                                  # Answer: True
# checkAns.isUgly( -51799 )                                 # Answer: False 
# checkAns.isUgly( 98 )                                     # Answer: False
# checkAns.isUgly( n = 1332185066 )                           # Answer: False
