# B - Geometric Sequence

Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 200 points

### Problem Statement

You are given a length-N sequence A=(A_1,A_2,...,A_N) of positive integers.

Determine whether A is a geometric progression.

### Constraints

- 2 <= N <= 100
- 1 <= A_i <= 10^9
- All input values are integers.

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 ... A_N
```

### Output

If A is a geometric progression, print `Yes`; otherwise, print `No`.

### Sample Input 1

```
5
3 6 12 24 48
```

### Sample Output 1

```
Yes
```

A=(3,6,12,24,48).
A is a geometric progression with first term 3, common ratio 2, and five terms.
Therefore, print `Yes`.

### Sample Input 2

```
3
1 2 3
```

### Sample Output 2

```
No
```

A=(1,2,3).
Since A_1 : A_2 = 1 : 2 != 2 : 3 = A_2 : A_3, A is not a geometric progression.
Therefore, print `No`.

### Sample Input 3

```
2
10 8
```

### Sample Output 3

```
Yes
```

A is a geometric progression with first term 10, common ratio 0.8, and two terms.
Therefore, print `Yes`.
