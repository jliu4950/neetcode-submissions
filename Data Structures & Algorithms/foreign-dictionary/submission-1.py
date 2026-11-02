from collections import defaultdict
class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        build graph : compare one by one
        return "":
            meet cycle
            graph is empty
        '''
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for word in words:
            for char in word:
                if char not in in_degree:
                    in_degree[char] = 0

        n = len(words)
        for i in range(n - 1):
            j = i + 1
            w1 = words[i]
            w2 = words[j]

            mark = True
            for k in range(min(len(w1),len(w2))):
                if w1[k] != w2[k]:
                    graph[w1[k]].append(w2[k])
                    in_degree[w2[k]] += 1
                    mark = False
                    break
            if mark and len(w1) > len(w2):
                return ""
        
        
        q = deque()
        for letter,indg in in_degree.items():
            if indg == 0:
                q.append(letter)

        
        res = []
        while q:
            w = q.popleft()
            res.append(w)
            for nxt_w in graph[w]:
                in_degree[nxt_w] -= 1
                if in_degree[nxt_w] == 0:
                    q.append(nxt_w)
        # print(res)
        return "".join(res) if len(res) == len(in_degree) else "" 
