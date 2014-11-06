#!/usr/bin/python
import time,os,sys
class Solution:
  def two_min(self,one,two):
    if one< two : return one
    return two
  # @param num, a list of integer
  # @return an integer
  def findMin(self, num):
    length = len(num)
    #print num
    if length == 1 or  num[0] < num[length-1]: return num[0]
    if length ==2:
      return self.two_min(num[0],num[1])
    else:
      mid = length/2 +1
      min1 = self.findMin(num[:mid])
      min2 = self.findMin(num[mid:])
      return self.two_min(min1,min2)
        
    
def rotated(list_num, pivot):
  one = list_num[pivot+1:len(list_num)]
  two = list_num[:pivot+1]
  return one+two
def main():
  list_num = [0, 1, 2, 4 ,5 ,6 ,7]
  pivotPos = 5
  rotated_list = rotated(list_num,pivotPos)
  print 'rotated list:',rotated_list
  #return
  res = Solution().findMin(rotated_list)
  return res
if __name__ == '__main__':
    sys.path.append(".")
    start = time.time()
    import pdb
    #pdb.set_trace()
    res = main()
    print res
    elapse = time.time() - start

    print 'time:%d'%elapse
