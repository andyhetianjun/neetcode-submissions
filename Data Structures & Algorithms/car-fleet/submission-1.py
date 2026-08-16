class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = 0 
        slowest = 0.0
        for pos, speed in sorted(zip(position, speed), reverse=True):
            time = (target - pos) / speed
            if time > slowest:
                res += 1
                slowest = time

        return res