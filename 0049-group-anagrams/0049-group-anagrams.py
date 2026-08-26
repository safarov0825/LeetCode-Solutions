class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        temp = 0
        anagrams = []
        dic = {}

        for s in strs:
            count = {}
            for l in s:
                count[l] = count.get(l, 0) + 1
            
            found = False
            for key, value in dic.items():
                if count == value:
                    anagrams[key].append(s)
                    found = True

            if not found:
                anagrams.append([s])
                dic[temp] = count
                temp += 1

        return anagrams
             


        

        
        