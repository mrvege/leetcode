# !/usr/bin/env python
# encoding: utf-8
__author__ = 'dm'

"""
You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the first turn to remove the stones.
Both of you are very clever and have optimal strategies for the game. Write a function to
determine whether you can win the game given the number of stones in the heap.
For example, if there are 4 stones in the heap, then you will never win the game:
no matter 1, 2, or 3 stones you remove, the last stone will always be removed by your friend.
Hint:
If there are 5 stones in the heap, could you figure out a way to remove the stones
such that you will always be the winner?
"""

"""
题目概述：
你和你的朋友玩游戏， 拿到最后一个石子的获胜。
不可能获胜：
剩下四个石子的时候轮到你

solution:
1<=n<=3时 先手必胜
n==4时 先手负
5<=n<=7时  先手可以取石子使得n变为4
n==8  转换为上述情况
因此 n能否被4整数为先手是否胜利的条件
"""


class Solution(object) :
	def canWinNim (self , n) :
		"""
		:type n: int
		:rtype: bool
		"""
		return n % 4 > 0


if __name__ == '__main__' :
	s1 = Solution()
	print s1.canWinNim(5)