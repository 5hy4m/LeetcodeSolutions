class Solution(object):
    def containsDuplicate(self, nums):
        visited_elements = {}
        p1 = 0
        p2 = len(nums) -1
        if len(nums) <=1:
            return False
        
        while p1<=p2:
            try:
                visited_elements[nums[p1]]
                return True
            except:
                if p1 != p2:
                    visited_elements[nums[p1]] = p1
                p1+=1
                
            try:
                visited_elements[nums[p2]]
                return True
            except:
                visited_elements[nums[p2]] = p2
                p2-=1
        return False