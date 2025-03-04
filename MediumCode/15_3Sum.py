# from itertools import combinations

# class Solution:
#     def threeSum( self, nums: list[ int ] ) -> list[ list[ int ] ]:
#         '''
#         '''
#         ans = []
#         ansWithRepeat = []
#         indexNums = [ index for index in range( len( nums ) ) ]
#         listOfCombinationNums = self.getIndexOfCombination( indexNums )
        
#         for idxTuple, eachTuple in enumerate( listOfCombinationNums ):
#             firstIndex, secondIndex, thirdIndex = eachTuple
#             value = ( nums[ firstIndex ], nums[ secondIndex ], nums[ thirdIndex ] )
#             if( sum( value ) == 0 ):
#                 ansWithRepeat.append( list(value) )
        
#         ans = self.checkRepeatAns( ansWithRepeat )      
        
#         return ans
    
#     def getIndexOfCombination( self, listOfNums ):
#         '''
#         '''
#         return list( combinations( listOfNums, 3 ) )
    
#     def checkRepeatAns( self, ansWithRepeat ):
#         '''
#         '''
#         # Convert each sublist to a tuple and use a set to keep track of unique tuples
#         unique_set = set( tuple( sorted( sublist ) ) for sublist in ansWithRepeat )

#         # Convert back to a list of lists
#         unique_list = [ list( sublist ) for sublist in unique_set ]
        
#         return unique_list
        
        
# checkAns = Solution()
# print( checkAns.threeSum( [-1,0,1,2,-1,-4] ) )          #Expect [[-1,-1,2],[-1,0,1]]
# print( checkAns.threeSum( [0,1,1] ) )                   #Expect []
# print( checkAns.threeSum( [0,0,0] ) )                   #Expect [[0,0,0]]
# print( checkAns.threeSum( [11,3,13,-14,12,-13,14,-7,-1,14,5,-15,-11,-15,9,11,-6,-11,-15,-5,-3,5,-7,10,11,11,-10,-3,-4,8,-15,-15,-4,6,8,-6,8,7,-6,-8,6,6,-8,11,-1,8,-1,8,13,-1,-11,-5,-11,-3,12,8,-15,-13,-10,-11,3,12,11,14,3,4,-15,-4,-4,-13,-5,9,8,2,-3,-8,-12,12,-14,-14,-12,12,-12,-7,-14,8,8,9,10,13,13,-10,2,9,-10,-9,-10,12,2,1,14,13,-13,8,-8,0,7,-5,-11,0,-12,-8,-11,-8,-8,-9,-15,-15] ) ) 




# Solution with quick algorithms
# website tutorial : https://www.youtube.com/watch?v=IIxoo93bmPQ&ab_channel=AlgoEngine

class Solution:
    def threeSum( self, nums: list[ int ] ) -> list[ list[ int ] ]:
        '''
        '''
        nums.sort()
        answer = []
        for i in range( len( nums ) - 2 ):
            if i > 0 and nums[ i ] == nums[ i - 1 ]:
                continue
            l = i + 1
            r = len( nums ) - 1
            while l < r:
                total = nums[ i ] + nums[ l ] + nums [ r ]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    triplet = [ nums[ i ], nums[ l ], nums[ r ] ]
                    answer.append( triplet )
                    while l < r and nums[ l ] == triplet[ 1 ]:
                        l += 1
                    while l < r and nums[ r ] == triplet[ 2 ]:
                        r -= 1
        return answer


checkAns = Solution()
print( checkAns.threeSum( [-1,0,1,2,-1,-4] ) )          #Expect [[-1,-1,2],[-1,0,1]]
print( checkAns.threeSum( [0,1,1] ) )                   #Expect []
print( checkAns.threeSum( [0,0,0] ) )                   #Expect [[0,0,0]]
# print( checkAns.threeSum( [11,3,13,-14,12,-13,14,-7,-1,14,5,-15,-11,-15,9,11,-6,-11,-15,-5,-3,5,-7,10,11,11,-10,-3,-4,8,-15,-15,-4,6,8,-6,8,7,-6,-8,6,6,-8,11,-1,8,-1,8,13,-1,-11,-5,-11,-3,12,8,-15,-13,-10,-11,3,12,11,14,3,4,-15,-4,-4,-13,-5,9,8,2,-3,-8,-12,12,-14,-14,-12,12,-12,-7,-14,8,8,9,10,13,13,-10,2,9,-10,-9,-10,12,2,1,14,13,-13,8,-8,0,7,-5,-11,0,-12,-8,-11,-8,-8,-9,-15,-15] ) ) 