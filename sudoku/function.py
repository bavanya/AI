from utils import boxes

def grid_values(grid):
    assert len(grid)==81
    all_digits = '123456789'
    values = []
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    return dict(zip(boxes,values))

#print(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))