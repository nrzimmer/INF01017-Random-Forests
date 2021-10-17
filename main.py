#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tree.node import TreeNode

def main():
    root = TreeNode('root')
    branch = TreeNode('branch')
    root.addChild(1, branch)
    leaf = TreeNode('leaf', 'true')
    branch.addChild('1', leaf)
    return

if __name__ == '__main__':
    main()