class Solution:
    def multiply( self, num1: str, num2: str ):
        calMultiply = list()
        calMultiply.append( int( num1 ) )
        calMultiply.append( int( num2 ) )
        ans = self.calMul( calMultiply )
        answer = "{}".format( ans )
        return answer
    
    def calMul( self, listInsert ):
        ans = 1
        for num in listInsert:
            ans *= num
        return ans
        
CheckAns = Solution()
# print( CheckAns.multiply( num1 = "2", num2 = "3" ) )                     # "6"
print( CheckAns.multiply( num1 = "123", num2 = "456" ) )                 # "56088"