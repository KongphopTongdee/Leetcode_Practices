class Solution:
    def __init__(self):
        self.answer = None
    
    def isHappy( self, n ):
        storeValue = []
        value = n
        
        while( storeValue.count( value ) <= 1 ):
            newValue = 0
            value = str( value )
            for idx in range( len( value ) ):
                newValue += ( int( value[ idx ] ) ** 2 )
        
            storeValue.append( newValue )
            value = newValue
            
        if ( storeValue[ len( storeValue ) - 1 ] == 1 ):
            self.answer = True
        else:
            self.answer = False
            
        return self.answer
    
checkAns = Solution()
# checkAns.isHappy( 19 )
checkAns.isHappy( 2 )