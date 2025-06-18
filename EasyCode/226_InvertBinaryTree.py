# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__( self ):
        self.answer = None
        
    def display( self, treeNodeInsert ):
        """ Output template
            Head node: x
            child node left: x.left
            child node right: x.right
        """
        def outputTemplate( treeNodeDisplay ):
            displayOutput = f" Head node: { current.val } \n child node left: { current.left.val } \n child node right: { current.right.val }  \n"
            print( displayOutput )
        
        current = treeNodeInsert
        outputTemplate( current )
        
        storeTreeNode = {  }
        
        # Not sure create with function when do it again
        while( ( current.left != None ) or ( current.right != None )  ):
            if( ( current.left == None ) and ( current.right != None ) ):
                outputTemplate( current.right )
                current = current.right
            elif( ( current.left != None ) and ( current.right == None ) ):
                outputTemplate( current.left )
                current = current.left
            elif( ( current.left != None ) and ( current.right != None ) ):
                outputTemplate( current.left )
                storeTreeNode.update( { "right": current.right } )
                current = current.left
            
        # Another loop function for search next branch
            
        
        
    
    def invertTree( self, root ):
        self.display( root )

# FirstQuestion
TreeNodeFirstQuestion = TreeNode( 4 )  
TreeNode_2 = TreeNode( 2 )
TreeNode_7 = TreeNode( 7 )
TreeNode_1 = TreeNode( 1 )
TreeNode_3 = TreeNode( 3 )
TreeNode_6 = TreeNode( 6 )
TreeNode_9 = TreeNode( 9 )

TreeNode_2.left = TreeNode_1
TreeNode_2.right = TreeNode_3

TreeNode_7.left = TreeNode_6
TreeNode_7.right = TreeNode_9

TreeNodeFirstQuestion.left = TreeNode_2
TreeNodeFirstQuestion.right = TreeNode_7

# SecondQuestion
TreeNodeSecondQuestion = TreeNode( 2 )
TreeNodeSecondQuestion.left = TreeNode( 1 )
TreeNodeSecondQuestion.right = TreeNode( 3 )
    
checkAns = Solution()
checkAns.invertTree( TreeNodeFirstQuestion )            # Ans: [4,7,2,9,6,3,1]
# checkAns.invertTree( TreeNodeSecondQuestion )           # Ans: [2,3,1]
# checkAns.invertTree( [] )                               # Ans: []
