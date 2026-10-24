import sys
sys.set_int_max_str_digits(20000)

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]: #should i just cast this into a string?
        total = ""
        for n in num:
           total += str(n)
        total = int(total) + k
     
        result = [int(d) for d in str(total)]
        return result


