from random import weibullvariate

import scipy.stats as sps

n_repeats = 30
means = [0] * n_repeats
sample_size = 30

for _ in range(100):
    for i in range(n_repeats):
        means[i] = sum(weibullvariate(2, 4) for _ in range(sample_size)) / sample_size
    if sps.normaltest(means)[1] < 0.05:
        print(sps.normaltest(means)[1])
