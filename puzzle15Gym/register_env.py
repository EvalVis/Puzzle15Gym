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