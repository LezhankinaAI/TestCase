import numpy as np
from sklearn import preprocessing


nums = np.random.uniform(1, 100, 100)
nums = preprocessing.normalize(nums[:,np.newaxis], axis=0).ravel()

# or just nums = np.random.rand(100)

print(np.average(nums))
print(np.var(nums))
print(np.std(nums))
