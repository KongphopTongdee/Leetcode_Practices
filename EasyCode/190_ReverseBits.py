class Solution:
    def __init__( self ):
        self.answer = 0
        
    def reveseBit( self, value ):
        return value[::-1]
    
    def convertToDecimal( self, value ):
        sumation = 0
        
        for idx in range( 0, len( value ) ):
            if( value[ idx ] == "1" ):
                sumation += 2**( len( value ) - 1 - idx )
                
        return sumation
    
    def reverseBits( self, n ):
        n = str( n )
        reverseInput = self.reveseBit( n )
        self.answer = self.convertToDecimal( reverseInput )
        print( self.answer )
        return self.answer


checkAns = Solution()
checkAns.reverseBits( "00000010100101000001111010011100" )                # Output: 964176192 
checkAns.reverseBits( "11111111111111111111111111111101" )                # Output: 3221225471
# checkAns.reverseBits( "1101" )                                            # Output: 11

        
