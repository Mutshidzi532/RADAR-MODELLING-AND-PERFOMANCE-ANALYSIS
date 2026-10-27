import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Physical constant
SPEED_OF_LIGHT = 300_000_000

# Simulation settings
ACTUAL_RANGE = 3_000
NUMBER_OF_MEASUREMENTS = 10_000

# Timing-noise scenarios in microseconds
NOISE_LEVELS_US = [0.05, 0.10, 0.20]

# Store the performance results
sensitivity_results = []

# Make the simulation reproducible
np.random.seed(42)

# Test each timing-noise scenario
for noise_us in NOISE_LEVELS_US:

    # Convert microseconds to seconds
    noise_seconds = noise_us / 1_000_000

    # Calculate ideal round-trip time
    ideal_time = (2 * ACTUAL_RANGE) / SPEED_OF_LIGHT

    # Generate random timing errors
    timing_errors = np.random.normal(
        loc=0,
        scale=noise_seconds,
        size=NUMBER_OF_MEASUREMENTS
    )

    # Simulate measured travel times
    measured_times = ideal_time + timing_errors

    # Estimate target ranges
    estimated_ranges = (
        SPEED_OF_LIGHT * measured_times
    ) / 2

    # Calculate range errors
    range_errors = estimated_ranges - ACTUAL_RANGE

    # Calculate performance metrics
    mae = np.mean(np.abs(range_errors))

    rmse = np.sqrt(
        np.mean(range_errors ** 2)
    )

    error_std = np.std(range_errors, ddof=1)

    # Save the results for this scenario
    sensitivity_results.append({
        "Timing Noise (microseconds)": noise_us,
        "Mean Absolute Error (m)": mae,
        "RMSE (m)": rmse,
        "Error Standard Deviation (m)": error_std
    })

# Convert results into a table
results = pd.DataFrame(sensitivity_results)

# Display the comparison
print("=" * 65)
print("RADAR TIMING-NOISE SENSITIVITY ANALYSIS")
print("=" * 65)

print(f"Actual target range: {ACTUAL_RANGE} m")
print(f"Measurements per scenario: {NUMBER_OF_MEASUREMENTS:,}")

print("\nPERFORMANCE COMPARISON")
print("-" * 65)
print(results.to_string(index=False, float_format=lambda x: f"{x:.3f}"))

# Export the comparison to CSV
results.to_csv(
    "radar_noise_sensitivity_results.csv",
    index=False
)

# Plot RMSE for each timing-noise scenario
plt.figure(figsize=(9, 5))

plt.plot(
    results["Timing Noise (microseconds)"],
    results["RMSE (m)"],
    marker="o"
)

plt.title("Effect of Timing Noise on Radar Range RMSE")
plt.xlabel("Timing-Noise Standard Deviation (microseconds)")
plt.ylabel("Range RMSE (metres)")
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig(
    "radar_noise_sensitivity.png",
    dpi=300
)

plt.show()

print("\nSaved: radar_noise_sensitivity_results.csv")
print("Saved: radar_noise_sensitivity.png")