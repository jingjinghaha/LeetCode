'''
Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5
Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
'''
# use a max queue to sort the val together with the frequency, which can be regarded as a priority queue
# push: O(lgn), update the max queue
# pop: O(n), find the val to pop in the max queue and decrease the frequency by 1, if frequency become 0, delete it
# top: O(1)
# peekMax: O(1)
# popMax: O(n), seach the max val in the stack then delete it
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_q = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        import bisect
        self.stack.append(x)
        pos = bisect.bisect_left(self.max_q, [x, 1])
        if pos >= len(self.max_q):
            self.max_q.append([x, 1])
        else:
            if x != self.max_q[pos][0]:
                bisect.insort(self.max_q, [x, 1])
            else:
                self.max_q[pos][1] += 1

    def pop(self):
        """
        :rtype: int
        """
        ans = self.stack.pop()
        import bisect
        pos = bisect.bisect_left(self.max_q, [ans, 1])
        self.max_q[pos][1] -= 1
        if self.max_q[pos][1] == 0:
            del self.max_q[pos]
        return ans

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_q[-1][0]

    def popMax(self):
        """
        :rtype: int
        """
        max = self.max_q[-1][0]
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == max:
                self.stack = self.stack[:i] + self.stack[i+1:]
                break
        self.max_q[-1][1] -= 1
        if self.max_q[-1][1] == 0:
            self.max_q.pop()
        return max

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()



# just use one stack, and one variable to track the current max value
# push: O(1)
# pop: O(n)
# top: O(1)
# peekMax: O(1)
# popMax: O(n)
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max = -sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x > self.max:
            self.max = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: int
        """
        res = self.stack.pop()
        if res == self.max:
            self.max = self.findMax()
        return res
    
    def findMax(self):
        if not self.stack:
            return -sys.maxint
        return max(self.stack)

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max

    def popMax(self):
        """
        :rtype: int
        """
        res = self.max
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == self.max:
                self.stack = self.stack[:i] + self.stack[i+1:]
                break
        self.max = self.findMax()
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
