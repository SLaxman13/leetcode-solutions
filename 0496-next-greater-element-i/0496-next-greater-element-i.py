class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:

        ans = []

        for num1 in nums1:

            for i in range(len(nums2)):
                if nums2[i] == num1:

                    found = -1

                    for j in range(i + 1, len(nums2)):
                        if nums2[j] > num1:
                            found = nums2[j]
                            break

                    ans.append(found)
                    break

        return ans
        