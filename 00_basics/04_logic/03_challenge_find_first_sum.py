"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

nums = [4, 5, 6, 2]
goal = 8

def find_first_sum(nums, goal):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == goal:
                return [i, j]
            
    return None
print(find_first_sum(nums, goal))  # [2, 3]

# vamos a hacer el ejercicio con diccionarios para optimizar la busqueda
def find_first_sum_optimized(nums, goal):
    num_indices = {}
    
    for index, num in enumerate(nums):
        complement = goal - num
        if complement in num_indices:
            return [num_indices[complement], index]
        num_indices[num] = index
    
    return None

print(find_first_sum(nums, goal))