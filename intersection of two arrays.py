from collections import Counter


def intersection_of_two_arrays(nums1, nums2):
    store = nums1
    ans = []
    for i in range(len(nums2)):
        if nums2[i] in store:
            ans.append(nums2[i])
            store.remove(nums2[i])
    return ans


print(intersection_of_two_arrays([4, 7, 9, 7, 6, 7], [5, 0, 0, 6, 1, 6, 2, 2, 4]))
