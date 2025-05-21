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
        
    
# checkAns = Solution()
# checkAns.main( maze = [
#     [0, 1, 0, 0],
#     [0, 0, 0, 1],
#     [1, 1, 0, 1],
#     [0, 0, 0, 0]
# ], start = (0, 0), end = ( 3, 3 ) )


# 2. Flood Fill (Like Paint Bucket Tool)
# 🧩 Problem: Implement the "flood fill" algorithm. Given a 2D image (grid of colors) and a start point, fill the connected region of the same color with a new color.

# ✅ Concepts practiced: handling boundaries, avoiding re-visiting cells

class Solution():
    def __init__( self ):
        self.answer = []
        
    def floodFill(self, image, startPos, newColor):
        '''The function for fill the new color on the image.
        
        Parameters
        ----------
        image : ndarray with shape ( imageHeight, imageWidth )
            The input image which has only one color dimension.
        startPos : ndarray with shape ( nSample, 2 )
            The select position for start depth-first search in the form of coordinate.
        newColor:
            The new color to change.
        
        Return
        ------
        image : ndarray with shape ( imageHeight, imageWidth )
            The output image after change color which has only one color dimension.
        '''
        # Seperate the tuple into one variable.
        sr, sc = startPos
        # Get the limit of image. 
        rows, cols = len(image), len( image[0] )
        # Get the original color of image before change.
        originalColor = image[sr][sc]

        # Check, no need to fill if color is same.
        if originalColor == newColor:
            return image  
    
        # Define funciton depth-first search.
        def dfs(r, c):
            # Check boundaries.
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return
            # If the color already change ignore them.
            if image[r][c] != originalColor:
                return
            
            # Fill the color
            image[r][c] = newColor  
    
            # Explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
    
        # Call the function 
        dfs(sr, sc)
        
        return image
        

    def main( self, array2D, startPos, numChange ):
        '''The main funciton receive the array, start postion, and number to change.
        
        Parameters
        ----------
        array2D : ndarray with shape ( arrayHeight, arrayWidth )
            The input array which have the random number.
        startPos : ndarray with shape ( nSample, 2 )
            The first point to start depth-first search.
        numChange : int
            The number which want to replace when depth-first search is running.
        
        Return
        ------
        array2D : ndarray with shape ( arrayHeight, arrayWidth )
            The new array2D that already change number inslide the array.
        '''
        
        # self.answer = self.dfsChangePointInArray( array2D, startPos, numChange )
        self.answer = self.floodFill( array2D, startPos, numChange )
    
        return self.answer
        
# checkAns = Solution()
# checkAns.main( ( 
# [ 4, 7, 0, 4, 10 ], 
# [ 5, 2, 0, 8, 2 ], 
# [ 5, 8, 0, 7, 7 ], 
# [ 10, 4, 0, 5, 2 ], 
# [ 8, 7, 0, 9, 1 ] ), ( 2, 2 ), 66 )
# checkAns.main( ( 
# [ 2, 1, 3, 8, 4 ], 
# [ 7, 4, 7, 2, 2 ], 
# [ 0, 0, 0, 0, 0 ], 
# [ 2, 1, 7, 9, 8 ], 
# [ 6, 5, 9, 5 ,7 ] ), ( 2, 4 ), 66 )
# checkAns.main( ( 
# [ 6, 0, 4, 5, 8 ], 
# [ 6, 0, 0, 6, 1 ], 
# [ 3, 6, 0, 0, 9 ], 
# [ 8, 2, 3, 0, 4 ], 
# [ 7, 8, 4, 0, 2 ]  ), ( 2, 3 ), 66 )

# 3. Path Sum in a Binary Tree
# 🧩 Problem: Given a binary tree and a sum, return True if there's a path from root to leaf where the sum of node values equals the given value.
# ✅ Concepts practiced: DFS on trees, backtracking

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# Build the TreeNode
# First Iteration
root = TreeNode( 5 )
root.left = TreeNode( 4 )
root.right = TreeNode( 8 )

# Second Iteration
root.left.left = TreeNode( 11 )
root.right.left = TreeNode( 13 )
root.right.right = TreeNode( 4 )

# Third Iteration
root.left.left.left = TreeNode( 7 )
root.left.left.right = TreeNode( 2 )

class Sollution():
    def __init__( self ):
        self.answer = False
        
    def subsetsWithDup( self, nums ):
        result = []
        
        def backTrack( start, current ):
            # Add current subset to the final result
            result.append( list( current ) )
            # Iterate over nums to generate all possible subsets
            for i in range( start, len( nums ) ):
                # 1. Skip duplicates
                if( ( i > start ) and nums[ i ] == nums[ i - 1 ] ):
                    continue
                # 2. Include nums[i] in current subset and move forward 
                current.append( nums[ i ] )
                backTrack( i + 1, current )
                # 3. Exclude nums[i] from current subset (backtrack)
                current.pop()
                
        # Sort the numbers to handle duplicates
        nums.sort()
        # Initiate backtracking
        backTrack( 0, [] )
        return result
        
    
    def main( self, objTreeNode, sumValue ):
        inputNums = [ 1, 2, 2 ]
        finalResult = self.subsetsWithDup( inputNums )
        
        return self.answer 
    
# checkAns = Sollution()
# checkAns.main( root, 22 )


# Don't Use
class Solution():
    def __init__( self ):
        self.answer = []
    
    def backTracking( self, arrayValue ):
        result = []
        
        def bT( start, current ):
            # Add every currnt array in result
            result.append( list( current ) )
            # Loop for amount of array input
            for idx in range( start, len( arrayValue ) ):
                # 1. Skip duplicates when idx is more than startIDX and value was the same as previous value.
                if( ( idx > start ) and ( arrayValue[ idx ] == arrayValue[ idx - 1 ] ) ):
                    continue
                # 2. Add value in current array and move forward.
                current.append( arrayValue[ idx ] )
                # Backtrack to the value that didn't similar to previous value.
                bT( idx + 1, current )
                # 3. Add the current array in the result when call backtrack function again. And search the back the previous value (backtrack)
                current.pop()
        # Sort the number to handle the duplicates
        arrayValue.sort()
        # Start first backTracking
        bT( 0, [] )
        
        return result
    
    def main( self, arrayValue ):
        self.answer  = self.backTracking( arrayValue )
        print( self.answer )
        return self.answer
        
checkAns = Solution()
checkAns.main( [ 1, 2, 3, 4 ] )
