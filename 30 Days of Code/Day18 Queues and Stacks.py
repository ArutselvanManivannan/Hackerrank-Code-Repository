# https://www.hackerrank.com/challenges/30-queues-stacks/problem


from collections import deque
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = deque()
        self.queue = deque()

    def pushCharacter(self, char):
        self.stack.appendleft(char)

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        return self.stack.popleft()

    def dequeueCharacter(self):
        return self.queue.popleft()

# github.com/ArutselvanManivannan
