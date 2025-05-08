# You are given a 2D grid representing a maze:
# - 0 means open space
# - 1 means a wall
# You are given a start position and an end position.
# Use DFS to check if there's a path from start to end.

# Example
# maze = [
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 1],
#     [0, 0, 0, 0]
# ]
# start = (0, 0)
# end = (3, 3)

class Solution():
    def __init__( self ):
        self.answer = False
          
    def depthFirstSearch( self, allMaze, startPos, endPos ):
        '''The function that use depth-first search algorithms to find the path.
        
        Parameters
        ----------
        allMaze : ndarray with shape ( mazeHeight, mazeWidth )
            The maze size 
        startPos : ndarray with coordinate shape ( row, y )
            The start point
        endPos : ndarray with coordinate shape ( row, y )
            The end point
        
        Return
        ------
        ansBool : boolean
            The answer of the True( There are some path from start to end position. ) 
            and False( There aren't any path from start to end position. ).
        
        '''
        # Declare the valiable for keep visit path.
        visit = set()
        
        # Declare the funtion for check around element.
        def dfs( row, column ):
            # Check, if there are boundary or wall.
            if( ( row < 0 ) or ( column < 0 ) or ( row >= len( allMaze ) ) or ( column >= len( allMaze[ 0 ] ) ) or ( allMaze[ row ][ column ] == 1 ) ):               #  Use >= because we want the last ( row, column ) position but len didn't give last index.
                return False
            # Check, if there are already visit.
            if( ( row, column ) in visit ):
                return False
            # Check, if there is the end position.
            if( ( row, column ) == endPos ):
                return True
                
            # If there aren't come to this, grid add it.
            visit.add( ( row, column ) )
            
            # Check Right
            if( dfs( row, column + 1 ) == True ):
                return True
            # Check Left
            if( dfs( row, column - 1 ) == True ):
                return True
            # Check Bottom
            if( dfs( row - 1, column ) == True ):
                return True
            # Check Top
            if( dfs( row + 1, column ) == True ):
                return True
                
        startPosX, startPosY = startPos
        if( dfs( startPosX, startPosY ) == True ) :
            return True
        
        return False
    
    def main( self, maze, start, end ):
        '''The main function for call the depth-first search funtion.
        
        Parameters
        ----------
        maze : ndarray with shape ( mazeHeight, mazeWidth )
            The maze size 
        start : ndarray with coordinate shape ( x, y )
            The start point
        end : ndarray with coordinate shape ( x, y )
            The end point
        
        Return
        ------
        ansBool : boolean
            The answer of the True( There are some path from start to end position. ) 
            and False( There aren't any path from start to end position. ).
        
        '''
        
        self.answer = self.depthFirstSearch( maze, start, end )
        print( self.answer )
        
        return self.answer
        
    
checkAns = Solution()
checkAns.main( maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
], start = (0, 0), end = ( 3, 3 ) )


# 2. Flood Fill (Like Paint Bucket Tool)
# 🧩 Problem: Implement the "flood fill" algorithm. Given a 2D image (grid of colors) and a start point, fill the connected region of the same color with a new color.

# ✅ Concepts practiced: handling boundaries, avoiding re-visiting cells
