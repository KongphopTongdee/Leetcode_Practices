class Solution:
    def __init__( self ):
        self.answer = 0
        
    def getFirstAndSecond( self, arraySort ):
        calArray = arraySort.copy()
        firstArray = ()
        secondArray = ()
        theRest = []
        
        if( len( arraySort ) == 2 ):
            firstArray = ( arraySort[ 0 ], arraySort[ 1 ] )
            return firstArray, secondArray, theRest
            
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
        firstArray, secondArray, theRest = self.getFirstAndSecond( nums )
        theRest.append( firstArray )
        theRest.append( secondArray )
        sumation = 0
    
        for amount in range( len( theRest ) ):
            sumation += min( theRest[ amount ] )
            
        return sumation
    
checkAns = Solution()
checkAns.arrayPairSum( [1,4,3,2] )
checkAns.arrayPairSum( [6,2,6,5,1,2] )
checkAns.arrayPairSum( [6,2,6,5,1,2,7,8,8,8,9,10] )
checkAns.arrayPairSum( [1,1] )                                  #Runtime Error