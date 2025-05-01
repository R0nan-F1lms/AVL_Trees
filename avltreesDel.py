import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.height = 1  # Initially, height of a node is 1 when it's just inserted

class AVLTree:
    def __init__(self):
        self.root = None
        self.step = 0  # This tracks the step of insertions or rotations
        self.imbalanced_node = None  # To track the imbalanced node during rotation

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Update height of this ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Get the balance factor to check if we need rotation
        balance = self.getBalance(root)

        # Left heavy case (Right rotation)
        if balance > 1 and key < root.left.key:
            self.imbalanced_node = root
            return self.rightRotate(root)

        # Right heavy case (Left rotation)
        if balance < -1 and key > root.right.key:
            self.imbalanced_node = root
            return self.leftRotate(root)

        # Left-Right case (Left then Right rotation)
        if balance > 1 and key > root.left.key:
            self.imbalanced_node = root
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        # Right-Left case (Right then Left rotation)
        if balance < -1 and key < root.right.key:
            self.imbalanced_node = root
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        self.step += 1
        self.plot(self.root, rotation_type="Left")
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        self.step += 1
        self.plot(self.root, rotation_type="Right")
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def visualize(self, root, pos=None, parent=None, graph=None):
        if graph is None:
            graph = nx.DiGraph()

        if root is not None:
            graph.add_node(root.key, label=f"{root.key}\nH:{root.height}")
            if parent is not None:
                graph.add_edge(parent.key, root.key)
            self.visualize(root.left, pos, root, graph)
            self.visualize(root.right, pos, root, graph)
        return graph

    def plot(self, root, rotation_type=None, node_to_delete=None):
        graph = self.visualize(root)

        # Define a grid layout to arrange nodes in top-down fashion
        pos = self.grid_layout(graph)

        # Create the figure and adjust its size for compactness
        plt.figure(figsize=(10, 8))  # Smaller, more compact size
        nx.draw(graph, pos, with_labels=True, arrows=True, node_size=3000, node_color="skyblue", font_size=10, font_weight='bold')

        # Annotating with height and operation step
        node_labels = nx.get_node_attributes(graph, 'label')
        nx.draw_networkx_labels(graph, pos, labels=node_labels, font_size=12, font_weight='bold')

        # Step text
        step_text = f"Step {self.step}: "
        if rotation_type:
            step_text += f"{rotation_type} Rotation"
        else:
            step_text += f"Inserting node"

        # Add the step text to the plot
        plt.text(0.5, 1.1, step_text, horizontalalignment='center', verticalalignment='bottom', fontsize=14, weight='bold')

        # Add the imbalanced node if available
        if self.imbalanced_node:
            plt.text(0.5, 1.0, f"Imbalance at node {self.imbalanced_node.key}", horizontalalignment='center', verticalalignment='bottom', fontsize=12, color="red", weight='bold')

        # Highlight node to be deleted if any
        if node_to_delete:
            plt.text(pos[node_to_delete][0], pos[node_to_delete][1] + 0.2, f"Deleting node {node_to_delete}", fontsize=12, color="red", fontweight="bold")

        # Use tight_layout to ensure everything fits in the figure
        plt.tight_layout()

        # Adjusting layout to avoid text being covered
        plt.subplots_adjust(top=0.85, bottom=0.15, left=0.05, right=0.95)

        # Show operation step
        plt.show()

    def grid_layout(self, graph):
        # Grid layout to arrange nodes in top-down fashion
        pos = {}
        level = 0  # Set level for y-positioning (root starts at the top)
        x_offset = 0  # Horizontal offset for spacing
        node_spacing = 2  # Horizontal spacing between nodes
        queue = [(self.root, 0)]  # Start from the root node

        while queue:
            node, x = queue.pop(0)
            pos[node.key] = (x, -level)  # Negative y to display top-down

            if node.left:
                queue.append((node.left, x - node_spacing))
            if node.right:
                queue.append((node.right, x + node_spacing))

            # Increment level for the next depth
            level += 1

        return pos

    def delete(self, root, key):
        # Step 1: Perform normal BST delete
        if root is None:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node to be deleted has been found

            # Case 1: Node has no children (leaf node)
            if root.left is None and root.right is None:
                return None

            # Case 2: Node has one child
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Case 3: Node has two children
            else:
                # Get the in-order predecessor (largest element smaller than the node)
                temp = self.getMax(root.left)
                root.key = temp.key
                root.left = self.delete(root.left, temp.key)

        # Update height and check balance
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        balance = self.getBalance(root)

        # Rotate to maintain AVL property
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)

        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)

        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)

        return root

    def getMax(self, root):
        while root.right:
            root = root.right
        return root

# Test the AVL Tree with visualization
avl = AVLTree()

# Insert nodes into the AVL Tree
keys_to_insert = [20, 9, 3, 7, 5, 8, 25, 30, 15, 6, 17]

# Insert nodes and visualize the tree after each insertion and rotation
for key in keys_to_insert:
    avl.root = avl.insert(avl.root, key)
avl.plot(avl.root)

# Deleting nodes
keys_to_delete = [20, 15, 8, 25, 30, 9, 17, 5, 6, 3, 7]
for key in keys_to_delete:
    print(f"Deleting {key}")
    avl.plot(avl.root, node_to_delete=key)
    avl.root = avl.delete(avl.root, key)
    avl.plot(avl.root)
