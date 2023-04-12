from binarytree import build, Node

# Construct a binary tree from a list of integers
data = [5, 3, 7, 1, 4, 6, 8]
root = build(data)

# Print the initial binary tree
print("Initial Binary Tree:")
print(root)

while True:
    # Ask the user for their choice
    print("\nChoose an option:")
    print("1. Add a new element")
    print("2. Delete an element")
    choice = int(input())

    if choice == 1:
        # Ask the user for the value of the new element
        value = int(input("Enter the value of the new element: "))

        # Add the new element to the binary tree
        root = Node(value)
        root.left = build(data[:len(data)//2])
        root.right = build(data[len(data)//2+1:])
        
        # Print the updated binary tree
        print("\nUpdated Binary Tree:")
        print(root)
        
    elif choice == 2:
        # Ask the user for the value of the element to be deleted
        value = int(input("Enter the value of the element to be deleted: "))

        # Find and delete the node with that value from the binary tree
        def delete_node(node):
            if node is None:
                return None
            
            if node.value == value:
                if node.left is None and node.right is None:
                    return None
                
                if node.left is None:
                    return node.right
                
                if node.right is None:
                    return node.left
                
                min_node = node.right
                while min_node.left is not None:
                    min_node = min_node.left
                
                node.value = min_node.value
                node.right = delete_node(node.right)
                
            elif value < node.value:
                node.left = delete_node(node.left)
                
            else:
                node.right = delete_node(node.right)
            
            return node
        
        root = delete_node(root)
        
        # Print the updated binary tree
        print("\nUpdated Binary Tree:")
        print(root)
        
    else:
        print("Invalid choice. Please try again.")