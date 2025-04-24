class Solution:
    def __init__( self ):
        self.answer = []
        self.STARTARR = [ 1, 1 ]
        
    def createTriangle( self, rowsInput ):
        allPascal = [ [ 1, 1 ] ]
        curentArr = [ 1, 1 ]
        if( rowsInput >= 3 ):
            for idx in range( rowsInput - 1 ):
                
            
        return allPascal
    
    def generate( self, numRows ):
        if( numRows == 1 ):
            self.answer.append( [ 1 ] )
        elif( numRows > 1 ):
            pascalArr = self.createTriangle( numRows )
            self.answer = pascalArr
            
        return self.answer


checkAns = Solution()
print( checkAns.generate( 5 ) )
# print( checkAns.generate( 1 ) )
