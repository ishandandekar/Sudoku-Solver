class Stack:
    def __init__(self) -> None:
        self.arr = []

    def push(self, number):
        self.arr.append(number)

    @property
    def stack_(self):
        return self.arr

    @property
    def length(self):
        return len(self.arr)

    def pop(self):
        if self.is_empty:
            print("The stack is empty!!!\nPush elements then try to pop")
        self.arr = self.arr[:-1]

    def get_pop(self):
        popped = self.arr[-1]
        self.pop()
        return popped

    def is_empty(self):
        return self.get_length() == 0

    def is_full(self):
        if None in self.arr:
            return False
        return True


def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(2)
    stack.push(3)
    print(stack.get_length())
    print(stack.get_stack())
    stack.pop()
    print(stack.get_stack())
    print(stack.get_pop())
    stack.push(None)
    print(stack.is_full())


if __name__ == '__main__':
    main()
