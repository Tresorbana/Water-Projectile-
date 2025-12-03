import numpy as np
import matplotlib.pyplot as plt
v0 = 25.0        
x_target = 45.0    
t_target = 3.0     
g = 9.8            
cos_alpha = x_target / (v0 * t_target)
alpha = np.arccos(cos_alpha)
vx = v0 * np.cos(alpha)
vy0 = v0 * np.sin(alpha)
t = np.linspace(0, t_target, 400)
x = vx * t
y = vy0 * t - 0.5 * g * t**2
t_top = vy0 / g
x_top = vx * t_top
y_top = vy0 * t_top - 0.5 * g * t_top**2
y_hit = vy0 * t_target - 0.5 * g * t_target**2
plt.figure(figsize=(12,6))
plt.plot(x, y, linewidth=2)
plt.scatter([x_top], [y_top])
plt.text(x_top, y_top + 0.7, "Highest point", fontsize=10)
plt.scatter([x_target], [y_hit])
plt.text(x_target - 4, y_hit + 0.7, "Impact point", fontsize=10)
plt.plot([x_target, x_target], [0, y_hit], linewidth=3)
plt.xlabel("Horizontal Distance (m)", fontsize=12)
plt.ylabel("Height (m)", fontsize=12)
plt.title("Water Stream ", fontsize=14)
plt.grid(True, linestyle="--", linewidth=0.7)
plt.tight_layout()
output_path = "waterStream.png"
plt.savefig(output_path, dpi=300)
plt.close()
print("Graph saved as:", output_path)
