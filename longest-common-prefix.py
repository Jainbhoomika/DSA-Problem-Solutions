class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        common_prefix = ""
        index = 0
        min_len = len(min(strs, key=len))
        while index < min_len:
            flag = 0
            for i in range(len(strs)-1):
                if strs[i][index] != strs[i+1][index]:
                    return common_prefix

            common_prefix += strs[i][index]
            index +=1

        return common_prefix               
        



            
        
