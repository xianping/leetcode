#!/usr/bin/python
import time,sys,operator
class Stack:
  def __init__(self):
    self.__storage = []

  def isEmpty(self):
    return len(self.__storage) == 0

  def push(self,p):
    self.__storage.append(p)

  def pop(self):
    return self.__storage.pop()

  def top(self):
    return self.__storage[-1]
  def __str__(self):
    return ','.join(map(str,self.__storage))
class MinStack:
    s1 = Stack()
    s2 = Stack() #store history min element
    def __min(self):
        return self.s2.top()
    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.s2.isEmpty():
            min = self.__min()
            if x< min:
                self.s2.push(x)
            else:
                self.s2.push(min)
        else: #first input
            self.s2.push(x)

        self.s1.push(x)
        

    # @return nothing
    def pop(self):
        self.s2.pop()
        return self.s1.pop()
        

    # @return an integer
    def top(self):
        return self.s1.top()

    # @return an integer
    def getMin(self):
        return self.s2.top()
        
def test():
    st = MinStack()
    st.push(2)
    print st.getMin() == 2
    st.push(1)
    print st.getMin() == 1
    st.push(3)
    print st.getMin() == 1
    st.pop()
    print st.getMin() == 1
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    test()
