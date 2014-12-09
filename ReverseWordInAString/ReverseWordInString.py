#Given an input string, reverse the string word by word.
#
#For example,
#Given s = "the sky is blue",
#return "blue is sky the".
#!/usr/bin/python
class Solution:  
  
    # @param s, a string  
    # @return a string  
    def reverseWords(self, s):  
  
        len_s = len(s)  
        if len_s < 1:  
            return s  
  
        index_right = len_s - 1  
        new_s = ""  
        result = []
        while index_right >= 0:  
            while index_right >= 0 and ' ' == s[index_right]:  
                index_right -= 1  
            end_index = index_right  
            while index_right >= 0 and ' ' != s[index_right]:  
                index_right -= 1  
            start_index = index_right + 1  
            word = s[start_index : end_index + 1] if end_index >= 0 else ""  
            if word:
                result.append(word)  

        return ' '.join(result) 
        
def test():
    #s = "the sky is blue"
    s = ' 1'
    #s = '2 1 '
    result = Solution().reverseWords(s)
    print 'result'
    print result
if __name__ == '__main__':
    import pdb
    #pdb.set_trace()
    test()
