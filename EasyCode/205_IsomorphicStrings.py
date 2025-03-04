class Solution:
    def __init__( self ):
        self.answer = None
    
    def sortedDict( self, inputDict ):
        sortDict = { key: value for key, value in sorted( inputDict.items(), key=lambda item: item[ 1 ] ) }
        return sortDict
    
    def convertIntoDict( self, inputWord ):
        ansDict = {}
        searchChar = set( inputWord )
        listInput = [ i for i in inputWord ]
        
        for eachChar in searchChar:
            ansDict.update( { eachChar : listInput.count( eachChar ) } )
    
        sortDict = self.sortedDict( ansDict )
        
        return sortDict
    
    def checkSimilar( self, firstInput, secondInput ):
        if ( len( firstInput ) != len( secondInput ) ):
            return False
            
        convertToListFirstInput = [ i for i in firstInput.values() ]
        convertToListSecondInput = [ i for i in secondInput.values() ]
        
        for idx in range( len( convertToListFirstInput ) ):
            if ( convertToListFirstInput[ idx ] ==  convertToListSecondInput[ idx ] ):
                continue
            else:
                return False
                
        return True
            
    def isIsomorphic( self, s , t ):
        sDict = self.convertIntoDict( s )
        tDict = self.convertIntoDict( t )
        self.answer = self.checkSimilar( sDict, tDict )
        print( self.answer )
        return( self.answer )
        
checkAns = Solution()
checkAns.isIsomorphic( "egg" , "add" )
checkAns.isIsomorphic( "foo" , "bar" )
checkAns.isIsomorphic( "paper" , "title" )
checkAns.isIsomorphic( "bbbaaaba" , "aaabbbba" )        # answer: false