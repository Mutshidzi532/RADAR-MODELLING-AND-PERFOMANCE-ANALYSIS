import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# 1. RADAR SIMULATION SETTINGS
# ============================================================

SPEED_OF_LIGHT = 300_000_000  # metres per second

TARGET_RANGES = [1_000, 3_000, 5_000, 10_000]

TIMING_NOISE_LEVELS_US = [0.05, 0.10, 0.20]

NUMBER_OF_MEASUREMENTS = 10_000

# Use a fixed seed to make the simulation reproducible
np.random.seed(42)

# Store all measurements and performance results
all_measurements = []
performance_results = []


# ============================================================
# 2. SIMULATE EACH DISTANCE AND NOISE COMBINATION
# ============================================================

for noise_us in TIMING_NOISE_LEVELS_US:

    # Convert timing noise from microseconds to seconds
    noise_seconds = noise_us / 1_000_000

    for actual_range in TARGET_RANGES:

        # Calculate ideal round-trip travel time
        ideal_time = (2 * actual_range) / SPEED_OF_LIGHT

        # Generate random timing errors
        timing_errors = np.random.normal(
            loc=0,
            scale=noise_seconds,
            size=NUMBER_OF_MEASUREMENTS
        )

        # Simulate measured round-trip travel times
        measured_times = ideal_time + timing_errors

        # Estimate target ranges
        estimated_ranges = (
            SPEED_OF_LIGHT * measured_times
        ) / 2

        # Calculate range-estimation errors
        range_errors = estimated_ranges - actual_range

        # Calculate performance metrics
        mean_error = np.mean(range_errors)

        mae = np.mean(np.abs(range_errors))

        rmse = np.sqrt(
            np.mean(range_errors ** 2)
        )

        error_std = np.std(range_errors, ddof=1)

        max_absolute_error = np.max(
            np.abs(range_errors)
        )

        # Store individual measurements
        measurements = pd.DataFrame({
            "Timing Noise (microseconds)": noise_us,
            "Actual Target Range (m)": actual_range,
            "Measurement Number": np.arange(
                1, NUMBER_OF_MEASUREMENTS + 1
            ),
            "Ideal Round-Trip Time (s)": ideal_time,
            "Timing Error (microseconds)": (
                timing_errors * 1_000_000
            ),
            "Measured Round-Trip Time (s)": measured_times,
            "Estimated Range (m)": estimated_ranges,
            "Range Error (m)": range_errors,
            "Absolute Range Error (m)": np.abs(range_errors)
        })

        all_measurements.append(measurements)

        # Store performance summary
        performance_results.append({
            "Timing Noise (microseconds)": noise_us,
            "Actual Target Range (m)": actual_range,
            "Number of Measurements": NUMBER_OF_MEASUREMENTS,
            "Mean Error (m)": mean_error,
            "Mean Absolute Error (m)": mae,
            "RMSE (m)": rmse,
            "Error Standard Deviation (m)": error_std,
            "Maximum Absolute Error (m)": max_absolute_error
        })


# ============================================================
# 3. COMBINE THE RESULTS
# ============================================================

combined_measurements = pd.concat(
    all_measurements,
    ignore_index=True
)

performance_report = pd.DataFrame(
    performance_results
)


# ============================================================
# 4. DISPLAY THE PERFORMANCE REPORT
# ============================================================

print("=" * 85)
print("RADAR TIMING-NOISE AND DISTANCE ANALYSIS")
print("=" * 85)

print(f"Target distances: {TARGET_RANGES} metres")
print(f"Timing-noise levels: {TIMING_NOISE_LEVELS_US} microseconds")
print(f"Measurements per scenario: {NUMBER_OF_MEASUREMENTS:,}")
print(f"Total simulated measurements: {len(combined_measurements):,}")

print("\nPERFORMANCE COMPARISON")
print("-" * 85)

print(
    performance_report.to_string(
        index=False,
        float_format=lambda value: f"{value:.3f}"
    )
)


# ============================================================
# 5. EXPORT THE RESULTS TO CSV
# ============================================================

combined_measurements.to_csv(
    "radar_noise_distance_measurements.csv",
    index=False
)

performance_report.to_csv(
    "radar_noise_distance_performance.csv",
    index=False
)

print("\nCSV files saved:")
print("- radar_noise_distance_measurements.csv")
print("- radar_noise_distance_performance.csv")


# ============================================================
# 6. GRAPH 1: RMSE AGAINST TARGET DISTANCE
# ============================================================

plt.figure(figsize=(10, 6))

for noise_us in TIMING_NOISE_LEVELS_US:

    scenario_data = performance_report[
        performance_report["Timing Noise (microseconds)"] == noise_us
    ]

    plt.plot(
        scenario_data["Actual Target Range (m)"],
        scenario_data["RMSE (m)"],
        marker="o",
        label=f"Timing noise: {noise_us:.2f} microseconds"
    )

plt.title("Radar RMSE Across Target Distances and Timing-Noise Levels")
plt.xlabel("Actual Target Range (m)")
plt.ylabel("Root Mean Square Error (m)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_noise_distance_rmse.png",
    dpi=300
)

plt.show()


# ============================================================
# 7. GRAPH 2: RMSE AGAINST TIMING NOISE
# ============================================================

plt.figure(figsize=(9, 5))

for actual_range in TARGET_RANGES:

    scenario_data = performance_report[
        performance_report["Actual Target Range (m)"] == actual_range
    ]

    plt.plot(
        scenario_data["Timing Noise (microseconds)"],
        scenario_data["RMSE (m)"],
        marker="o",
        label=f"Target range: {actual_range:,} m"
    )

plt.title("Effect of Timing Noise on Radar Range RMSE")
plt.xlabel("Timing-Noise Standard Deviation (microseconds)")
plt.ylabel("Root Mean Square Error (m)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_noise_distance_sensitivity.png",
    dpi=300
)

plt.show()


# ============================================================
# 8. GRAPH 3: MAE COMPARISON
# ============================================================

plt.figure(figsize=(10, 6))

for noise_us in TIMING_NOISE_LEVELS_US:

    scenario_data = performance_report[
        performance_report["Timing Noise (microseconds)"] == noise_us
    ]

    plt.plot(
        scenario_data["Actual Target Range (m)"],
        scenario_data["Mean Absolute Error (m)"],
        marker="o",
        label=f"Timing noise: {noise_us:.2f} microseconds"
    )

plt.title("Mean Absolute Range Error Across Target Distances")
plt.xlabel("Actual Target Range (m)")
plt.ylabel("Mean Absolute Error (m)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "radar_noise_distance_mae.png",
    dpi=300
)

plt.show()


# ============================================================
# 9. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 85)
print("STAGE 8 COMPLETED SUCCESSFULLY")
print("=" * 85)

print("Total measurements analysed:", f"{len(combined_measurements):,}")

print("\nGenerated files:")
print("- radar_noise_distance_measurements.csv")
print("- radar_noise_distance_performance.csv")
print("- radar_noise_distance_rmse.png")
print("- radar_noise_distance_sensitivity.png")
print("- radar_noise_distance_mae.png")