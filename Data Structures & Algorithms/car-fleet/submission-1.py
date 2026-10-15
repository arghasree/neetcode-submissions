class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # what do we need?
        # first sort 
        # then have the time saved. 

        sorted_ = sorted(zip(position, speed))
        position, speed = zip(*sorted_)

        time=[]
        for i in range(len(position)):
            time.append((target-position[i])/speed[i])

        res=1
        
        while len(time)>=2:
            # print( time, res)
            current = time.pop()
            last = time.pop()
            if current < last:
                res+=1
                time.append(last)
            else:
                # same fleet 
                time.append(current)
                


        return res


        