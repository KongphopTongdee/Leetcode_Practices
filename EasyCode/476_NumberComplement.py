class Solution:
    def __init__( self ):
        self.answer = 0
        
    def convertBinary( self, inputVal ):
        binaryList = []
        
        while( inputVal != 1 ):
            binaryList.append( inputVal % 2 )
            inputVal = inputVal // 2 
            
        binaryList.append( 1 )
            
        return binaryList[::-1]
    
    def flipComplement( self, inputBinary ):
        outputAns = []
        for output in inputBinary:
            if( output == 1 ):
                outputAns.append( 0 )
            elif( output == 0 ):
                outputAns.append( 1 )
        
        return outputAns
    
    def convertDecimal( self, inputBinary ):
        outputValue = 0
        
        for idx in range( len( inputBinary ) ):
            if( inputBinary[ idx ] == 1 ):
                outputValue += 2**( len( inputBinary ) - 1 - idx )
            
        return outputValue
    
        
    def findComplement( self, num ):
        binaryOutput = self.convertBinary( num )
        flipAns = self.flipComplement( binaryOutput )
        decimalOutput = self.convertDecimal( flipAns )
    
        self.answer = decimalOutput
        
        return self.answer
        
    
    
checkAns = Solution()
checkAns.findComplement( 5 )
# checkAns.findComplement( 1 )
        