import numpy as np
import matplotlib.pyplot as plt

print("====================================")
print("   ADVANCED AIRCRAFT PERFORMANCE")
print("====================================")

# -------- USER INPUT --------
weight = float(input("Aircraft weight (N): "))
wing_area = float(input("Wing area (m^2): "))
air_density = float(input("Air density (kg/m^3): "))
CD0 = float(input("Zero-lift drag coefficient CD0: "))
k = float(input("Induced drag factor k: "))
CL_max = float(input("Maximum lift coefficient CLmax: "))

# -------- VELOCITY RANGE --------
velocities = np.linspace(10,150,100)

# -------- DRAG POLAR --------
CL = weight / (0.5 * air_density * velocities**2 * wing_area)

CD = CD0 + k * CL**2

# -------- DRAG FORCE --------
Drag = 0.5 * air_density * velocities**2 * wing_area * CD

# -------- POWER REQUIRED --------
Power = Drag * velocities

# -------- STALL SPEED --------
stall_speed = np.sqrt((2 * weight) / (air_density * wing_area * CL_max))

# -------- L/D RATIO --------
LD_ratio = CL / CD
max_LD = np.max(LD_ratio)

best_glide_speed = velocities[np.argmax(LD_ratio)]

print("\n---- PERFORMANCE RESULTS ----")
print(f"Stall Speed: {stall_speed:.2f} m/s")
print(f"Maximum Lift-to-Drag Ratio: {max_LD:.2f}")
print(f"Best Glide Speed: {best_glide_speed:.2f} m/s")

# -------- PLOTS --------
plt.figure(figsize=(12,4))

# Drag vs Velocity
plt.subplot(1,3,1)
plt.plot(velocities,Drag)
plt.axvline(stall_speed,color='r',linestyle='--',label="Stall Speed")
plt.title("Drag vs Velocity")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Drag (N)")
plt.legend()
plt.grid(True)

# Power Curve
plt.subplot(1,3,2)
plt.plot(velocities,Power)
plt.axvline(best_glide_speed,color='g',linestyle='--',label="Best Glide Speed")
plt.title("Power Required")
plt.xlabel("Velocity (m/s)")
plt.ylabel("Power (W)")
plt.legend()
plt.grid(True)

# L/D Ratio
plt.subplot(1,3,3)
plt.plot(velocities,LD_ratio)
plt.title("Lift-to-Drag Ratio")
plt.xlabel("Velocity (m/s)")
plt.ylabel("L/D")
plt.grid(True)

plt.tight_layout()
plt.show()