class Solution:
    def __init__(self):
        self.Answer = []
    
    def fillCharecterEachWord( self, listStrs ):
        storeCha = []
        
        for words in listStrs:
            for cha in words:
                storeCha.append( cha ) 
            break
        return storeCha
    
    def separateWord( self, checkChar, words ):
        listAns = []
        checkTrue = []
        for eachWords in words:
            for eachChar in checkChar:
                if( eachChar in eachWords ):
                    checkTrue.append( True )
                else:
                    checkTrue.append( False )
            if( all( checkTrue ) == True ):
                listAns.append( eachWords )
            checkTrue = []
        return listAns
    
    def deleteValue( self, listStrs, listDel ):
        calListStrs = listStrs.copy()
        for wordDel in listDel:
            calListStrs.remove( wordDel )
        return calListStrs
    
    def arrangeTheQuantity( self, itemToArrange ):
        convertToDict = {}
        for eachItem in itemToArrange:
            convertToDict.update( { len(eachItem) : eachItem } )
        sort_convertToDict = dict( sorted(convertToDict.items() ) )
        convertToList = []
        for key, value in sort_convertToDict.items():
            convertToList.append( value )
        return convertToList
        
    def groupAnagrams( self, strs ):
        strs.sort()
        
        emptyPart = 0
        if( strs[0] == "" ):
            strs.pop(0)
            emptyPart = 1
            
        spareAnswer = []
        
        while( ( len(strs) != 0 ) ):
            checkCharInWord = self.fillCharecterEachWord( strs )
            sameWords = self.separateWord( checkCharInWord, strs )
            spareAnswer.extend( [ sameWords ] )
            newStrs = self.deleteValue( strs, sameWords )
            strs = newStrs
        
        self.Answer = self.arrangeTheQuantity( spareAnswer )
        if( emptyPart == 1 ):
            self.Answer.append( [""] )
        print(self.Answer)
        return self.Answer

CheckAns = Solution()
CheckAns.groupAnagrams( ["eat","tea","tan","ate","nat","bat"] )         #Output => [["bat"],["nat","tan"],["ate","eat","tea"]]
CheckAns.groupAnagrams( [""] )                                          #Output => [[""]]
CheckAns.groupAnagrams( ["a"] )                                         #Output => [["a"]]
CheckAns.groupAnagrams( ["","b"] )                                      #Output => [["b"],[""]]
CheckAns.groupAnagrams( ["",""] )                                       #Output => [["",""]]

