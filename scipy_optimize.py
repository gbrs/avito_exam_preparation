from scipy.optimize import minimize

foo = lambda x: 3 * x[0]**2 + x[0] * x[1] + 2 * x[1]**2 - x[0] - 4 * x[1]

print(minimize(foo, (0, 0)))

'''
3 * x[0]**2 + x[0] * x[1] + 2 * x[1]**2 - x[0] - 4 * x[1]
(0, 1)


'''
