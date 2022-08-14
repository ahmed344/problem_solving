def binary_search(nums: list, target: int) -> int:
    """
    search in sorted list
    """ 
    mid = len(nums) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] > target:
        return binary_search(nums[:mid], target)
    else:
        return mid + binary_search(nums[mid:], target)