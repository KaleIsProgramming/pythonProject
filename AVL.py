class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_bst(root.left, val)
    else:
        root.right = insert_bst(root.right, val)
    return root

def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

def inorder_traversal(root, arr):
    if root:
        inorder_traversal(root.left, arr)
        arr.append(root.val)
        inorder_traversal(root.right, arr)

def build_avl(arr):
    if not arr:
        return None
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    root.left = build_avl(arr[:mid])
    root.right = build_avl(arr[mid+1:])
    return root

# Funkcja do wyświetlania drzewa (do celów testowych)
def print_tree(root, level=0):
    if root:
        print_tree(root.right, level + 1)
        print("  " * level + str(root.val))
        print_tree(root.left, level + 1)

# Tworzenie drzewa BST
bst_root = None
bst_values = [5, 3, 8, 2, 4, 7, 9, 12, 34, 54,23 ,1, 43 ,1235]
for val in bst_values:
    bst_root = insert_bst(bst_root, val)

print("Drzewo BST:")
print_tree(bst_root)

# Wysokość drzewa BST
bst_height = height(bst_root)
print("Wysokość drzewa BST:", bst_height)

# Odczytanie elementów drzewa BST w porządku inorder
bst_inorder = []
inorder_traversal(bst_root, bst_inorder)
print("Elementy drzewa BST w porządku inorder:", bst_inorder)

# Konstrukcja drzewa AVL
avl_root = build_avl(bst_inorder)

print("\nDrzewo AVL:")
print_tree(avl_root)

# Wysokość drzewa AVL
avl_height = height(avl_root)
print("Wysokość drzewa AVL:", avl_height)