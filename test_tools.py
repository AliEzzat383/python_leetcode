from typing import*
def exist_check(nums,target):
    '''returns true if target exists in list'''
    if len(nums)>0 and target in nums:
        return True
    else:
        return False
def intersection(self, nums1, nums2):
    '''returns unique intersection between two lists'''
    return list(set(nums1) & set(nums2))
def remove_duplicates(lst):
    '''removes duplicates from list disturbing it's order'''
    return list(set(lst))
def remove_duplicates_ordered(lst):
    '''removes duplicates from list maintaining elements order'''
    return list(dict.fromkeys(lst))
def is_sorted(arr):
    '''returns true if list is sorted in ascending order'''
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
def binarysearch(nums,target):
    '''returns index of target element in list'''
    low=0
    mid=0
    high=len(nums)-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return high
def swap(a,b):
    temp=None
    temp=a
    a=b
    b=temp
    return a,b
def swap_w_in_arr_slow(a,b,arr):
    temp=None
    temp=arr[a]
    arr[a]=arr[b]
    arr[b]=temp
def swap_w_in_arr_fast(a,b,arr):
    arr[a],arr[b]=arr[b],arr[a]
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self,lst=[]):
        self.head = None
        self.lst2ll(lst)

    def lst2ll(self, lst: List[int]):
        if not lst:  # Check if the list is empty
            return None
        self.head = ListNode(lst[0])
        cur = self.head
        for item in lst[1:]:
            cur.next = ListNode(item)
            cur = cur.next
        return self.head

    def ll_print(self):
        cur = self.head
        while cur:
            print(cur.val, end="->")
            cur = cur.next
        print("None")

