# D - Stone XOR

Time Limit: 3 sec / Memory Limit: 1024 MiB

Score : 400 points

### Problem Statement

There are N bags, labeled bag 1, bag 2, ..., bag N.

Bag i (1 <= i <= N) contains A_i stones.

Takahashi can perform the following operation any number of times, possibly zero:

> Choose two bags A and B, and move **all** stones from bag A into bag B.

Find the number of different possible values for the following after repeating the operation.

- B_1 XOR B_2 XOR ... XOR B_N, where B_i is the final number of stones in bag i.

Here, XOR denotes bitwise XOR.

### Constraints

- 2 <= N <= 12
- 1 <= A_i <= 10^{17}
- All input values are integers.

### Input

The input is given from Standard Input in the following format:

```
N
A_1 A_2 ... A_N
```

### Output

Print the number of different possible values for B_1 XOR B_2 XOR ... XOR B_N after repeating the operation.

### Sample Input 1

```
3
2 5 7
```

### Sample Output 1

```
3
```

For example, if Takahashi chooses bags 1 and 3 for the operation, then the numbers of stones in bags 1, 2, 3 become 0, 5, 9.
If he stops at this point, the XOR is 0 XOR 5 XOR 9 = 12.
The other possible XOR values after repeating the operation are 0 and 14.
Therefore, the possible values are 0, 12, 14; there are three values, so the output is 3.

### Sample Input 2

```
2
100000000000000000 100000000000000000
```

### Sample Output 2

```
2
```

### Sample Input 3

```
6
71 74 45 34 31 60
```

### Sample Output 3

```
84
```
