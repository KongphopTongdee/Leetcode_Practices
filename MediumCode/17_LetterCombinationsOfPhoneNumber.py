# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         ans = []
#         listPhoneNums = [ [],[ "a", "b", "c" ],[ "d", "e", "f" ],[ "g", "h", "i" ],[ "j", "k", "l" ],[ "m", "n", "o" ],[ "p", "q", "r", "s" ],[ "t", "u", "v" ],[ "w", "x", "y", "z" ],[ " " ] ]               #Expectation nums = 1,2,3,4,5,6,7,8,9,0
        
#         if( len( digits ) == 0 ):
#             return ans
        
#         for firstDigit in listPhoneNums[ int( digits[ 0 ] ) - 1 ]:
#             if ( len( digits ) > 1 ):
#                 for secondDigtit in listPhoneNums[ int( digits[ 1 ] ) - 1 ]:
                    
#                     if( len( digits ) > 2 ):
#                         for thirdDigit in listPhoneNums[ int( digits[ 2 ] ) - 1 ]:
                            
#                             if( len( digits ) > 3 ):
#                                 for fourthDigit in listPhoneNums[ int( digits[ 3 ] ) - 1 ]:
#                                     ans.append( str( firstDigit ) + str( secondDigtit ) + str( thirdDigit ) + str( fourthDigit ) )
#                             else:
#                                 ans.append( str( firstDigit ) + str( secondDigtit ) + str( thirdDigit ) )
#                     else:
#                         ans.append( str( firstDigit ) + str( secondDigtit ) )
#             else:
#                 ans.append( str( firstDigit ) )
        
#         return ans

# checkAns = Solution()
# print( checkAns.letterCombinations( "23" ) )            #Expect ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# print( checkAns.letterCombinations( "" ) )              #Expect []
# print( checkAns.letterCombinations( "2" ) )             #Expect ["a","b","c"]




# Solution with quick algorithms
# website tutorial : https://www.youtube.com/watch?v=Jobb9YUFUq0&ab_channel=vanAmsen

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Recursive function what is this????
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                output.append(combination)
            else:
                for letter in phone_map[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        output = []
        backtrack("", digits)
        return output
    
checkAns = Solution()
print( checkAns.letterCombinations( "23" ) )            #Expect ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print( checkAns.letterCombinations( "" ) )              #Expect []
print( checkAns.letterCombinations( "2" ) )             #Expect ["a","b","c"]