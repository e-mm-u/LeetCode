class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        for match in matches:
            if match[0] not in d:
                d[match[0]] = [0,0]
            if match[1] not in d:
                d[match[1]] = [0,0]

            d[match[0]][0] +=  1
            d[match[1]][1] +=  1

        winners = []
        oneLoss = []

        for key in d.keys():
            if d[key][1]==0:
                winners.append(key)
            if d[key][1]==1:
                oneLoss.append(key)
        
        return [sorted(winners),sorted(oneLoss)]

        