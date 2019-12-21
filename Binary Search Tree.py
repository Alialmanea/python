
from random import randint
import random

class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

def insert(root,node):
    if root is None:
         root=node
    else:
        if root.data>node.data:
            if root.left is None:
                root.left=node
            else:
                insert(root.left,node)
        else:
            if root.right is None:
                root.right=node
            else:
                insert(root.right,node)


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def preorder(root):
    if root:
        print(root.data,end=" ")
        preorder(root.left)
        preorder(root.right)


def main():
    '''
  BinarySearchTree1
    50
  /	   \
 30	   70
 / \   / \
20 40 60 80
    '''

    BinarySearchTree1=Node(50)

    insert(BinarySearchTree1,Node(30))
    insert(BinarySearchTree1, Node(20))
    insert(BinarySearchTree1, Node(40))
    insert(BinarySearchTree1, Node(70))
    insert(BinarySearchTree1, Node(60))
    insert(BinarySearchTree1, Node(80))

    print ("İnOrder",end=":")
    inorder(BinarySearchTree1)
    print()
    print("PostOrder", end=":")
    postorder(BinarySearchTree1)
    print()
    print("Preorder", end=":")
    preorder(BinarySearchTree1)

    '''
     Built BinarySearchTree2 with Random Node from 0 to 100  
    '''
    random.seed()

    BinarySearchTree2 = Node(random.randrange(0,100))

    for _ in range(10):
        insert(BinarySearchTree2,Node(random.randrange(0,100)))

    print()
    print("BinarySearchTree2:")
    print ("İnOrder",end=":")
    inorder(BinarySearchTree2)
    print()
    print("PostOrder", end=":")
    postorder(BinarySearchTree2)
    print()
    print("Preorder", end=":")
    preorder(BinarySearchTree2)


if __name__ == '__main__':
    main()