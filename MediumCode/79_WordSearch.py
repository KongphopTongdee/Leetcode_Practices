'''
Step to create word search question
1.Find all position which relate to the first charecter. Create the array which store the position 
2.Create depth first search algorithms
2.1.Create the visit path to store the old position. Don't use the same charecter
2.2.Search around the current position which relate to another charecter of input word.
3.After finish, If it was true return out, It would be false pop out the position and start new search which reset the old memory.
'''

class Solution:
    def __init__( self ):
        self.answer = False
        self.allStartPos = []
        self.testValue = "ABCD"
    
    def findStartPos( self, allMaze, firstCharacter ):
        storePos = []
        for row in range( len( allMaze ) ):
            for column in range( len( allMaze[ 0 ] ) ):
                if( allMaze[ row ][ column ] == firstCharacter ):
                    storePos.append( ( row, column ) )
        return storePos
        
    def depthFirstSearch( self, board, startPos, word ):
        visit = set()
        
        word = list( word )
        # word.pop( 0 )
        nextChar = word[ 0 ]
        insertOldChar = []
        
        
        def dfs( row, column, nextChar ):
            if( ( row < 0 ) or ( column < 0 ) or ( row >= len( board ) ) or ( column >= len( board[ 0 ] ) ) or ( board[ row ][ column ] != nextChar ) ):
                return False
            if( ( row, column ) in visit ):
                return False
            if( ( board[ row ][ column ] == nextChar ) and ( len( word ) != 0 ) ):
                insertOldChar.append( word[ 0 ] )
                word.pop( 0 )
                
                # condition for stop loop
                if( len( word ) == 0 ):
                    return True
                    
                nextChar = word[ 0 ]
            
            visit.add( ( row, column ) )
            
            # search top
            if( dfs( row + 1, column, nextChar ) == True ):
                return True
            # search bottom
            if( dfs( row - 1, column, nextChar ) == True ):
                return True
            # search left
            if( dfs( row, column - 1, nextChar ) == True ):
                return True
            # search right
            if( dfs( row, column + 1, nextChar ) == True ):
                return True
            
            word = insertOldChar.extend( word )
            insertOldChar = []
            
        startPosX, startPosY = startPos
        
        if( dfs( startPosX, startPosY, nextChar ) == True ):
            return True
            
        return False
        
        
    def exist( self, board, word ):
        self.allStartPos = self.findStartPos( board, word[ 0 ] )
        for eachStartPos in self.allStartPos:
            if( self.answer == True ):
                return True
            self.answer = self.depthFirstSearch( board, eachStartPos, word )
            
        return self.answer
        
    
    def test( self ):
        word = list( self.testValue )
        word.pop( 0 )
        print( word )
    
checkAns = Solution()
# checkAns.test()
# checkAns.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" )
checkAns.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE" )
# checkAns.exist( board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB" )
