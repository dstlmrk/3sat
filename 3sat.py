#!/usr/bin/python3.4
# coding=utf-8

import click
from simulated_annealing import SimulatedAnnealing
import time


class File(list):
    """Represents file"""

    def __init__(self, path):
        self = [self.append(x) for x in File.load(path)]

    @staticmethod
    def load(path):
        with open(path) as f:
            return f.readlines()


def solve(files, variables, temperature, cooling, inner_loop, ratio):
    instances = 50
    duration_sum = 0
    weight_usage_ratio_sum = 0
    satisfied_ratio_sum = 0

    for file in files:
        sa = SimulatedAnnealing(temperature, cooling, inner_loop, ratio, File(file))
        start_time = time.time()
        result = sa.evaluate()
        duration = time.time() - start_time
        print(result.value, result.satisfied_ratio, result.weight_usage_ratio, result.bit_array)
        duration_sum += duration
        weight_usage_ratio_sum += result.weight_usage_ratio
        satisfied_ratio_sum += result.satisfied_ratio
        # break

    # from seconds to milliseconds
    duration_avg = (duration_sum / instances) * 1000
    weight_usage_ratio_avg = (weight_usage_ratio_sum / instances)
    satisfied_ratio_avg = (satisfied_ratio_sum / instances)
    return duration_avg, weight_usage_ratio_avg, satisfied_ratio_avg


@click.command()
@click.option('-p', '--path', default=None,
              help="Input file. [./data/example.data]")
@click.option('-v', '--variables', default=20,
              help="Number of variables [20]")
@click.option('-t', '--temperature', default=1000,
              help="Init temperature for simulated annealing. [1000]")
@click.option('-c', '--cooling', default=0.85,
              help="Cooling for simulated annealing. [0.85]")
@click.option('-i', '--inner-loop', default=200,
              help="Number of iterations in inner loop for simulated annealing. [200]")
@click.option('-r', '--ratio', default=0.85,
              help="Ratio between satisfaction and weight from closed interval from 0 to 1 [0.85]")
def main(path, variables, temperature, cooling, inner_loop, ratio):

    if path:
        files = [path]
    else:
        files = [
            "./data/{}/uf{}-0{}.cnf".format(
                variables, variables, x
            ) for x in range(1, 51)
        ]


    # for ratio in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1]:
    # for temperature in [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000]:
    # for cooling in [0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
    # for inner_loop in [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 950, 1000]:

    duration_avg, weight_usage_ratio_avg, satisfied_ratio_avg = solve(
        files, variables, temperature, cooling, inner_loop, ratio
    )


    print(duration_avg, weight_usage_ratio_avg, satisfied_ratio_avg)

        # print("cooling = %s" % cooling)
        # print("          {} ms\nweight    {}\nsatisfied {}\n".format(
        #     duration_avg,
        #     weight_usage_ratio_avg,
        #     satisfied_ratio_avg)
        # )


if __name__ == '__main__':
    main()
