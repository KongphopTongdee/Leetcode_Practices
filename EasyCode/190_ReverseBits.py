class Solution:
    def __init__( self ):
        self.answer = 0
    
    def convertToDecimal( self, value ):
        reverseStr = value[::-1]
        sumation = 0
        newValue = 0
        print( reverseStr )
    
        
        for idx in range( 0, len( reverseStr ) - 1 ):
            newValue = 2**( ( len( reverseStr ) - 1 ) - idx )
            print( newValue )
            if( reverseStr[ ( len( reverseStr ) - 1 ) - idx ] == "1" ):
                sumation += 2**( ( len( reverseStr ) - 1 ) - idx )
            
        print( sumation )
    
    def reverseBits( self, n ):
        self.convertToDecimal( n )
        


checkAns = Solution()
# checkAns.reverseBits( "00000010100101000001111010011100" )                # Output: 964176192 
# checkAns.reverseBits( "11111111111111111111111111111101" )                # Output: 3221225471
checkAns.reverseBits( "1101" )                # Output: 3221225471

        
