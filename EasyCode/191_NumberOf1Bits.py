class Solution:
    def __init__( self ):
        self.answer = 0
    
    def convertToBinary( self, num ):
        '''
        Parameters
        -----------
		num : number 

        Return
        ----------
		listBinary : ndarray of shape ( nDim, )
        '''
        listBinary = []
        
        while( ( num != 1 ) and ( num != 0 ) ):
            listBinary.append( int( num % 2 ) )
            num = num // 2
            
        listBinary.append( 1 )
        
        return listBinary[::-1]
    
    def hammingWeight( self, n ):
        binaryArray = self.convertToBinary( n )
        for result in binaryArray:
            if( result == 1 ):
                self.answer += 1

        return self.answer
        
        
checkAns = Solution()
checkAns.hammingWeight( 11 )
checkAns.hammingWeight( 128 )
checkAns.hammingWeight( 2147483645 )