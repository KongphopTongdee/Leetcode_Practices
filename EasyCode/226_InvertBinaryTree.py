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
            displayOutput = f" \n Head node: { treeNodeDisplay.val }"
            if( treeNodeDisplay.left != None ):
                displayOutput += f" \n child node left: { treeNodeDisplay.left.val }"
            if( treeNodeDisplay.right != None ):
                displayOutput += f" \n child node right: { treeNodeDisplay.right.val }"
            print( displayOutput )
            
        def findAllLeftTreeNode( inputTreeNode ):
            idxCount = 0
            while( ( inputTreeNode.val != 0 ) ):
                outputTemplate( inputTreeNode )
                if( inputTreeNode.right != None ):
                    idxCount += 1
                    storeTreeNode.update( { idxCount : inputTreeNode.right } )
                if( inputTreeNode.left != None ):
                    inputTreeNode = inputTreeNode.left
                else:
                    break
                
        current = treeNodeInsert
        storeTreeNode = {  }
        findAllLeftTreeNode( current )
        
        while( storeTreeNode != {} ):
            popDict = storeTreeNode.popitem()
            findAllLeftTreeNode( popDict[ len( popDict ) - 1 ] )
    
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
