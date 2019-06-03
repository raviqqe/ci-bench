#!/usr/bin/env python3

import multiprocessing

num_processes = 8


def run(_):
    acc = 0

    for i in range(2 ** 24 * 16):
        acc += i

    return acc


if __name__ == "__main__":
    with multiprocessing.Pool(num_processes) as pool:
        print(pool.map(run, range(num_processes)))
