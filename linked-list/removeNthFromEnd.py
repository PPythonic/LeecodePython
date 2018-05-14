# coding=utf-8

"""
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first, second = head, head

        for i in range(n):
            first = first.next
        if not first:
            return head.next

        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return head