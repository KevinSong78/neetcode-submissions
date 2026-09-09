class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #We can use a hash set to efficiently keep track of the values we have already encountered.As we iterate through the array, we check whether the current value is already present in the set. If it is, that means we've seen this value before, so a duplicate exists.Using a hash set allows constant-time lookups, making this approach much more efficient than comparing every pair.
        seen_hash = set()
        for num in nums:
            if num in seen_hash:
                return True
            seen_hash.add(num)
        return False