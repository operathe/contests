# E - Vitamin Balance

Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 450 points

### Problem Statement

There are N foods, each containing exactly one of vitamins 1, 2, and 3.

Specifically, eating the i-th food gives you A_i units of vitamin V_i, and C_i calories.

Takahashi can choose any subset of these N foods as long as the total calorie consumption does not exceed X.

Find the maximum possible value of this: the minimum intake among vitamins 1, 2, and 3.

### Constraints

- 1 <= N <= 5000
- 1 <= X <= 5000
- 1 <= V_i <= 3
- 1 <= A_i <= 2 * 10^5
- 1 <= C_i <= X
- All input values are integers.

### Input

The input is given from Standard Input in the following format:

```
N X
V_1 A_1 C_1
V_2 A_2 C_2
...
V_N A_N C_N
```

### Output

Print the maximum possible value of "the minimum intake among vitamins 1, 2, and 3" when the total calories consumed is at most X.

### Sample Input 1

```
5 25
1 8 5
2 3 5
2 7 10
3 2 5
3 3 10
```

### Sample Output 1

```
3
```

Each food provides the following if eaten:

- 1st food: 8 units of vitamin 1, and 5 calories
- 2nd food: 3 units of vitamin 2, and 5 calories
- 3rd food: 7 units of vitamin 2, and 10 calories
- 4th food: 2 units of vitamin 3, and 5 calories
- 5th food: 3 units of vitamin 3, and 10 calories

Eating the 1st, 2nd, 4th, and 5th foods gives 8 units of vitamin 1, 3 units of vitamin 2, 5 units of vitamin 3, and 25 calories.
In this case, the minimum among the three vitamin intakes is 3 (vitamin 2).
It is impossible to get 4 or more units of each vitamin without exceeding 25 calories, so the answer is 3.

### Sample Input 2

```
2 5000
1 200000 1
2 200000 1
```

### Sample Output 2

```
0
```
