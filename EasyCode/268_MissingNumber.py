class Solution:
    def __init__( self ):
        self.answer = 0
    
    def genCorrectAns( self, inputArray ):
        copyInputArray = inputArray.copy()
        copyInputArray.sort()
        outputArray = []
        
        for num in range( copyInputArray[ len( copyInputArray ) - 1 ] ):
            outputArray.append( num )
            
        outputArray.append( copyInputArray[ len( copyInputArray ) - 1 ] )
            
        return outputArray
        
    def checkArray( self, inputArray, correctArray ):
        inputArray.sort()

        if( len( inputArray ) == len( correctArray ) ):
            return inputArray[ len( inputArray ) - 1 ] + 1
        else:
            for idx in range( len( correctArray ) ):
                try:
                    if( correctArray[ idx ] == inputArray[ idx ] ):
                        continue
                    else:
                        return correctArray[ idx ]
                except:
                    return correctArray[ len( correctArray ) - 1 ] 
                    
    def missingNumber( self, nums ):
        correctArray = self.genCorrectAns( nums )
        missNumber = self.checkArray( nums, correctArray )
        self.answer = missNumber
        
        return self.answer
