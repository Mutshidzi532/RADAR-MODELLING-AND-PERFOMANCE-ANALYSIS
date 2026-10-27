import pandas as pd
import matplotlib.pyplot as plt

# Load the radar simulation results
data = pd.read_csv("radar_simulation_results.csv")

# Graph 1: Distribution of radar range errors
plt.figure(figsize=(10, 6))

plt.hist(
    data["Range Error (m)"],
    bins=50,
    edgecolor="black"
)

plt.title("Distribution of Radar Range Estimation Errors")
plt.xlabel("Range Error (metres)")
plt.ylabel("Number of Measurements")
plt.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.savefig("radar_error_distribution.png", dpi=300)
plt.show()

# Graph 2: Estimated range across the first 200 measurements
first_200 = data.head(200)

plt.figure(figsize=(10, 6))

plt.plot(
    first_200["Measurement"],
    first_200["Estimated Range (m)"]
)

plt.axhline(
    y=3000,
    linestyle="--",
    label="Actual Target Range"
)

plt.title("Radar Range Estimates Across 200 Measurements")
plt.xlabel("Measurement Number")
plt.ylabel("Estimated Range (metres)")
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()
plt.savefig("radar_range_estimates.png", dpi=300)
plt.show()

print("Visualisation completed successfully.")
print("Saved: radar_error_distribution.png")
print("Saved: radar_range_estimates.png")