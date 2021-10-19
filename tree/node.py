# -*- coding: utf-8 -*-

from typing import Any


class TreeNode:
    def __init__(self, name: Any, value: str = ""):
        self.Parent: 'TreeNode' or None = None
        self.Childs: dict[Any, 'TreeNode'] = {}
        self.Value: str = value
        self.Name: Any = name

    def addChild(self, child: 'TreeNode') -> None:
        self.Childs[child.Name] = child
        child.setParent(self)

    def setParent(self, parent: 'TreeNode') -> None:
        self.Parent = parent

    def isRoot(self) -> bool:
        return self.Parent is None
