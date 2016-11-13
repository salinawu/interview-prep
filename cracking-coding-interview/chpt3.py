#represent 3 stacks with an array
class Stacks(object):
    def __init__(self, space=10):
        self.array = [-1]*space
        self.free = 0
        self.first = {'prev': [], 'curr': 0}
        self.second = {'prev': [], 'curr': 0}
        self.third = {'prev': [], 'curr': 0}

    def push_first(self, item):
        if self.full():
            return False

        self.first['prev'].append(free)
        self.array[free] = item
        self.free = self.array.index(-1)

    def push_second(self, item):
        if self.full():
            return False

        self.second['prev'].append(free)
        self.array[free] = item
        self.free = self.array.index(-1)

    def push_third(self, item):
        if self.full():
            return False

        self.third['prev'].append(free)
        self.array[free] = item
        if not self.full():
            self.free = self.array.index(-1)
        else:
            self.free = False

    def pop_first(self):
        self.array[self.first['prev']] = -1
        self.first['prev'].pop()
        self.free = self.array.index(-1)

    def pop_second(self):
        self.array[self.second['prev']] = -1
        self.second['prev'].pop()
        self.free = self.array.index(-1)

    def pop_second(self):
        self.array[self.second['prev']] = -1
        self.second['prev'].pop()
        self.free = self.array.index(-1)

    def full(self):
        return -1 not in self.array


class StackMin(object):
    def __init__(self):
        self.stack = []

    def push(self, item):
        if self.stack==[]:
            self.stack = [[item, item]
        else
            minimum = min(self.stack[-1][1], item)
            self.stack.append([item, minimum])

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def min(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return "nothing in stack"

class SetOfStacks(object):
    def __init__(self, capacity=10):
        self.stacks = []
        self.capacity = capacity

    def push(self, item):
        if len(self.stacks[-1]) >= self.capacity:
            self.stacks.append([item])
        else:
            self.stacks[-1].append(item)

    def pop(self):
        self.stacks[-1].pop()
        if self.stacks[-1]==[]:
            return self.stacks.pop()

    def popAt(self, index):
        popped = self.stacks[index].pop()
        for i in range(index...len(self.stacks)):
            self.stacks[i].append(self.stacks[i+1].pop(0))
        return popped

class QueueViaStacks(object):
    def __init__(self):
        self.first_stack = []
        self.second_stack = []

    def push(self, item):
        self.first_stack.append(item)

    def pop(self):
        if self.second_stack==[]:
            if self.first_stack==[]:
                return "no items to pop"
            else:
                while self.first_stack:
                    self.second_stack.append(self.first_stack.pop())
        return self.second_stack.pop()

#TODO i misread the question..
class SortStack(object):
    def __init__(self):
        self.stack = []

    def peek(self):
        return self.stack[-1]

    def pop(self):
        return self.stack.pop()

    def push(self, item):
        tmp = []
        while item > self.peek():
            tmp.append(self.pop())

        self.stack.append(item)

        while tmp:
            self.stack.append(tmp.pop())

class Animal(object):
    def __init__(self, type):
        if type:
            self.type = type
            self.order = None
        else:
            return "error: pls specify animal type"

class AnimalShelter(object):
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0

    def enqueue(animal):
        animal.order = self.order
        if animal.type=="dog":
            self.dogs.append(animal)
        elif animal.type=="cat":
            self.cats.append(animal)
        else:
            return "sorry - this shelter only supports dogs and cats"
        self.order += 1

    def dequeueDog(self):
        return self.dogs.pop(0)

    def dequeueCat(self):
        return self.cats.pop(0)

    def dequeueAny(self):
        return self.cats[0].order > self.dogs[0].order ? self.dogs.pop(0) : self.cats.pop(0)
