class Solution:
    def __init__( self ):
        self.answer = 0
        
    def convertToBinary( self, value ):
        storeBinary = []
        
        if( value == 0 ):
            storeBinary.append( 0 )
            return storeBinary
            
        if ( value == 1 ):
            storeBinary.append( 1 )
            return storeBinary
        
        while( value != 1 ):
            storeBinary.append( value % 2 )
            value = value // 2
            
        storeBinary.append( 1 )
        
        return storeBinary[ ::-1 ]
        
    def checkNumDifferent( self, input1, input2 ):
        amountOfDiff = 0
        if( len( input1 ) > len( input2 ) ):
            for idx in range( len( input1 ) - len( input2 ) ):
                input2.insert( 0, 0 )
        elif( len( input1 ) < len( input2 ) ):
            for idx in range( len( input2 ) - len( input1 ) ):
                input1.insert( 0, 0 )
        
        for idx in range( len( input1 ) ):
            if( input1[ idx ] != input2[ idx ] ):
                amountOfDiff += 1
    
        return amountOfDiff
    
    def hammingDistance( self, x, y ):
        binaryOfX = self.convertToBinary( x )
        binaryOfY = self.convertToBinary( y )
    
        self.answer = self.checkNumDifferent( binaryOfX, binaryOfY )

        return self.answer
        
checkAns = Solution()
checkAns.hammingDistance( 1, 4 )
checkAns.hammingDistance( 3, 1 )
checkAns.hammingDistance( 0, 1 )
