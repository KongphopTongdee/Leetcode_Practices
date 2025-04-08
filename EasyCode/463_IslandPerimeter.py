class Solution:
    def __init__( self ):
        self.answer = 0
    
    def findAllIsland( self, girdInput ):
        girdCount = 0
        
        for i in range( len( girdInput ) ):
            for j in range( len( girdInput[ i ] ) ):
                if( girdInput[ i ][ j ] == 1 ):
                    girdCount += 1
        
        
    
    def islandPerimeter( self, grid ):
        self.findAllIsland( grid )
        
    
checkAns = Solution()
checkAns.islandPerimeter( [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] )
# checkAns.islandPerimeter( [[1]] )
# checkAns.islandPerimeter( [[1,0]] )
