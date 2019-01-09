class Solution_once:
    def singleNumber(self, arr):
        ones, twos = 0, 0
        for X in arr:
            ones, twos = (ones ^ X) & ~twos, (ones & X) | (twos & ~X)
        assert twos == 0
        return ones
class Solution_twice:
    def single_number(arr):
        ones, twos, threes = 0, 0, 0
        for X in arr:
            ones, twos, threes = (~X & ones) | (X & ~ones & ~twos & ~threes), (~X & twos) | (X & ones), (~X & threes) | (X & twos)
        return twos
if __name__ == "__main__":
    print(Solution_once().singleNumber([1, 1, 1, 2, 2, 2, 3]))
    print(Solution_once().singleNumber([5, 3, 0, 3, 5, 5, 3]))
	
