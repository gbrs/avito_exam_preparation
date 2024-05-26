def calculate_foo(x: float) -> float:
    return (1 - x)**10 * x


low = -2
high = 3
intervals = 100_000
step = (high - low) / intervals
integral = (0 + calculate_foo(low) + calculate_foo(high)) * step / 6
low_with_bias = low + step / 2

for i in range(1, intervals):
    integral += 2 * calculate_foo(low + i * step) * step / 6
    integral += 4 * calculate_foo(low_with_bias + (i - 1) * step) * step / 6

integral += 4 * calculate_foo(high + step / 2) * step / 6

print(integral)
# -27654.962
# -27627           100
# -27654.689     1 000
# -27654.959    10 000
# -27654.962   100 000
