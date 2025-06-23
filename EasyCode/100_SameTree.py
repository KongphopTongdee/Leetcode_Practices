# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.answer = None
        
    def crateTreeNode( self, inputArr ):
        if( len( inputArr ) != 3 ):
            inputArr.append( None )
        
        headNode = TreeNode( inputArr[ 0 ] )
        headNode.left = TreeNode( inputArr[ 1 ] )
        headNode.right = TreeNode( inputArr[ 2 ] )
        
        return headNode
    
    def displayTreeNode( self, inputTreeNode ):
        displayText = f"Head node value: { inputTreeNode.val }"
        if( inputTreeNode.left != None ):
            displayText += f" Left node value: { inputTreeNode.left.val }"
        if( inputTreeNode.right != None ):
            displayText += f" Right node value: { inputTreeNode.right.val }"
        print( displayText )
    
    def isSameTree( self, p, q ):
        firstNode = self.crateTreeNode( p )
        secondNode = self.crateTreeNode( q )
        self.displayTreeNode( firstNode )
        self.displayTreeNode( secondNode )
        
checkAns = Solution()
# checkAns.isSameTree( p = [1,2,3], q = [1,2,3] )
checkAns.isSameTree( p = [1,2], q = [1,None,2] )
# checkAns.isSameTree( p = [1,2,1], q = [1,1,2] )
        