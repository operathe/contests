# C - Paint to make a rectangle

Time Limit: 2 sec / Memory Limit: 1024 MiB

Score : 300 points

### Problem Statement

You are given a grid of H rows and W columns.

Let (i,j) denote the cell at row i (1 <= i <= H) from the top and column j (1 <= j <= W) from the left.

The state of the grid is represented by H strings S_1, S_2, ..., S_H, each of length W, as follows:

- If the j-th character of S_i is `#`, cell (i,j) is painted black.
- If the j-th character of S_i is `.`, cell (i,j) is painted white.
- If the j-th character of S_i is `?`, cell (i,j) is not yet painted.

Takahashi wants to paint each not-yet-painted cell white or black so that all the black cells form a rectangle.

More precisely, he wants there to exist a quadruple of integers (a,b,c,d) (1 <= a <= b <= H, 1 <= c <= d <= W) such that:

> For each cell (i,j) (1 <= i <= H, 1 <= j <= W),
> if a <= i <= b and c <= j <= d, the cell is black;
>
> otherwise, the cell is white.

Determine whether this is possible.

### Constraints

- 1 <= H, W <= 1000
- H and W are integers.
- Each S_i is a string of length W consisting of `#`, `.`, `?`.
- There is at least one cell that is already painted black.

### Input

The input is given from Standard Input in the following format:

```
H W
S_1
S_2
...
S_H
```

### Output

If it is possible to paint all the not-yet-painted cells so that the black cells form a rectangle, print `Yes`; otherwise, print `No`.

### Sample Input 1

```
3 5
.#?#.
.?#?.
?...?
```

### Sample Output 1

```
Yes
```

The grid is in the following state. `?` indicates a cell that are not yet painted.

By painting cells (1,3), (2,2), and (2,4) black and cells (3,1) and (3,5) white, the black cells can form a rectangle as follows:

Therefore, print `Yes`.

### Sample Input 2

```
3 3
?##
#.#
##?
```

### Sample Output 2

```
No
```

To form a rectangle with all black cells, you would need to paint cell (2,2) black, but it is already painted white.
Therefore, it is impossible to make all black cells form a rectangle, so print `No`.

### Sample Input 3

```
1 1
#
```

### Sample Output 3

```
Yes
```
