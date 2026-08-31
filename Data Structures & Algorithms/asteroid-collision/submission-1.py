class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        state=[]
        for i in asteroids:
            while state and i < 0 and state[-1] > 0:
                diff=i+state[-1]
                if diff < 0:
                    state.pop()
                elif diff > 0:
                    i=0
                else:
                    i=0
                    state.pop()
            if i:
                state.append(i)
        return state