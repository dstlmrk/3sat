#!/usr/bin/python
# coding=utf-8

import random
import math
from sat import Sat

MIN_TEMPERATURE = 1


class State():
    """
    Represents state in the state space by the bit array
    and its optimization criterion by the price.
    """
    def __init__(self, satisfied_ratio, weight_usage_ratio, value, bit_array):
        self.satisfied_ratio = satisfied_ratio
        self.weight_usage_ratio = weight_usage_ratio
        self.value = value
        self.bit_array = bit_array


class SimulatedAnnealing(Sat):
    """
    Simulated annealing algorithm.
    """
    def __init__(self, init_temperature, cooling, inner_loop, ratio, file):
        super(SimulatedAnnealing, self).__init__(file)
        self.init_temperature = init_temperature
        self.cooling = cooling
        self.inner_loop = inner_loop
        # ratio satisfaction/weight
        self.ratio = float(ratio)

    def get_neighbor(self, state):
        """
        Returns neighbor which is fit for max capacity of the bag.
        """
        new_bit_array = list(state.bit_array)
        random_position = random.randint(0, self.variables_count - 1)
        # add/remove one item from state
        new_bit_array[random_position] = (new_bit_array[random_position] + 1) % 2

        c, w = self.get_ratios(new_bit_array)
        new_value = (self.ratio*c) + ((1-self.ratio)*w)
        return State(c, w, new_value, new_bit_array)

    def get_random_state(self):
        # empty bit array
        # random.getrandbits(1)
        return State(0, 0, 0, [0 for i in range(self.variables_count)])

    def cool(self, temperature):
        return temperature * self.cooling

    @staticmethod
    def frozen(temperature):
        return temperature > MIN_TEMPERATURE

    def evaluate(self):
        # init state
        state = self.get_random_state()
        temperature = self.init_temperature

        best_state = None

        while self.frozen(temperature):
            # search between neighbors
            for i in range(self.inner_loop):
                neighbor = self.get_neighbor(state)
                if neighbor.value > state.value:
                    state = neighbor
                # P(f_curr, f_new, t) = e^((f_new − f_curr)/t) >= random(0,1)
                elif math.e**((neighbor.value - state.value)/temperature) >= random.random():
                    state = neighbor

                if not best_state:
                    best_state = state
                elif best_state.value < state.value and best_state.satisfied_ratio <= state.satisfied_ratio:
                    best_state = state
            temperature = self.cool(temperature)
            # TODO: udelat graf
            # relative error in time for one specific run
            # print("%s %s %s" % (temperature, state.value, state.satisfied_ratio))
              # / float(self.expected_price) * 100)))
        return best_state
        # return state
