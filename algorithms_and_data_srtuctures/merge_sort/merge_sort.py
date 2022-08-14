def merge(nums_left: list, nums_right: list) -> list:
    """
    Merge two lists after sorting them
    """
    # Creat an empty list to store the results
    merged = []
    
    # Initialize the dummy variables
    i, j = 0, 0
    
    # Append the smallest element from the two lists on after another till you finish a one
    while i < len(nums_left) and j < len(nums_right):
        if nums_left[i] < nums_right[j]:
            merged.append(nums_left[i])
            i += 1
        else:
            merged.append(nums_right[j])
            j += 1
            
    # Return the merged list with rest of the remaining of one of the lists
    return merged + nums_left[i:] + nums_right[j:]


def merge_sort(nums: list) -> list:
    """
    Sort a list using merge sort algorithm
    """
    # Compute the length of the list
    l = len(nums)
    
    # Terminating condition
    if l < 2:
        return nums
    
    # Compute the midpoint
    mid = l // 2
    
    # Sort the left and the right part recursivly
    sorted_left, sorted_right = merge_sort(nums[:mid]), merge_sort(nums[mid:])
    
    # Merge the two lists to return the sorted list
    return merge(sorted_left, sorted_right)