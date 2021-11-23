class Stack: 
    def __init__(self): 
        self.items = [] 
    
    def push(self, data): 
        self.items.append(data) 
        return data 
    
    def pop(self): 
        return self.items.pop() 
        
    def peek(self): 
            return self.items[-1] 
        
    def is_empty(self): 
        return self.items==[]
    def size(self):
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    
    ## checking is_empty method -> true
    print(stack.is_empty())

    ## pushing the elements
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    ## again checking is_empty method -> false
    print(stack.is_empty())

    ## printing the topmost element of the stack -> 5
    print(stack.peek())

    ## popping the topmost element -> 5
    stack.pop()

    ## checking the topmost element using peek method -> 4
    print(stack.peek())

    ## popping all the elements
    stack.pop()
    stack.pop() 
    stack.pop() 
    stack.pop() 
    stack.push(5)
    print(stack.peek())
    ## checking the is_empty method for the last time -> true
    print(stack.is_empty())
    print(stack.size())