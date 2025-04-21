class Solution:
    def __init__( self ):
        self.answer = 0
    
    def positionAllIsland( self, girdInput ):
        allPosition = []
        islandPosition = []
        
        for xIndex in range( len( girdInput ) ):
            for yIndex in range( len( girdInput[ xIndex ] ) ):
                allPosition.append( ( xIndex, yIndex ) )
                if( girdInput[ xIndex ][ yIndex ] == 1 ):
                    islandPosition.append( ( xIndex, yIndex ) )
        
        # print( "allPosition: ", allPosition )
        # print( "islandPosition: ", islandPosition )
        
        return islandPosition, allPosition
    
    def countBorderLine( self, areaIsland, allIsland ):
        countBorderLine = 0
        for searchBorderLine in areaIsland:
            xIndex, yIndex = searchBorderLine
            topArea = ( xIndex, yIndex - 1 )
            bottomArea = ( xIndex, yIndex + 1 )
            leftArea = ( xIndex - 1, yIndex )
            rightArea = ( xIndex + 1, yIndex )
            
            if( ( topArea in areaIsland ) and ( bottomArea in areaIsland ) and ( leftArea in areaIsland ) and ( rightArea in areaIsland ) ):
                countBorderLine += 0
            
            # need to check 3 axis, 2 axis, 1 axis    
                
                
                
        return countBorderLine
    
    def islandPerimeter( self, grid ):
        areaIsland, allIsland = self.positionAllIsland( grid )
        borderLine = self.countBorderLine( areaIsland, allIsland )
        
        self.answer = borderLine
        
        return self.answer
        
    
checkAns = Solution()
checkAns.islandPerimeter( [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]] )
# checkAns.islandPerimeter( [[1]] )
# checkAns.islandPerimeter( [[1,0]] )
