# Q-learning-Temporal-Diff-
### Illustrates the temporal difference method for Q-learning in Reinforcement Learning by finding optimal path.

> ![image](https://user-images.githubusercontent.com/75536336/163526434-e91da93b-1737-47a4-a7c4-0ae4c0687e6a.png)

> Here we start from box marked S and try to reach End point, box marked with E. X represents boxes with danger, so need to avoid them.
> We run the model for 8 episodes and updating the Q(s, a) values in a 2D matrix for each action in each episode. Finally, the model learns the path
> and outputs the most probable actions that are to be taken for each box to reach E.

Output:

![image](https://user-images.githubusercontent.com/75536336/163526916-c33fefe2-db3d-479f-b1a4-dd9ca9d8e51a.png)

> Where 'd', 'u', 'r', 'l' represents down, up, right, left respectively. The output matrix describe the best move that can be choosen from the given box of the grid.
> Like start from S(0,0) then move down, then right, then right again & we reach E.
