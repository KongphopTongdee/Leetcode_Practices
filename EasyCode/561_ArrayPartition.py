class Solution:
    def __init__( self ):
        self.answer = 0
        
    def getFirstAndSecond( self, arraySort ):
        calArray = arraySort.copy()
        firstArray = ()
        secondArray = ()
        theRest = []
            
        if( len( arraySort ) == 4 ):
            firstArray = ( arraySort[ 0 ], arraySort[ 1 ] )
            secondArray = ( arraySort[ len( arraySort ) - 2 ], arraySort[ len( arraySort ) - 1 ] )
            return firstArray, secondArray, theRest
            
        if( len( arraySort ) >= 6 ):
            firstArray = ( arraySort[ 0 ], arraySort[ 1 ] )
            calArray.remove( arraySort[ 0 ] )
            calArray.remove( arraySort[ 1 ] )
            secondArray = ( arraySort[ len( arraySort ) - 2 ], arraySort[ len( arraySort ) - 1 ] )
            calArray.remove( arraySort[ len( arraySort ) - 1 ] )
            calArray.remove( arraySort[ len( arraySort ) - 2 ] )
            
        for iteration in range( 1, int( ( len( arraySort ) / 2 ) - 1 ) ):
            theRest.append( ( arraySort[ 2 + iteration ], arraySort[ len( arraySort ) - 3 -iteration ] ) )
        
        return firstArray, secondArray, theRest
        
    def arrayPairSum( self, nums ):
        nums.sort()
        print( nums )
        
        if( len( nums ) == 2 ):
            print( min( nums ) )
            return min( nums )
        
        firstArray, secondArray, theRest = self.getFirstAndSecond( nums )
        theRest.append( firstArray )
        theRest.append( secondArray )
        sumation = 0
    
        print( theRest )
        for amount in range( len( theRest ) ):
            print( theRest[ amount ] )
            sumation += min( theRest[ amount ] )
            
        self.answer = sumation
        print( self.answer )
        return self.answer
        
checkAns = Solution()
# checkAns.arrayPairSum( [1,4,3,2] )
# checkAns.arrayPairSum( [6,2,6,5,1,2] )
# checkAns.arrayPairSum( [6,2,6,5,1,2,7,8,8,8,9,10] )
# checkAns.arrayPairSum( [1,1] ) 
checkAns.arrayPairSum( [11, 41, -9046, 2047, 1118, 8477, 8446, 279, 4925, 7380, -1719, 3855] )      #Output: 6662
