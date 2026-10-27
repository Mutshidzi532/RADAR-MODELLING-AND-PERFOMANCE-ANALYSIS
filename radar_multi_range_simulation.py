import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. RADAR SIMULATION SETTINGS
# ============================================================

SPEED_OF_LIGHT = 300_000_000  # Speed of light in metres per second

TARGET_RANGES = [1_000, 3_000, 5_000, 10_000]  # Metres

NUMBER_OF_MEASUREMENTS = 10_000

TIMING_NOISE_STD_US = 0.1  # Timing-noise standard deviation in microseconds

# Convert timing noise from microseconds to seconds
timing_noise_std_seconds = TIMING_NOISE_STD_US / 1_000_000

# Make the simulation reproducible
np.random.seed(42)


# ============================================================
# 2. SIMULATE RADAR MEASUREMENTS FOR MULTIPLE TARGET RANGES
# ============================================================

all_measurements = []
performance_results = []

for actual_range in TARGET_RANGES:

    # Calculate ideal round-trip travel time
    ideal_time = (2 * actual_range) / SPEED_OF_LIGHT

    # Generate random timing errors
    timing_errors = np.random.normal(
        loc=0,
        scale=timing_noise_std_seconds,
        size=NUMBER_OF_MEASUREMENTS
    )

    # Simulate measured round-trip travel times
    measured_times = ideal_time + timing_errors

    # Estimate target ranges using the radar range equation
    estimated_ranges = (
        SPEED_OF_LIGHT * measured_times
    ) / 2

    # Calculate range-estimation errors
    range_errors = estimated_ranges - actual_range

    # Store every simulated measurement
    measurements = pd.DataFrame({
        "Actual Target Range (m)": actual_range,
        "Measurement Number": np.arange(1, NUMBER_OF_MEASUREMENTS + 1),
        "Ideal Round-Trip Time (s)": ideal_time,
        "Measured Round-Trip Time (s)": measured_times,
        "Timing Error (microseconds)": timing_errors * 1_000_000,
        "Estimated Range (m)": estimated_ranges,
        "Range Error (m)": range_errors,
        "Absolute Range Error (m)": np.abs(range_errors)
    })

    all_measurements.append(measurements)

    # Calculate performance metrics
    mae = np.mean(np.abs(range_errors))

    rmse = np.sqrt(
        np.mean(range_errors ** 2)
    )

    mean_error = np.mean(range_errors)

    error_std = np.std(range_errors, ddof=1)

    # Store summary results
    performance_results.append({
        "Actual Target Range (m)": actual_range,
        "Number of Measurements": NUMBER_OF_MEASUREMENTS,
        "Mean Error (m)": mean_error,
        "Mean Absolute Error (m)": mae,
        "RMSE (m)": rmse,
        "Error Standard Deviation (m)": error_std,
        "Maximum Absolute Error (m)": np.max(np.abs(range_errors))
    })


# ============================================================
# 3. COMBINE ALL SIMULATED MEASUREMENTS
# ============================================================

combined_measurements = pd.concat(
    all_measurements,
    ignore_index=True
)

performance_report = pd.DataFrame(performance_results)


# ============================================================
# 4. DISPLAY THE PERFORMANCE REPORT
# ============================================================

print("=" * 80)
print("RADAR MULTIPLE TARGET-RANGE SIMULATION")
print("=" * 80)

print(f"Speed of light: {SPEED_OF_LIGHT:,} m/s")
print(f"Target ranges: {TARGET_RANGES} metres")
print(f"Measurements per target range: {NUMBER_OF_MEASUREMENTS:,}")
print(f"Total simulated measurements: {len(combined_measurements):,}")
print(f"Timing-noise standard deviation: {TIMING_NOISE_STD_US} microseconds")

print("\nPERFORMANCE COMPARISON")
print("-" * 80)

print(
    performance_report.to_string(
        index=False,
        float_format=lambda value: f"{value:.3f}"
    )
)


# ============================================================
# 5. EXPORT THE SIMULATION DATA AND PERFORMANCE REPORT
# ============================================================

combined_measurements.to_csv(
    "radar_multi_range_measurements.csv",
    index=False
)

performance_report.to_csv(
    "radar_multi_range_performance.csv",
    index=False
)

print("\nFiles saved:")
print("- radar_multi_range_measurements.csv")
print("- radar_multi_range_performance.csv")


# ============================================================
# 6. GRAPH 1: ESTIMATED RANGE FOR EACH TARGET DISTANCE
# ============================================================

plt.figure(figsize=(10, 6))

for actual_range in TARGET_RANGES:

    target_data = combined_measurements[
        combined_measurements["Actual Target Range (m)"] == actual_range
    ]

    # Plot the first 200 measurements for readability
    plt.plot(
        target_data["Measurement Number"].iloc[:200],
        target_data["Estimated Range (m)"].iloc[:200],
        label=f"Target at {actual_range:,} m"
    )

plt.title("Radar Range Estimates at Multiple Target Distances")
plt.xlabel("Measurement Number")
plt.ylabel("Estimated Range (m)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_multi_range_estimates.png",
    dpi=300
)

plt.show()


# ============================================================
# 7. GRAPH 2: RMSE COMPARISON ACROSS TARGET DISTANCES
# ============================================================

plt.figure(figsize=(9, 5))

plt.plot(
    performance_report["Actual Target Range (m)"],
    performance_report["RMSE (m)"],
    marker="o"
)

plt.title("Radar Range RMSE Across Multiple Target Distances")
plt.xlabel("Actual Target Range (m)")
plt.ylabel("Root Mean Square Error (m)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_multi_range_rmse.png",
    dpi=300
)

plt.show()


# ============================================================
# 8. GRAPH 3: RANGE-ERROR DISTRIBUTIONS
# ============================================================

plt.figure(figsize=(10, 6))

for actual_range in TARGET_RANGES:

    target_data = combined_measurements[
        combined_measurements["Actual Target Range (m)"] == actual_range
    ]

    plt.hist(
        target_data["Range Error (m)"],
        bins=50,
        alpha=0.4,
        label=f"{actual_range:,} m"
    )

plt.title("Range-Error Distributions at Multiple Target Distances")
plt.xlabel("Range Error (m)")
plt.ylabel("Frequency")
plt.legend(title="Actual Target Range")
plt.grid(alpha=0.2)

plt.tight_layout()

plt.savefig(
    "radar_multi_range_error_distributions.png",
    dpi=300
)

plt.show()


# ============================================================
# 9. FINAL CONFIRMATION
# ============================================================

print("\n" + "=" * 80)
print("STAGE 7 COMPLETED SUCCESSFULLY")
print("=" * 80)

print("Generated files:")
print("- radar_multi_range_measurements.csv")
print("- radar_multi_range_performance.csv")
print("- radar_multi_range_estimates.png")
print("- radar_multi_range_rmse.png")
print("- radar_multi_range_error_distributions.png")