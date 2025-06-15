class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        MaxWealth = 0
        for customer in accounts:
            wealth = sum(customer)
            if wealth > MaxWealth:
                MaxWealth = wealth
        return MaxWealth