from random import sample, uniform

import scipy.stats as sps

n_repeats = 20
means = [0] * n_repeats
sample_1 = [uniform(2, 4) for _ in range(1000)]
sample_size = 10


for _ in range(100):
    for i in range(n_repeats):
        means[i] = sum(sample(sample_1, sample_size)) / sample_size
    if sps.normaltest(means)[1] < 0.05:
        print(sps.normaltest(means)[1])
