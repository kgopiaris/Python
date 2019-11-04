"""
Given two numbers N,K and an array of size N, print the three nearest neighbours of K(nearest neighbours are numbers which have least difference with K).
Input Size : 4 <= N, K <= 100000
Sample Testcases :
INPUT
5 3
1 2 3 4 6
OUTPUT
2 4 1


Steps to follow:
Step-1: 
	Get the median value of N
Step-2:
	Get the difference between K and median, 
    then start to print from median upto N length.
"""

N= 7
k = 6   
m = k - (N//2)

for i in range(N):
    print(m, end=' ')
    m += 1
