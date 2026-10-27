import pandas as pd
import numpy as np

# Load the existing simulation results
data = pd.read_csv("radar_simulation_results.csv")

# Extract the range estimation errors
errors = data["Range Error (m)"]

# Calculate performance metrics
mean_error = errors.mean()
mean_absolute_error = errors.abs().mean()
rmse = np.sqrt((errors ** 2).mean())
error_standard_deviation = errors.std()

# Calculate the best and worst estimates
minimum_error = errors.min()
maximum_error = errors.max()

# Calculate the percentage of estimates within 10 metres
within_10_metres = (errors.abs() <= 10).mean() * 100

# Display the performance report
print("=" * 50)
print("RADAR PERFORMANCE ANALYSIS REPORT")
print("=" * 50)

print(f"Number of measurements: {len(data):,}")
print(f"Actual target range: {data['Actual Range (m)'].iloc[0]:.2f} m")

print("\nACCURACY METRICS")
print("-" * 50)
print(f"Mean signed error: {mean_error:.3f} m")
print(f"Mean absolute error (MAE): {mean_absolute_error:.3f} m")
print(f"Root mean square error (RMSE): {rmse:.3f} m")

print("\nPRECISION METRICS")
print("-" * 50)
print(f"Standard deviation of errors: {error_standard_deviation:.3f} m")

print("\nERROR RANGE")
print("-" * 50)
print(f"Smallest signed error: {minimum_error:.3f} m")
print(f"Largest signed error: {maximum_error:.3f} m")
print(f"Measurements within 10 m of actual range: {within_10_metres:.2f}%")

print("=" * 50)

# Save the performance report
report = pd.DataFrame({
    "Metric": [
        "Number of measurements",
        "Mean signed error (m)",
        "Mean absolute error (m)",
        "RMSE (m)",
        "Standard deviation of errors (m)",
        "Minimum signed error (m)",
        "Maximum signed error (m)",
        "Measurements within 10 m (%)"
    ],
    "Value": [
        len(data),
        mean_error,
        mean_absolute_error,
        rmse,
        error_standard_deviation,
        minimum_error,
        maximum_error,
        within_10_metres
    ]
})

report.to_csv("radar_performance_report.csv", index=False)

print("\nReport saved to radar_performance_report.csv")