from collections import Counter
from math import ceil

def your_function_name(nums):
    cnt = Counter(nums)
    for max_group_size in range(min(cnt.values()) + 1, 0, -1):
        total_groups = 0
        for num in cnt.keys():
            groups = ceil(cnt[num] / max_group_size)
            if groups * max_group_size >= cnt[num] and groups * (max_group_size - 1) <= cnt[num]:
                total_groups += groups
            else:
                # add 1e9 summy value to mark that this max_group_size is impossible
                total_groups += 1e9
        if total_groups < 1e9: 
            return total_groups

# Example usage:
nums = [1, 2, 2, 2, 3, 3, 4]
result = your_function_name(nums)
print(result)
