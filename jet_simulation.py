import numpy as np
import matplotlib.pyplot as plt

print("====================================")
print("      TURBOJET ENGINE SIMULATOR")
print("====================================")

# User Inputs
air_mass_flow = float(input("Enter air mass flow rate (kg/s): "))
fuel_flow = float(input("Enter fuel flow rate (kg/s): "))
exit_velocity = float(input("Enter exhaust velocity (m/s): "))
flight_velocity = float(input("Enter aircraft velocity (m/s): "))

# Constants
fuel_energy = 43e6  # J/kg typical jet fuel energy

# Thrust Calculation
thrust = (air_mass_flow + fuel_flow) * exit_velocity - air_mass_flow * flight_velocity

# Thermal Efficiency
thermal_efficiency = (thrust * flight_velocity) / (fuel_flow * fuel_energy)

print("\n----- ENGINE PERFORMANCE -----")
print(f"Thrust: {thrust:.2f} N")
print(f"Thermal Efficiency: {thermal_efficiency:.4f}")

# Range of exhaust velocities for analysis
exit_range = np.linspace(300, 1200, 100)

# Thrust variation
thrust_values = (air_mass_flow + fuel_flow) * exit_range - air_mass_flow * flight_velocity

# Efficiency variation
efficiency_values = (thrust_values * flight_velocity) / (fuel_flow * fuel_energy)

# Plotting
plt.figure()

plt.plot(exit_range, thrust_values, label="Thrust (N)")
plt.plot(exit_range, efficiency_values * 1e6, label="Efficiency (scaled)")

plt.xlabel("Exhaust Velocity (m/s)")
plt.ylabel("Performance")
plt.title("Turbojet Engine Performance Analysis")

plt.legend()
plt.grid(True)

plt.show()