def calculate_foo(x: float) -> float:
    return (1 - x)**10 * x

low = -2
high = 3
intervals = 100
step = (high - low) / intervals
integral = (0 + calculate_foo(low) + calculate_foo(high)) / 2 * step

for i in range(1, intervals):
    integral += calculate_foo(low + i*step) * step

print(integral)
# -27654.962
# -27745           100
# -27656         1 000
# -27656.971    10 000
# -27655.962   100 000
# -27654.962 1 000 000
