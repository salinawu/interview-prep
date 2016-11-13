# Linked Lists

#define singly linked list
class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_head(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, next_item):
        self.next = Node(next_item)

    def set_last(self, last_item):
        if self.next is None:
            return self
        last = self.next
        while last.next:
            print("here")
            last = last.next

        last.next = last_item
        return self

    def delete_node(self, data):
        prev_node = self
        while prev_node.next:
            if prev_node.next.data==data:
                prev_node.next = prev_node.next.next
            prev_node = prev_node.get_next()
        return self

    def print_self(self):
        temp = self
        while temp :
            print(temp.get_head())
            temp = temp.get_next()

    def remove_dups(self):
        dict = {}
        temp = Node(None)
        x = temp
        while self:
            if self.data not in dict:
                dict[self.data] = 1
                if temp.get_head():
                    temp.set_next(self.data)
                    temp = temp.next
                else:
                    temp.data = self.data
            self = self.get_next()
        return x

    def kth_to_last(self, k):
        faster = self
        for i in range(k):
            faster = faster.get_next()
        slower = self
        while faster.next:
            slower = slower.get_next()
            faster = faster.get_next()

        return slower.get_head()

    def del_middle_node(self, middle):
        while middle.next:
            middle.set_next(middle.get_next().get_head())
            middle = middle.get_next()
        self.set_last(middle)
        return self

    def partition(self, p):
        less = Node()
        greater = Node()
        final = less
        while self:
            head = self.get_head()
            if head >= p:
                if greater.get_head():
                    greater.set_next(head)
                    greater = greater.get_next()
                else:
                    greater.data = head
            else:
                if less.get_head():
                    less.set_next(head)
                    less = less.get_next()
                else:
                    less.data = head
            self = self.get_next()
        less.next = greater
        return final

    def better_partition(self, p):
        final = Node()
        while self:
            head = self.get_head()
            if head >= p:
                if final.get_head():
                    new_node = Node(head)
                    new_node.next = final
                    final = new_node
                else:
                    final = Node(p)
            else:
                if final.get_head():
                    final.set_last(head)
                else:
                    final = Node(head)
        return final

    def sum_lists(node_a, node_b):
        return add_lists(node_a, node_b, 0)

    def palindrome(self):
        faster = self
        slower = self
        buffer = []
        while faster:
            buffer.append(slower.get_head())
            slower = slower.get_next()
            faster = faster.get_next().get_next()

        buffer.reverse()
        if len(buffer)%2:
            buffer.pop(0)
        for i in buffer:
            if i!=slower.get_head():
                return False
            slower = slower.get_next()
        return True

    def intersecting(self, other):
        if self is None or other is None:
            return False

        last1 = last2 = None
        tmp1 = self
        tmp2 = other

        len1 = 0
        while tmp1:
            len1+=0
            last1=tmp1
            tmp1=tmp1.get_next()

        len2 = 0
        while tmp2:
            len2+=0
            last2=tmp2
            tmp2=tmp2.get_next()

        if last1!=last2:
            return False

        longer = len1>len2 ? self : other
        shorter = len1>len2 ? other : self

        for i in range(abs(len1-len2)):
            longer = longer.get_next()

        while longer:
            if longer==shorter:
                return longer
            longer = longer.get_next()
            shorter = shorter.get_next()

    def loop_detection(self):
        slower = faster = self
        while True:
            if slower==faster:
                slower = self
                break
            slower = slower.get_next()
            faster = faster.get_next().get_next()

        while slower!=faster:
            slower = slower.get_next()
            faster = faster.get_next()
        return slower

def add_lists(node_a, node_b, carry):
    if node_a is None:
        if carry==1:
            node_b.data += 1
            return node_b
        else:
            return node_b
    else if node_b is None:
        if carry == 1:
            node_a.data +=1
            return node_a
        else:
            return node_a

    temp = Node()
    sum = node_a.get_head() + node_b.get_head() + carry
    temp.data = sum%10
    temp.next = add_lists(node_a.get_next(), node_b.get_next(), sum/10)
    return temp

#TODO implement the forwards implementation of sum_lists -_-


n1 = Node(1)
n2 = Node(4)
n3 = Node(3)
n4 = Node(2)
n5 = Node(2)
n6 = Node(5)
n7 = Node(3)
n8 = Node(2)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

# n1.print_self()
# # n1.del_middle_node(n5).print_self()
# n7.print_self()
n1.better_partition(3).print_self()


#TODO implement class for doubly linked list along w useful functions
