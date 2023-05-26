# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.
# A customer's wealth is the amount of money they have in all their bank accounts. 
# The richest customer is the customer that has the maximum wealth.

from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
    
# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         richest = 0
#         for wealth in accounts:
#             richest = max(sum(wealth), richest)
#         return richest

# class Solution:
#     def maximumWealth(self, accounts: List[List[int]]) -> int:
#         customers = []
#         richest = 0

#         for i in accounts:
#             customer = sum(i)
#             customers.append(customer)
        
#         for wealth in customers:
#             if wealth >= richest:
#                 richest = wealth

#         return richest