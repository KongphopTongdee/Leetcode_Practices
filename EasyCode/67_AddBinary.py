# class Solution():
#     def __init__( self ):
#         self.answer = ""
        
#     def convertToBinary( self, inputInt ):
#         numerator = ""
#         while( inputInt != 1 ):
#             numerator += str( inputInt % 2 )
#             inputInt = inputInt // 2
        
#         numerator += "1"
            
#         return numerator[::-1]
    
#     def convertToNumberic( self, inputStr ):
#         numAns = 0
#         for idx in range( len( inputStr ) ):
#             if( inputStr[ idx ] == "1" ):
#                 numAns += 2**( len( inputStr ) - idx - 1 )
            
#         return numAns
    
#     def calSummation( self, firstValue, secondValue ):
#         return firstValue + secondValue
        
#     def main( self, inputStrFirst, inputStrSecond ):
#         if( inputStrFirst == "0" ):
#             return inputStrSecond
#         elif( inputStrSecond == "0" ):
#             return inputStrFirst
#         elif( inputStrSecond == "0" and inputStrFirst == "0" ):
#             return "0"
#         firstValue = self.convertToNumberic( inputStrFirst )
#         secondValue = self.convertToNumberic( inputStrSecond )
#         summation = self.calSummation( firstValue, secondValue )
#         sumBinary = self.convertToBinary( summation )
#         return sumBinary
    
#     def addBinary( self, inputStrFirst, inputStrSecond ):
#         self.answer = self.main( inputStrFirst, inputStrSecond  )
#         return self.answer
    
# checkAns = Solution()
# checkAns.addBinary( "11", "1" )
# checkAns.addBinary( "1010", "1011" )
# checkAns.addBinary( "0", "0" )

# -------------------------------------------------------------------------------------
# Leetcode Answer

class Solution:
  def addBinary(self, a: str, b: str) -> str:
    s = []
    carry = 0
    i = len(a) - 1
    j = len(b) - 1

    while i >= 0 or j >= 0 or carry:
      if i >= 0:
        carry += int(a[i])
        i -= 1
      if j >= 0:
        carry += int(b[j])
        j -= 1
      s.append(str(carry % 2))
      carry //= 2

    return ''.join(reversed(s))

checkAns = Solution()
# checkAns.addBinary( "11", "1" )
checkAns.addBinary( "1010", "1011" )
# checkAns.addBinary( "0", "0" )