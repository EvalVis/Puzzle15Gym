from gym.envs.registration import register

register(
    id='Puzzle3x3Random-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'height': 3,
        'width': 3
    }
)

register(
    id='Puzzle4x4Random-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'height': 4,
        'width': 4
    }
)

register(
    id='Puzzle5x5Random-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'height': 5,
        'width': 5
    }
)

register(
    id='Puzzle3x3Fixed-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'custom_puzzle': "2 8 6|7 1 3|-1 5 4"
    }
)

register(
    id='Puzzle4x4Fixed-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'custom_puzzle': "6 -1 13 12|7 11 10 4|9 15 5 3|1 2 14 8"
    }
)

register(
    id='Puzzle4x4Fixed-v0',
    entry_point='Puzzle15Gym.puzzle15_env:Puzzle15Env',
    kwargs={
        'custom_puzzle': "20 -1 7 17 9|1 21 16 6 19|4 3 22 12 5|11 8 13 15 18|14 24 23 2 10"
    }
)