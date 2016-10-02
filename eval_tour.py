#!/usr/bin/env python
from basic_functions import cost_tour, read_inp
from sys import argv

t = map(int, raw_input().split())
N, c, d = read_inp('problems/'+argv[1])
print cost_tour(t, d, N)

