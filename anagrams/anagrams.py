class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        d = dict()
        result = list()
        for st in strs:
            sorted_st = ''.join(sorted(st))
            if not sorted_st in d:
                d[sorted_st] = st
            else: #already find one before
                #add the first one in result
                if d[sorted_st] != ',':
                    result.append(d[sorted_st])
                    d[sorted_st] = ',' 

                result.append(st)
        return result
if __name__ == '__main__':
    import pdb 
    strs = ['xian','naxi','hello','world','dlrowd','orwld']
    res = Solution().anagrams(strs)
    print "res:",res
