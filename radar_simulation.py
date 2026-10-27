import numpy as np
import pandas as pd

SPEED_OF_LIGHT = 300_000_000
ACTUAL_RANGE = 3_000
NUMBER_OF_MEASUREMENTS = 10_000
TIMING_NOISE_STD_US = 0.1

timing_noise_std_seconds = TIMING_NOISE_STD_US / 1_000_000

ideal_round_trip_time = (2 * ACTUAL_RANGE) / SPEED_OF_LIGHT

np.random.seed(42)

timing_errors = np.random.normal(
    loc=0,
    scale=timing_noise_std_seconds,
    size=NUMBER_OF_MEASUREMENTS
)

measured_times = ideal_round_trip_time + timing_errors

estimated_ranges = (SPEED_OF_LIGHT * measured_times) / 2

range_errors = estimated_ranges - ACTUAL_RANGE

results = pd.DataFrame({
    "Measurement": np.arange(1, NUMBER_OF_MEASUREMENTS + 1),
    "Actual Range (m)": ACTUAL_RANGE,
    "Timing Error (s)": timing_errors,
    "Measured Round-Trip Time (s)": measured_times,
    "Estimated Range (m)": estimated_ranges,
    "Range Error (m)": range_errors,
    "Absolute Error (m)": np.abs(range_errors)
})

mean_estimated_range = results["Estimated Range (m)"].mean()
mean_signed_error = results["Range Error (m)"].mean()
mean_absolute_error = results["Absolute Error (m)"].mean()
rmse = np.sqrt((results["Range Error (m)"] ** 2).mean())
error_std = results["Range Error (m)"].std()

print("=" * 45)
print("RADAR TIMING NOISE SIMULATION")
print("=" * 45)

print(f"Actual target range: {ACTUAL_RANGE:.2f} m")
print(f"Number of measurements: {NUMBER_OF_MEASUREMENTS:,}")
print(f"Timing noise standard deviation: {TIMING_NOISE_STD_US:.3f} microseconds")

print("\nPERFORMANCE ANALYSIS")
print("-" * 45)
print(f"Mean estimated range: {mean_estimated_range:.3f} m")
print(f"Mean signed error: {mean_signed_error:.3f} m")
print(f"Mean absolute error (MAE): {mean_absolute_error:.3f} m")
print(f"Root mean square error (RMSE): {rmse:.3f} m")
print(f"Error standard deviation: {error_std:.3f} m")

output_file = "radar_simulation_results.csv"
results.to_csv(output_file, index=False)

print(f"\nSimulation results saved to: {output_file}")
print("=" * 45)