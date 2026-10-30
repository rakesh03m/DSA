class Solution:
    def sortColors(self, nums: list[int]) -> None:
#     l = len(nums) -1
#     i = 0
#     j = i + i
#     while (j<l):
#         if (nums[i] > nums[j]):
#             nums[i], nums[j] =  nums[j], nums[i]
#             j += 1
#     return nums


        l = len(nums) - 1
        i = 0
        j = 0

        while j <= l:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1

            elif nums[j] == 1:
                j += 1

            else:
                nums[j], nums[l] = nums[l], nums[j]
                l -= 1

        return nums

        # l = len(nums) - 1
        # i = 0
        # j = 0
        # while(j<=l):
        #     if (nums[j] == 0):
        #         nums[i],nums[j] = nums[j],nums[i]
        #         i += 1
        #         j += 1
        #     elif(nums[j] == 1):
        #         j += 1
        #     else:
        #         nums[j],nums[l] = nums[l],nums[j]
        #         l -= 1
        # return nums
