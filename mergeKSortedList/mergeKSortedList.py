#从各个list中入堆第一个元素，取出堆顶，入堆该list中下一个元素
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        
        current = sentinel = ListNode(0)
        lists = [(i.val, i) for i in lists if i]
        heapq.heapify(lists)
        while lists:
            current.next = heapq.heappop(lists)[1]
            current = current.next
            if current.next:
                heapq.heappush(lists, (current.next.val, current.next))
        return sentinel.next
