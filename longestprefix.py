"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
"""
def longestCommonPrefix(strs):
        prefix = ""
        if len(strs) > 0:
            for i in range(len(min(strs))):
                new_prefix = prefix + strs[0][i]
                for j in range(len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return prefix
                prefix = new_prefix
        return prefix

def main():
    print(longestCommonPrefix(['dog','racecar','car']))

if __name__=='__main__':
    main()