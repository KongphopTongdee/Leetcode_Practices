class Solution:
    def __init__( self ):
        self.answer = 0
    
    def return1ArrayNum( self, numInput ):
        numInput = str( numInput )
        numArray = list( numInput )
        result = 0
        
        while( ( len( numArray ) != 1 ) ):
            for idx in range( len( numArray ) ):
                result += int( numArray[ idx ] )
            numArray = list( str( result ) )
            result = 0
        
        return numArray
    
    def addDigits( self, num ):
        answer = self.return1ArrayNum( num )
        self.answer = int( answer[ 0 ] )
        
        return self.answer
