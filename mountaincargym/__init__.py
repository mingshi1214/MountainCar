from gym.envs.resistration import register

register(
        id='MountainCar-v0',
        entry_point='mountaincargym.mountaincar:MountainCarEnv',
        max_episode_steps=60,
        )
