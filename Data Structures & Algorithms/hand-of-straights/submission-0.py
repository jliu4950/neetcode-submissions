from collections import defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        
        dic = defaultdict(int)
        for card in hand:
            dic[card] += 1
        
        hand.sort()
        '''
        [1, 2, 2, 3, 3, 4, 4, 5]
        1:0
        2:2
        3:2
        4:2
        5:1
        '''
        for card in hand:
            if dic[card] == 0:
                continue
            
            dic[card] -= 1
            for i in range(1,groupSize):
                nextCard = card + i
                if dic[nextCard] == 0:
                    return False
                else:
                    dic[nextCard] -= 1
        
        return True
