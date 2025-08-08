# F - Double Sum 3

Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 525 points

### Problem Statement

You are given an integer sequence A=(A_1,A_2,...,A_N) of length N.

For each integer pair (L,R) with 1 <= L <= R <= N, define f(L,R) as follows:

- Start with an empty blackboard. Write the R-L+1 integers A_L, A_{L+1}, ..., A_R on the blackboard in order.
- Repeat the following operation until all integers on the blackboard are erased:
  - Choose integers l, r with l <= r such that every integer from l through r appears at least once on the blackboard. Then, erase all integers from l through r that are on the blackboard.
- Let f(L,R) be the minimum number of such operations needed to erase all the integers from the blackboard.

Find the sum of f(L,R) over all L, R such that 1 <= L <= R <= N.

### Constraints

- 1 <= N <= 3 * 10^5
- 1 <= A_i <= N
- All input values are integers.

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 ... A_N
```

### Output

Print the answer.

### Sample Input 1

```
4
1 3 1 4
```

### Sample Output 1

```
16
```

For example, in the case of (L,R)=(1,4):
- The blackboard has 1,3,1,4.
- Choose (l,r)=(1,1) and erase all occurrences of 1. The blackboard now has 3,4.
- Choose (l,r)=(3,4) and erase all occurrences of 3 and 4. The blackboard becomes empty.
- It cannot be done in fewer than two operations, so f(1,4) = 2.

Similarly, you can find f(2,4)=2, f(1,1)=1, etc.
The sum of f(L,R) is 16, so print 16.

### Sample Input 2

```
5
3 1 4 2 4
```

### Sample Output 2

```
23
```

### Sample Input 3

```
10
5 1 10 9 2 5 6 9 1 6
```

### Sample Output 3

```
129
```
