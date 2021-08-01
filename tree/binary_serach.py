class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(node: Node, value: int) -> Node:
    if node is None:
        return Node(value)

    if value < node.value:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node

def inorder(node:Node) ->None:
    # inorder：left→root→right
    if node is not None:
        inorder(node.left)
        # 再帰
        print(node.value)
        inorder(node.right)

def search(node:Node,value:int)->bool:

    if node is None:
        return False

    if node.value ==value:
        return True

    elif node.value >value:
        return search(node.left,value)

    elif node.value<value:
        return search(node.right,value)



if __name__ == '__main__':
    root = None
    root = insert(root, 3)
    root = insert(root, 6)
    root = insert(root, 5)
