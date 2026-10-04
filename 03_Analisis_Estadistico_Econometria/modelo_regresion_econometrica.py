import math
x_bar, y_bar, r = 5, 15, -0.85
r_cuadrado = r**2
b_yx = -math.sqrt(r_cuadrado / 2)
b_xy = 2 * b_yx
a1 = y_bar - (b_yx * x_bar)
a2 = x_bar - (b_xy * y_bar)
print(f"Y sobre X: y = {b_yx:.4f}x + {a1:.4f}")
print(f"X sobre Y: x = {b_xy:.4f}y + {a2:.4f}")
print(f"R^2: {r_cuadrado*100:.2f}%")
