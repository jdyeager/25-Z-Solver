import numpy as np
from copy import deepcopy

id3 = np.identity(3, dtype=np.int32)
# orientations = [(df*id3[f],ds*id3[(f+1+s)%3]) for f in range(3) for s in range(2) for df in (1,-1) for ds in (1,-1)]
orientations = [np.column_stack((df*id3[f],ds*id3[(f+1+s)%3])) for f in range(3) for s in range(2) for df in (1,-1) for ds in (1,-1)]

combo_lookup = [(np.array([0,0])), (np.array([1,0])), (np.array([1,1])), (np.array([2,1])), (np.array([3,1]))]

def check_placement(base, O, board):
  for v in combo_lookup:
    loc = base + O @ v
    for i in range(3):
      if loc[i] < 0 or loc[i] > 5:
        return False
    if board.get(tuple(loc.tolist())) is not None:
      return False
  return True

def get_placements(loc, board):
  return [(base, O) for O in orientations for n,v in enumerate(combo_lookup) if check_placement((base := loc - O @ v), O, board)]
  # for O in orientations:
  #   print(O)
  #   for n,v in enumerate(combo_lookup):
  #     base = loc - O @ v
  #     if check_placement(base, O, board):
  #       print(f"base: {base}, n = {n}: {loc}")

def update_board(board, base, O, num):
  board = deepcopy(board)
  for v in combo_lookup:
    board[tuple((base + O @ v).tolist())] = num
  return board

def place_Z(loc, board, num):
  for base, O in get_placements(loc, board):
    new_board = update_board(board, base, O, num)
    print_board(new_board)
    # get updated board
    # get new loc

def print_board(board):
  block_nums = set(board.values())
  blocks = {n:[] for n in block_nums}
  for loc, n in board.items():
    blocks[n].append(loc)
  for n, locs in blocks.items():
    print(f"block {n}: {locs}")

# for orientation in orientations:
#   print(orientation)

# print(get_placements(np.array((0,0,0)), {}))

# place_Z(np.array((0,0,0)), {}, 0)
