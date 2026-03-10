import numpy as np
import matplotlib.pyplot as plt

print("===================================")
print("   ADVANCED NACA AIRFOIL ANALYZER")
print("===================================")

# Inputs
naca = input("Enter NACA 4-digit airfoil (example 2412): ")
velocity = float(input("Enter airflow velocity (m/s): "))
air_density = float(input("Enter air density (kg/m^3): "))
wing_area = float(input("Enter wing area (m^2): "))

# NACA parameters
m = int(naca[0]) / 100
p = int(naca[1]) / 10
t = int(naca[2:]) / 100

# Airfoil geometry
x = np.linspace(0,1,100)

yt = 5*t*(0.2969*np.sqrt(x)-0.1260*x-0.3516*x**2+0.2843*x**3-0.1015*x**4)

yc = np.zeros_like(x)
dyc_dx = np.zeros_like(x)

for i in range(len(x)):
    if x[i] < p and p != 0:
        yc[i] = m/p**2*(2*p*x[i]-x[i]**2)
        dyc_dx[i] = 2*m/p**2*(p-x[i])
    elif p != 0:
        yc[i] = m/(1-p)**2*((1-2*p)+2*p*x[i]-x[i]**2)
        dyc_dx[i] = 2*m/(1-p)**2*(p-x[i])

theta = np.arctan(dyc_dx)

xu = x - yt*np.sin(theta)
yu = yc + yt*np.cos(theta)

xl = x + yt*np.sin(theta)
yl = yc - yt*np.cos(theta)

# Angle of attack
angles_deg = np.linspace(-5,20,50)
angles_rad = np.radians(angles_deg)

# Lift coefficient
CL = 2*np.pi*angles_rad

# Stall simulation
CL_max = 1.4
CL = np.clip(CL, -CL_max, CL_max)

# Drag model
CD0 = 0.02
k = 0.04
CD = CD0 + k*CL**2

# Lift and drag forces
Lift = 0.5*air_density*velocity**2*wing_area*CL
Drag = 0.5*air_density*velocity**2*wing_area*CD

# Plotting
plt.figure(figsize=(12,4))

# Airfoil shape
plt.subplot(1,3,1)
plt.plot(xu,yu)
plt.plot(xl,yl)
plt.title("NACA "+naca+" Airfoil")
plt.axis("equal")
plt.grid(True)

# Lift curve
plt.subplot(1,3,2)
plt.plot(angles_deg,CL)
plt.title("Lift Coefficient vs AoA")
plt.xlabel("Angle of Attack")
plt.ylabel("CL")
plt.grid(True)

# Drag curve
plt.subplot(1,3,3)
plt.plot(angles_deg,CD)
plt.title("Drag Coefficient vs AoA")
plt.xlabel("Angle of Attack")
plt.ylabel("CD")
plt.grid(True)

plt.tight_layout()
plt.show()

print("\nSample Results:")
for i in range(0,len(angles_deg),10):
    print(f"AoA {angles_deg[i]:.1f}° -> Lift {Lift[i]:.2f} N | Drag {Drag[i]:.2f} N")