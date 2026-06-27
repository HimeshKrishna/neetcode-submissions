class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for word in strs:
            keys="".join(sorted(word))
            if keys not in hashmap:
                hashmap[keys]=[]
            hashmap[keys].append(word)
        return list(hashmap.values())