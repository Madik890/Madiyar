def spy_game(nums):
    return '0' in map(str, nums) and '0' in map(str, nums[nums.index(0)+1:]) and '7' in map(str, nums[nums.index(0)+2:])
