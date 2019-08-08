import math
import gym
import gym.spaces
import matplotlib.pyplot as plt
import numpy as np
from gym.utils import seeding

class MountainCarEnv(gym.Env):
    metadata = {
            'render.modes': ['human', 'rgb_array'],
            'video.frames_per_second' : 70
    }

    def __init__(self):
        self.gravity = 0.0028
        self.masscart = 1.0 
        #trying to make a sine graph?
        self.hill = 0.8*np.cos(2*np.pi*3*10*(1.0/100) + 0)
        self.tau = 0.02
        self.kinematics_integrator = 'euler'
        self.force = 0.01
        self.min_position = -1.2
        self.max_position = 0.6
        self.max_speed = 0.7
        self.goal_position = 0.5
        self.goal_velocity = 0

        self.low = np.array([self.min_position, -self.max_speed])
        self.high = np.array([self.max+position, self.max_speed])

        self.action_space = spaces.Discrete(3)
        self.obervation_space = spaces.Box(self.low, self.high. dtype = np.float32)

        self.seed()
        self.state = None
        self.steps_beyone_done = None

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        self.state = self.np_random.uniform(low=-0.6, high=-0.4), 0])
        return np.array(self.state)
    
    def step(self, action):
        assert self.action_space.contains(action), "%r (%s) invalid"%(action, type(action))
        #not sure why the below code line is allowed???
        position, velocity = self.state
        velocity += (action-1)*self.force + math.cos(3*position)*(-self.gravity)
        velocity = np.clip(velocity, -self.max_speed, self.max_speed)
        position += velocity
        position = np.clip(position, self.min_position, self.max_position)
        if (position==self.min_position and velocity<0): 
            velocity = 0

        done = bool (position >=self.goal_position and velocity >= self.goal_velocity)
        reward = -1.0

        self.state = (position, velocity)
        return np.array(self.state)

    def render(self, mode='human'):
        screen_width = 600
        screen_height = 400

        world_width = self.x_threshold*2
        scale = screen_width/world_width
        
        if self.viewer is None:
            from gym.envs.classic_control import rendering
            self.viewer = rendering.View(screen_width, screen_height)
            cart = rendering.FilledPolygon([(-2,2),(-2,2),(2,2), (2,-2)])
        return self.viewer.render(return_rgb_array = mode == 'rgb_array')

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None






