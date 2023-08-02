<div align="center"><h1>Sudoku-solver</h1></div>
<div align="center"><h3>A simple program in python to solve a 9x9 sudoku table with backtracking algorithm (recursion + brute-force)</h3></div>

-----


<div align="center">
  <h4>
    I was playing sudoku to keep my mind sharp; but after some minutes, I got tired of it... 🥱 <br>
    So I tried to write a program to keep my mind sharp by programming and solve the sudoko too 😏!
  </h4>
  <br>
  A solved sudoku board is a grid consisting of nine squares subdivided into a further nine smaller squares in such a way that every number appears once in each horizontal line, vertical line, and 3x3 square.
</div>
<br>

<div align="center">

  ![sudoku-board](https://github.com/behrad26/sudoku-solver/assets/112078003/d1bdd1e6-9e81-4136-b875-cb05a552f75e)
</div>

-----

### input
```
0 0 0 0 0 0 5 0 0 
1 0 0 4 0 6 0 0 0 
0 0 0 0 5 3 0 0 0 
0 2 0 0 7 0 0 0 5
7 0 0 1 0 0 0 0 0
0 0 0 9 0 0 8 0 3
0 0 9 8 0 0 0 1 0
8 3 0 0 4 9 0 0 0 
0 0 0 0 0 0 4 0 0
```
#### or
```
000000500 
100406000
000053000
020070005
700100000
000900803
009800010
830049000
000000400
```

-----
### output
```
 _____________________________
| 3  9  6 | 2  1  8 | 5  4  7 |
| 1  5  7 | 4  9  6 | 2  3  8 |
| 2  8  4 | 7  5  3 | 6  9  1 |
|---------|---------|---------|
| 9  2  8 | 3  7  4 | 1  6  5 |
| 7  6  3 | 1  8  5 | 9  2  4 |
| 4  1  5 | 9  6  2 | 8  7  3 |
|---------|---------|---------|
| 5  4  9 | 8  2  7 | 3  1  6 |
| 8  3  1 | 6  4  9 | 7  5  2 |
| 6  7  2 | 5  3  1 | 4  8  9 |
 ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
```

-----

<div align="center">
  
  ![solved-sudoku](https://github.com/behrad26/sudoku-solver/assets/112078003/2bebebe9-105a-4556-8878-cb0c345b8790)
  ![good-job](https://github.com/behrad26/sudoku-solver/assets/112078003/f80da7fd-cd47-4d16-90ad-d9bb3015ef18)
</div>
