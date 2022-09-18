
from typing import List


class Solution:
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        size_1 = len(nums1)
        size_2 = len(nums2)
        
        merged_list = []
        i = 0
        j = 0

        while i < size_1 and j < size_2:
            if nums1[i] < nums2[j]:
                merged_list.append(nums1[i])
                i += 1
        
            else:
                merged_list.append(nums2[j])
                j += 1
        merged_list = merged_list + nums1[i:] + nums2[j:]

        
        med=len(merged_list)//2

        if med%2==0:
            return (merged_list[med]+merged_list[med-1])/2
        else:
            return merged_list[med]

    print(findMedianSortedArrays([1,3],[2]))
    print(findMedianSortedArrays([1,2],[3,4]))
