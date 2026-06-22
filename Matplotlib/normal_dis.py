from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

def normal_distribution():
    # normal distribution in graphs
    sns.displot(random.normal(loc=10, scale=0.5, size=1000), kind='kde')

    plt.show()

# binomial distribution in graphs

a = {
        'normal': random.normal(loc=50, scale=5, size=1000),
        'binomial': random.binomial(n=100, p=0.5, size=1000)
}

sns.displot(a, kind='kde')

plt.show()