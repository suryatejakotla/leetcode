class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = 0
        arr = [0] * k
        arr[0] = 1

        for num in nums:
            prefix = (prefix + num % k + k) % k
            res += arr[prefix]
            arr[prefix] += 1

        return res
        
        
        
        
        
        
        
        

        '''c=0
        for i in range(len(nums)):
            sum=0
            for j in range(i,len(nums)):
                sum+=nums[j]
                if sum%k==0:
                    c+=1
        return c
        '''
            
        