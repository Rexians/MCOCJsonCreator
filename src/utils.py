class Utils:

    def __init__(self) -> None:
        pass

    def get_sig_list(self, tier) -> list:
        '''
        Used to get the signature list for looping.
        '''
        if tier == 6 or tier == 5:
            return([0,20,40,60,80,100,120,140,160,180,200])
        elif tier == 4 or tier == 3 or tier == 2:
            return([0,1,20,40,60,80,99])

    def get_ranks_list(self, tier) -> list:
        if tier == 6:
            return([1,2,3,4])
        elif tier == 5 or tier == 4:
            return([1,2,3,4,5])    
        elif tier == 3:
            return([1,2,3,4])
        elif tier == 2:
            return([1,2,3])        