# class Solution:
#     def myAtoi( self, s: str ) -> int:
#         '''
        
#         '''    
#         answer = 0
#         clasifyNum = ''
#         listCheck = []
        
#         for idxString, string in enumerate( s ) :
#             if( string == ' ' ):
#                 listCheck.append( 'Space' )
#             elif( string.isalpha() == True ):
#                 listCheck.append( False )
#             else:
#                 if( ( ( s[ idxString - 1 ] == '+' and s[ idxString ] == '-' ) or ( s[ idxString - 1 ] == '-' and s[ idxString ] == '+' ) ) and ( idxString != 0 ) ):
#                     listCheck.append( False )
#                     listCheck[ idxString - 1 ] = False
#                 elif( ( string.isdigit() == True ) or ( string == '.' ) ):
#                     listCheck.append( True )
#                 elif( ( string == '-' ) or ( string == '+' ) ):
#                     listCheck.append( 'Mark' )
               
#         for idxList in range( len( listCheck ) ) :
#             if( ( listCheck[ idxList ] == True ) and ( listCheck[ idxList - 1 ] == 'Space' ) ):
#                 clasifyNum += s[ idxList ]
#             elif( listCheck[ idxList ] == True and idxList == 0 ):
#                 clasifyNum += s[ idxList ]
#             elif( ( listCheck[ idxList - 1 ] == True ) and ( listCheck[ idxList ] == 'Mark' ) and ( idxList != 0 ) ):
#                 break
#             elif( ( listCheck[ idxList ] == True ) or ( listCheck[ idxList ] == 'Mark' ) ):
#                 if( ( listCheck[ idxList ] == 'Mark' ) and ( listCheck[ idxList + 1 ] == False or listCheck[ idxList + 1 ] == 'Space' ) ):
#                     break
#                 else:
#                     clasifyNum += s[ idxList ]
#             elif( ( listCheck[ idxList ] == 'Space' ) and ( listCheck[ idxList - 1 ] == True ) and ( idxList != 0 ) ):
#                 break
#             elif( listCheck[ idxList ] == False ):
#                 break
        
#         try:
#             clasifyNum = float( clasifyNum )
#             answer = int( clasifyNum )
#         except:
#             answer = 0
        
#         return self.convertMaxMinValue( answer )
    
#     def convertMaxMinValue( self, value: int ) -> int:
#         '''
        
#         '''
#         if( value >= 2**31 ) :
#             value = ( 2**31 - 1 )
#         elif( value < -(2**31) ):
#             value = -(2**31)
#         return value
    
class Solution:
    def myAtoi(self, s: str) -> int:
        '''GuildLine : This Algorithm will get the first index that it is integer and the final index that will
        be integer value and intialize number from startIndex to endIndex
        '''
        indexStart, indexEnd = -1, -1
        result = 0
        if len( s ) == 1 and not s[ 0 ].isdigit():
            return 0
        for i in range( len( s ) ):
            if ( s[ i ] == "+" or s[ i ]== "-" ):
                if indexStart != -1:
                    if indexEnd == -1:
                        return 0
                    else:
                        break
                indexStart = i
            elif s[ i ].isdigit():
                if indexStart == -1:
                    indexStart = i
                indexEnd = i
            else:
                if indexStart == -1 and s[ i ] != ' ':
                    return result
                elif indexEnd > -1:
                    break
                elif indexStart != -1 and indexEnd == -1:
                    return 0
                else:
                    pass
        if indexStart == -1 or indexEnd == -1:
            return 0
        elif indexStart == indexEnd:
            return int( s[ indexStart ] )
        result = int( s[ indexStart : indexEnd+1 ] )
        if result < -2**31:
            return -2**31
        elif result > ( 2**31 ) - 1:
            return ( 2**31 ) - 1
        return result
    
strToInt = Solution()
print( strToInt.myAtoi( "42" ) )                    # Expected 42
print( strToInt.myAtoi( "   -42" ) )                # Expected -42
print( strToInt.myAtoi( "4193 with words" ) )       # Expected 4193
print( strToInt.myAtoi( "words and 987" ) )         # Expected 0
print( strToInt.myAtoi( "3.14159" ) )               # Expected 3
print( strToInt.myAtoi( "+-12" ) )                  # Expected 0
print( strToInt.myAtoi( "-+12" ) )                  # Expected 0
print( strToInt.myAtoi( "+1" ) )                    # Expected 1
print( strToInt.myAtoi( "   +0 123" ) )             # Expected 0
print( strToInt.myAtoi( "  -0012a42" ) )            # Expected -12
print( strToInt.myAtoi( "-5-" ) )                   # Expected -5
print( strToInt.myAtoi( "-123+" ) )                 # Expected -123
print( strToInt.myAtoi( "  +  413" ) )              # Expected 0
