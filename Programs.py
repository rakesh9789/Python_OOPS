1. Two Sum

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        return []
       
2. Valid Palindrome

    def isPalindrome(self, s: str) -> bool:
        left,right=0,len(s)-1
        while left<right:
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()!=s[right].lower():
                return False
            left+=1
            right-=1
        return True
        

3. Palindrome Number

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left,right=0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right-=1
        return True
		
4. Remove Duplicates from Sorted Array

    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        r=1
        while r<len(nums):
            if nums[r]!=nums[r-1]:
                nums[l]=nums[r]
                r+=1
                l+=1
            else:
                r+=1
        return l


5.Remove Element

    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i
		
6.  3Sum

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=[]
        for i in range(0,len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
        
            l,r=i+1, len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total == 0:
                    result.append([nums[i],nums[l],nums[r]])

                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                
                    l+=1
                    r-=1

                elif total<0:
                    l+=1
                else:
                    r-=1
        return result

            
7.Reverse String

    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
			
8. Reverse Vowels of a String

    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        s=list(s)
        left,right=0, len(s)-1
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1 
            s[left], s[right]= s[right], s[left]
            left+=1
            right-=1
        return "".join(s)
		
9. Reverse Vowels of a String

    def reverseVowels(self, s: str) -> str:
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        s=list(s)
        left,right=0, len(s)-1
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1 
            s[left], s[right]= s[right], s[left]
            left+=1
            right-=1
        return "".join(s)
		
10. Move Zeroes

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0

        for right in range(len(nums)):
            if nums[right]!=0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
        return nums
        

