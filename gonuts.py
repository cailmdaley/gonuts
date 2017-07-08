import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from subprocess import call
import seaborn as sns

# Tunables
#===================================#
sns.set_style('whitegrid')
board_size = 13

# Startup stuff
#===================================#
fig, ax = plt.subplots()    
ax.set_xticks(range(13))
ax.set_yticks(range(13))
ax.set_xticklabels(np.arange(-board_size/2. + 0.5, board_size/2. + 0.5))
ax.set_yticklabels(np.arange(-board_size/2. + 0.5, board_size/2. + 0.5))

# get board
#===================================#
# gameID = raw_input('game name? ')
gameID='test'

call(['git', 'pull'])
try:
    board_states = list(np.load(gameID + '.npy'))
except IOError:
    board_states = [np.zeros((board_size, board_size), dtype=int)]    
ax.imshow(board_states[-1], origin='lower')

# move
board_states.append(board_states[-1])

board_states[-1]
x_input, y_input = input('please give the x,y coordinates of your ') 
if len(board_states) % 2 == 1: # white
    board_states[-1][x_input + board_size//2, y_input + board_size//2] = 1
else: # black
    board_states[-1][x_input + board_size//2, y_input + board_size//2] = -1
ax.imshow(board_states[-1], origin='lower')
plt.show()

#end turn, save board states
np.save(gameID, board_states)


call(['git', 'add', '{}.npy'.format(gameID)])
call(['git', 'commit', "-m'gameID_{}''".format(gameID)])
call(['git', 'status'])
call(['git', 'push'])
