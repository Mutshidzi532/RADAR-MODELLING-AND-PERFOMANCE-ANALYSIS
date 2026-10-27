import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Physical constant
SPEED_OF_LIGHT = 300_000_000

# Simulation settings
TARGET_RANGES = [1_000, 3_000, 5_000, 10_000]
NUMBER_OF_MEASUREMENTS = 10_000
TIMING_NOISE_STD_US = 0.1

# Convert timing noise from microseconds to seconds
timing_noise_std_seconds = TIMING_NOISE_STD_US / 1_000_000

# Store performance results
distance_results = []

# Make the simulation reproducible
np.random.seed(42)

# Simulate radar measurements at each target distance
for actual_range in TARGET_RANGES:

    # Calculate ideal round-trip travel time
    ideal_time = (2 * actual_range) / SPEED_OF_LIGHT

    # Generate random timing errors
    timing_errors = np.random.normal(
        loc=0,
        scale=timing_noise_std_seconds,
        size=NUMBER_OF_MEASUREMENTS
    )

    # Simulate measured travel times
    measured_times = ideal_time + timing_errors

    # Estimate target ranges
    estimated_ranges = (
        SPEED_OF_LIGHT * measured_times
    ) / 2

    # Calculate range estimation errors
    range_errors = estimated_ranges - actual_range

    # Calculate performance metrics
    mae = np.mean(np.abs(range_errors))

    rmse = np.sqrt(
        np.mean(range_errors ** 2)
    )

    error_std = np.std(range_errors, ddof=1)

    # Store the results
    distance_results.append({
        "Actual Target Range (m)": actual_range,
        "Mean Absolute Error (m)": mae,
        "RMSE (m)": rmse,
        "Error Standard Deviation (m)": error_std
    })

# Convert results into a table
results = pd.DataFrame(distance_results)

# Display the performance report
print("=" * 70)
print("RADAR DISTANCE PERFORMANCE ANALYSIS")
print("=" * 70)

print(f"Measurements per distance: {NUMBER_OF_MEASUREMENTS:,}")
print(f"Timing-noise standard deviation: {TIMING_NOISE_STD_US} microseconds")

print("\nPERFORMANCE COMPARISON")
print("-" * 70)

print(
    results.to_string(
        index=False,
        float_format=lambda x: f"{x:.3f}"
    )
)

# Export performance results to CSV
results.to_csv(
    "radar_distance_analysis_results.csv",
    index=False
)

# Plot RMSE against target distance
plt.figure(figsize=(9, 5))

plt.plot(
    results["Actual Target Range (m)"],
    results["RMSE (m)"],
    marker="o"
)

plt.title("Effect of Target Distance on Radar Range RMSE")
plt.xlabel("Actual Target Range (m)")
plt.ylabel("Range RMSE (m)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_distance_analysis.png",
    dpi=300
)

plt.show()

# Confirm saved files
print("\nSaved: radar_distance_analysis_results.csv")
print("Saved: radar_distance_analysis.png")