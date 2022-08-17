def findSublists(nums):
    """
    Check a list and device into two sublists that sum equal to each other
    :param nums: parent list
    :return: True False
    """
    parentsize = sum(nums) / 2
    for i in range(len(nums)):
        sumlist = 0
        for j in range(i, len(nums)):
            sumlist += nums[j]
            if sumlist == parentsize and len(nums[i:j + 1]) == len(nums) / 2:
                return True
    return False


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(findSublists(nums))

# output = nums[i:j + 1]
# print("nums", nums[i:j + 1])
# sublist = []
# for item in nums:
#     if item not in output:
#         sublist.append(item)
# print("sublist", sublist)
