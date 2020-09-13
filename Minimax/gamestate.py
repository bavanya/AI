
xlim, ylim = 3, 2  
#taking top left corner as origin, x axis from left to right and y axis from top to bottom
class GameState:
    def __init__(self):
        self._board = [[0] * ylim for _ in range(xlim)]
        #print(self._board)
        self._board[-1][-1] = 1 
        self._parity = 0
        self._player_locations = [None, None]

    def _get_blank_spaces(self):
        return [(x,y) for y in range(ylim) for x in range(xlim) if self._board[x][y]==0]

    def _get_legal_moves(self):
        loc = self._player_locations[self.parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in rays:
            _x,_y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x,_y = _x+dx,_y+dy
                if self._board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves
