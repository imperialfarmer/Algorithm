# -*- using: utf-8 -*-
import numpy as np
import sys

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        print('new Node with ' + str(data))

# Insersion for BST
def Insert(root, data):
    if root == None:
        root = BSTNode(data)
        print('end recursive')
    else:
        if data <= root.data:
            print( str(data) + ' Left to ' + str(root.data) )
            root.left = Insert(root.left, data)
            # input()
        else:
            print( str(data) + ' Right to ' + str(root.data) )
            root.right = Insert(root.right, data)
            # input()
    return root

# Search algorithm for BST
def Search(root, data):
    if root == None:
        print('Not Found', data)
    elif root.data == data:
        print('Found ', data)
    elif data < root.data:
        Search(root.left, data)
    else:
        Search(root.right, data)

def CheckTree(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        return
    elif root.left == None:
        print('* ' + str(root.data) + ' : L-  R' + str(root.right.data) + '\n')
    elif root.right == None:
        print('* ' + str(root.data) + ' : L' + str(root.left.data) + ' R- \n')
    
    else:
        print('* ' + str(root.data) + ' : L' + str(root.left.data) + ' R' + str(root.right.data) + '\n')
        CheckTree(root.left)
        CheckTree(root.right)

def FindMinimum(root):
    current = root
    while current.left is not None:
        current = current.left
    return current

def FindMaximum(root):
    if root.right == None:
        print('MAX ROOT')
        print(root)
        print(root.data)
        return root
    else:
        CheckTree(root.right)
        FindMaximum(root.right)


def Deletion(root,data):
    # locate the address
    if root == None:
        print('Not Found', data)
        return root
    elif data < root.data:
        root.left = Deletion(root.left, data)
    elif data > root.data:
        root.right = Deletion(root.right, data)
    else:
        print(root)
        if root.left == None:
            temp = root.right
            root = None
            return temp
        elif root.right == None:
            temp = root.left
            root = None
            return temp
        else:
            temp = FindMinimum(root.right)
            root.data = temp.data
            root.right = Deletion(root.right,temp.data)

        return root


def main():
    array = [12,5,15,3,7,13,17,1,9]

    print('---- build tree ----')
    root = None
    for num in array:
        root = Insert(root, num)
    print('\n')

    print('---- search tree ----')
    Search(root, 20)
    Search(root, 7)
    print('\n')

    print('---- check tree ----')
    CheckTree(root)
    print('\n')


    # print('---- minimum and maximum of tree ----')
    # minimumPos = FindMinimum(root)
    # print('Minimum')
    # print(minimumPos)
    # maximumPos = FindMaximum(root)
    # print('Maximum')
    # print(maximumPos)
    # # print('Minimum = ', FindMinimum(root).data)
    # print('\n')

    print('---- deletion in tree ----')
    Deletion(root,12)
    CheckTree(root)


if __name__ == '__main__':
    main()
