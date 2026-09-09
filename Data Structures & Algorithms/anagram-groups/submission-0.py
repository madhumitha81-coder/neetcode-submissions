class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        re=defaultdict(list)
        for i in strs:
            cnt=[0]*26
            for j in i:
                cnt[ord(j)-ord("a")]+=1
            re[tuple(cnt)].append(i)
        return list(re.values())

