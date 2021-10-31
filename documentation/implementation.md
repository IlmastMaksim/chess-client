# Implementation

## Project structure

- Basic commands are available at `README` file in the root directory 
- Source code can be found at `src` directory
- Tests can be found at `src/tests` directory
- Project split into modules `board`, `move`, `pieces`, `server` and `tables`.

## Implementation details

In this project I used such algorithms as Minimax and Alpha Beta pruning. The idea of Minimax is that it circulates over all possible situations in the game and comes up with the most optimal move to take eventually. Nevertheless, its significant disadvantage is that it analyzes lots of the nodes of the game tree that are irrelevant to be analyzed. Therefore, it was opted to use Alpha Beta pruning algorithm in cooperation with Minimax as well. The goal of Alpha Beta pruning is to reduce the number of nodes, that the Minimax processes in order to achieve greater performance efficiency.

The desicion making happens on the basis of the adequacy of positions of the chess pieces on board. The adequacy of piece positions is defined in [piece-square tables](https://www.chessprogramming.org/Piece-Square_Tables). The principle idea of this approach is that some positions of the chess board are more adequate for certain chess pieces than others. For example, it is better for knights to keep away from cells, that are located on the edge of the board, so for this reason, those cells that are located on the edge are marked as negative numbers in the square table for knights.

## Implemented time and space complexities

The alpha-beta pruning algorithm is expected to correspond to `O(b^(d/2))` time complexity.

## Possible flaws and improvements

The algorithm evaluation doesnt take into an account such possible moves as [castling](https://en.wikipedia.org/wiki/Castling) or [en passant](https://en.wikipedia.org/wiki/En_passant). Also, currently the game is supposed to be played via terminal with no graphical interface, so a good enhancement would be to write a UI module for the program. 

## Sources

https://zserge.com/posts/carnatus/

https://www.javatpoint.com/ai-alpha-beta-pruning

https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning

https://adamberent.com/2019/03/02/chess-board-evaluation/

https://adamberent.com/2019/03/02/piece-square-table/