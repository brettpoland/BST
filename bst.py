class BSTNode:
    def __init__(self, val: int=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val: str):
        """[Uses Binary Search Tree Algorithm to insert Data]

        Args:
            val (int): [int Value for binary tree insertion 1]
        """        
        if not self.val:
            self.val = val
            return
        
        if self.val ==  val:
            return 
        
        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val

    def delete(self, val):
        if self == None:
            return self
        
        if val < self.val:
            self.left = self.left.delete(val)
            return self
        if val > self.val:
            self.right = self.left.delete(val)
            return self
        if self.right == None:
            return self.left
        if self.left == None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.val = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)

        return self

    def exists (self, val):
        if val == self.val:
            return True

        if val < self.val:
            if self.left == None:
                return False
            return self.left.exists(val)

        if self.right == None:
            return False
        return self.right.exists(val)

    def inorder (self, vals):
        if self.left is not None:
            self.left.inorder(vals)
        if self.val is not None:
            vals.append(self.val)
        if self.right is not None:
            self.right.inorder(vals)
        return vals

    def preorder(self, vals):
        if self.val is not None:
            vals.append(self.val)
        if self.left is not None:
            self.left.preorder(vals)
        if self.right is not None:
            self.right.preorder(vals)
        return vals

    def postorder(self, vals):
        if self.left is not None:
            self.left.postorder(vals)
        if self.right is not None:
            self.right.postorder(vals)
        if self.val is not None:
            vals.append(self.val)
        return vals

def base_set():
    
    n = input("Enter number set: ")
    base_set.base = n.split()
    return base_set.base    

def display():
    nums = base_set.base

    for num in nums:
        bst.insert(num)
    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

def get_menu_choice():
    def print_menu():       
        print(30 * "-", "Options", 30 * "_")
        print("1. Enter value for entry")
        print("2. Enter value for deletion")
        print("3. Display orders")
        print("4. Re-enter base values for tree")
        print("5. Exit")
        print(80 * "-")

    loop = True
    int_choice = -1

    while loop:       
        print_menu()    
        choice = input("Enter your choice [1-5]: ")

        if choice == '1':
            add_int = input("Enter value to add:")
            bst.insert(add_int)
            int_choice = 1
            loop = True
        elif choice == '2':
            remove_int = input("Enter value to delete: ")
            bst.delete(remove_int)
            loop = True
        elif choice == '3':
            choice = ''
            display()
            int_choice = 3
            loop = True
        elif choice == '4':
            base_set()
            int_choice = 4
            loop = True
        elif choice == '5':
            int_choice = -1
            print("Exiting..")
            loop = False  
        else:
            input("Wrong menu selection. Enter any key to try again..")
    return [int_choice, choice]


if __name__ == "__main__":
    bst = BSTNode()
    base_set()
    get_menu_choice()

