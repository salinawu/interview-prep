# Why do you have to swap with the smaller element in a min-heap ordering when you remove the smallest value?
import pdb
class Node(object):
    def __init__(self, data="blank", neighbors=[]):
        self.data = data
        self.neighbors = neighbors
        self.visited = False

class Graph(object):
    def __init__(self, nodes=[]):
        self.nodes = []

    def insert(self, node):
        self.nodes.append(node)

    def remove(self, node):
        self.nodes.remove(node)

    #TODO idt this is right
    def depth_first_search(self, start, end):
        if start:
            if start.data==end.data:
                return True
            else:
                start.visited = True
                for i in start.neighbors:
                    if not i.visited:
                        return depth_first_search(self, i, end)
        return False

    def breadth_first_search(self, start, end):
        queue = Queue.Queue()
        start.visited = True
        queue.put(start)

        while not queue.empty():
            next_item = queue.get()
            if next_item.data==end.data:
                return True
            else:
                for i in next_item.neighbors:
                    if not i.visited:
                        i.visited = True
                        queue.put(i)
        return False

    def bidirectional_search(self, start, end):
        start_queue = Queue.Queue()
        end_queue = Queue.Queue()
        start.visted = end.visited = True
        start_visited = [start]
        end_visited = [end]

        while not start_queue.empty() or end_queue.empty():
            front = start_queue.get()
            back = end_queue.get()
            if front in end_visited or back in start_visited:
                return True

            for i in front.neighbors:
                if not i.visited:
                    i.visited = True
                    start_visited.append(i)
                    start_queue.put(i)
            for i in back.neighbors:
                if not i.visited:
                    i.visited = True
                    end_visited.append(i)
                    end_queue.put(i)
        return False

class BinaryTree(object):
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right

def create_min_tree(array):
    length = len(array)
    if length==1:
        return BinaryTree(array[0])
    root = BinaryTree(array[length/2])
    root.left = create_min_tree(array[0:length/2])
    root.right = create_min_tree(array[-1:length/2])
    return root

def list_of_depths(tree):
    lists = {}
    get_depths(tree, lists, 0)
    return lists

def get_depths(tree, lists, depth):
    if tree:
        if depth in lists:
            lists[depth].append(tree.root)
        else:
            lists[depth] = [tree.root]

        get_depths(tree.left, lists, depth+1)
        get_depths(tree.right, lists, depth+1)

def check_balanced(tree):
    if not tree:
        return 0

    left = check_balanced(tree.left)
    right = check_balanced(tree.right)
    if not left or not right:
        return False

    height_diff = left - right
    if abs(height_diff) > 1:
        return False
    else:
        return max(left, right) + 1

def validate_bst(tree):
    if not tree:
        return True
    return validate_edges(tree.left, None, None) and validate_edges(tree.right, None, None)

def validate_edges(tree, min, max):
    if not tree:
        return True

    if (min and tree.root <= min) or (max and tree.root > max):
        return False

    return validate_edges(tree.left, min, tree.root) and validate_edges(tree.right, tree.root, max)

# def successor(tree, node):
#     if not tree:
#         return False
#     else:
#         if node.right:
#             node = node.right
#             while node.left:
#                 node = node.left
#             return node.left
#         else:
#             while node.parent and node.parent.right!=node:
#                 node = node.parent
#             if node.parent:
#                 return node.parent
#             else:
#                 return False

def dependencies(list, pairs):
    dictionary = {}
    for i in list:
        dictionary[i] = []
    print(dictionary)
    for i in pairs:
        dictionary[i[0]].append(i[1])
    order = []
    d = dict((k, v) for k, v in dictionary.iteritems() if v==[])
    print(d)
    while dictionary:
        # pdb.set_trace()
        for k, v in d.iteritems():
            dictionary.pop(k)
            order.append(k)
        for i in dictionary:
            dictionary[i] = [x for x in dictionary[i] if x not in order]
        d = dict((k, v) for k, v in dictionary.iteritems() if v==[])
    if len(order)<len(list):
        return False
    else:
        return order

print(dependencies(["a", "b", "c", "d", "e", "f"], [["d", "a"], ["b", "f"], ["d", "b"], ["a", "f"], ["c", "d"]]))

#TODO this was a confusing one
def first_common_ancestor(tree, a, b):
    if not tree:
        return False

    if tree==a or tree==b:
        return tree

    left = first_common_ancestor(tree.left, a, b)
    right = first_common_ancestor(tree.right, a, b)

    if left and right:
        return tree

    return left ? first_common_ancestor(tree.left, a, b) : first_common_ancestor(tree.right, a, b)

#TODO bst sequences - all possible arrays. this one looked too annoying

def check_subtree(tree_a, tree_b):
    #assuming a is the bigger tree
    if not tree_a:
        return False
    if tree_a.root == tree_b.root:
        return check_subtree_helper(tree_a, tree_b)
    else:
        return check_subtree(tree_a.left, tree_b) or check_subtree(tree_a.right, tree_b)

def check_subtree_helper(tree_a, tree_b):
    if not tree_b:
        return True
    elif not tree_a:
        return False
    if tree_a.root == tree_b.root:
        return check_subtree_helper(tree_a.left, tree_b.left) and check_subtree_helper(tree_a.right, tree_b.right)
    else:
        return False

class BinSearchTree(object):
    def __init__(self, root=None, left=None, right=None):
        self.root = root
        self.left = left
        self.right = right
        self.size = 1

    def random_tree_node(self):
        if not tree:
            return self
        else:
            return random_node(self, self.size)

#TODO check if this is valid - you might have to check children for null rather than using a base case
def insert(bst, item):
    if not bst:
        return BinSearchTree(item)
    if bst.root < item:
        return insert(bst.right, item)
    else:
        return insert(bst.left, item)
    bst.size += 1

def find(bst, item):
    if not bst:
        return False
    elif bst.root == item:
        return bst
    elif bst.root > item:
        return find(bst.left, item)
    else:
        return find(bst.right, item)

def random_node(tree, i):
    size = tree ? tree.size : 0
    r = random.randint(0, size)
    left_size = tree.left ? tree.left.size : 0
    if i<left_size:
        return random_node(tree.left, i)
    elif i==left_size:
        return tree.root
    else:
        return random_node(tree.right, (i-size-1))

def countPathsWithSum(tree, target):
    if not tree:
        return False
    dictionary = {0: 1}
    return countPathsWithSumHelper(tree, target, 0, hash)

def countPathsWithSumHelper(tree, target, running_sum, hash):
    if not tree:
        return 0
    running_sum += tree.root
    if running_sum in hash:
        hash[running_sum] += 1
    else:
        hash[running_sum] = 1

    diff = running_sum - target
    total = 0
    if diff in hash:
        total += hash[diff]

    total += countPathsWithSumHelper(tree.left, target, running_sum, hash) + countPathsWithSumHelper(tree.right, target, running_sum, hash)

    hash[running_sum] -= 1
    return total
