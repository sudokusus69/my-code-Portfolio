from scipy import stats
import matplotlib.pyplot as plt

'''RELATION OF THE DATA OR HOW CLOSE TO THE LINE THAT DATA IS GIVEN 
1 (DIRECTLY PROPORTIONAL)-- GOOD
-1 (INDIRECTLY PROPORTIONAL)-- GOOD
0 (NO RELATION)-- BAD'''


x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
slope, intercept, r,p, std_err = stats.linregress(x,y)


print(r)

