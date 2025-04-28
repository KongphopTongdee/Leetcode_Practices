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
        self.answer = ()
        
        
    def depthFirstSearch( self, allMaze, startPos, endPos ):
        '''The function that use depth-first search algorithms to find the path.
        
        Parameters
        ----------
        allMaze : ndarray with shape ( mazeHeight, mazeWidth )
            The maze size 
        startPos : ndarray with coordinate shape ( x, y )
            The start point
        endPos : ndarray with coordinate shape ( x, y )
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
        def dfs( x, y ):
            # Check, if there are boundary or wall
            if( ( x < 0 ) or ( y < 0 ) or ( x >= len( allMaze ) ) or ( y >= len( allMaze[ len( allMaze ) - 1 ] )  ) or ( ( x, y ) == 1 ) ):               #  Use >= because we want the last ( x, y ) position but len didn't give last index.
                return 0
            if( x, y ) in visit:
                return 1 
            
            visit.add( x, y )
            
                
            
    
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
        
        return self.answer
        
    
checkAns = Solution()
checkAns.main( maze = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 0, 0]
], start = (0, 0), end = ( 3, 3 ) )