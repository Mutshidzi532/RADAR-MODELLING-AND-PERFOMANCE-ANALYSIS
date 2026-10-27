import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 1. PROJECT CONFIGURATION
# ============================================================

OUTPUT_DIR = Path(".")

# Input files from previous stages
NOISE_FILE = OUTPUT_DIR / "radar_noise_sensitivity_results.csv"
DISTANCE_FILE = OUTPUT_DIR / "radar_distance_analysis_results.csv"
MULTI_RANGE_FILE = OUTPUT_DIR / "radar_multi_range_performance.csv"
NOISE_DISTANCE_FILE = OUTPUT_DIR / "radar_noise_distance_performance.csv"

# Output files for Stage 9
SUMMARY_FILE = OUTPUT_DIR / "radar_comprehensive_performance_report.csv"
TEXT_REPORT_FILE = OUTPUT_DIR / "radar_comprehensive_report.txt"

print("=" * 80)
print("RADAR COMPREHENSIVE PERFORMANCE ANALYSIS")
print("=" * 80)


# ============================================================
# 2. VERIFY INPUT FILES
# ============================================================

input_files = [
    NOISE_FILE,
    DISTANCE_FILE,
    MULTI_RANGE_FILE,
    NOISE_DISTANCE_FILE
]

missing_files = [
    str(file)
    for file in input_files
    if not file.exists()
]

if missing_files:
    print("\nERROR: The following input files are missing:")

    for file in missing_files:
        print(f"- {file}")

    raise FileNotFoundError(
        "Please check that all previous simulation stages have been completed."
    )

print("\nAll required input files were found.")


# ============================================================
# 3. LOAD PREVIOUS PERFORMANCE REPORTS
# ============================================================

noise_results = pd.read_csv(NOISE_FILE)

distance_results = pd.read_csv(DISTANCE_FILE)

multi_range_results = pd.read_csv(MULTI_RANGE_FILE)

noise_distance_results = pd.read_csv(NOISE_DISTANCE_FILE)


# ============================================================
# 4. STANDARDISE COLUMN NAMES
# ============================================================

# Stage 5: Timing-noise sensitivity
noise_results = noise_results.rename(columns={
    "Timing Noise (microseconds)": "Timing Noise (microseconds)",
    "Mean Absolute Error (m)": "MAE (m)",
    "RMSE (m)": "RMSE (m)",
    "Error Standard Deviation (m)": "Error Standard Deviation (m)"
})

noise_results["Analysis Stage"] = "Stage 5: Noise Sensitivity"

# Stage 6: Target-distance analysis
distance_results = distance_results.rename(columns={
    "Mean Absolute Error (m)": "MAE (m)",
    "RMSE (m)": "RMSE (m)",
    "Error Standard Deviation (m)": "Error Standard Deviation (m)"
})

distance_results["Timing Noise (microseconds)"] = 0.1
distance_results["Analysis Stage"] = "Stage 6: Distance Analysis"

# Stage 7: Multiple target-range analysis
multi_range_results = multi_range_results.rename(columns={
    "Mean Absolute Error (m)": "MAE (m)",
    "RMSE (m)": "RMSE (m)",
    "Error Standard Deviation (m)": "Error Standard Deviation (m)"
})

multi_range_results["Timing Noise (microseconds)"] = 0.1
multi_range_results["Analysis Stage"] = "Stage 7: Multiple Range Analysis"

# Stage 8: Combined noise and distance analysis
noise_distance_results = noise_distance_results.rename(columns={
    "Mean Absolute Error (m)": "MAE (m)",
    "RMSE (m)": "RMSE (m)",
    "Error Standard Deviation (m)": "Error Standard Deviation (m)"
})

noise_distance_results["Analysis Stage"] = "Stage 8: Noise and Distance Analysis"


# ============================================================
# 5. CONSOLIDATE THE RESULTS
# ============================================================

required_columns = [
    "Analysis Stage",
    "Timing Noise (microseconds)",
    "MAE (m)",
    "RMSE (m)",
    "Error Standard Deviation (m)"
]

# Stage 5 does not include target distance
noise_results["Actual Target Range (m)"] = np.nan

# Ensure all tables contain the required columns
all_results = [
    noise_results,
    distance_results,
    multi_range_results,
    noise_distance_results
]

cleaned_results = []

for results in all_results:

    for column in required_columns:
        if column not in results.columns:
            results[column] = np.nan

    if "Actual Target Range (m)" not in results.columns:
        results["Actual Target Range (m)"] = np.nan

    cleaned_results.append(
        results[
            required_columns + ["Actual Target Range (m)"]
        ].copy()
    )

comprehensive_report = pd.concat(
    cleaned_results,
    ignore_index=True
)

# Reorder columns for readability
comprehensive_report = comprehensive_report[
    [
        "Analysis Stage",
        "Actual Target Range (m)",
        "Timing Noise (microseconds)",
        "MAE (m)",
        "RMSE (m)",
        "Error Standard Deviation (m)"
    ]
]


# ============================================================
# 6. SAVE THE CONSOLIDATED PERFORMANCE REPORT
# ============================================================

comprehensive_report.to_csv(
    SUMMARY_FILE,
    index=False
)

print("\nConsolidated performance report saved:")
print(SUMMARY_FILE)

print("\nPERFORMANCE REPORT PREVIEW")
print("-" * 80)

print(
    comprehensive_report.to_string(
        index=False,
        float_format=lambda value: f"{value:.3f}"
    )
)


# ============================================================
# 7. CALCULATE OVERALL STAGE 8 PERFORMANCE
# ============================================================

print("\n" + "=" * 80)
print("STAGE 8 OVERALL PERFORMANCE SUMMARY")
print("=" * 80)

stage8_summary = noise_distance_results.groupby(
    "Timing Noise (microseconds)"
).agg(
    Average_MAE=("MAE (m)", "mean"),
    Average_RMSE=("RMSE (m)", "mean"),
    Average_Error_Std=("Error Standard Deviation (m)", "mean")
).reset_index()

print(
    stage8_summary.to_string(
        index=False,
        float_format=lambda value: f"{value:.3f}"
    )
)


# ============================================================
# 8. GRAPH 1: AVERAGE RMSE BY TIMING-NOISE LEVEL
# ============================================================

plt.figure(figsize=(9, 5))

plt.plot(
    stage8_summary["Timing Noise (microseconds)"],
    stage8_summary["Average_RMSE"],
    marker="o"
)

plt.title("Average Radar RMSE at Different Timing-Noise Levels")
plt.xlabel("Timing-Noise Standard Deviation (microseconds)")
plt.ylabel("Average RMSE (m)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "radar_comprehensive_noise_performance.png",
    dpi=300
)

plt.show()


# ============================================================
# 9. GRAPH 2: RMSE ACROSS TARGET DISTANCES
# ============================================================

stage8_distance_summary = noise_distance_results.pivot(
    index="Actual Target Range (m)",
    columns="Timing Noise (microseconds)",
    values="RMSE (m)"
)

plt.figure(figsize=(10, 6))

for noise_level in stage8_distance_summary.columns:

    plt.plot(
        stage8_distance_summary.index,
        stage8_distance_summary[noise_level],
        marker="o",
        label=f"{noise_level:.2f} microseconds"
    )

plt.title("Radar RMSE Across Target Distances")
plt.xlabel("Actual Target Range (m)")
plt.ylabel("RMSE (m)")
plt.legend(title="Timing Noise")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "radar_comprehensive_distance_performance.png",
    dpi=300
)

plt.show()


# ============================================================
# 10. GRAPH 3: MAE VERSUS RMSE
# ============================================================

plt.figure(figsize=(9, 5))

plt.scatter(
    noise_distance_results["MAE (m)"],
    noise_distance_results["RMSE (m)"]
)

plt.title("Mean Absolute Error Versus RMSE")
plt.xlabel("Mean Absolute Error (m)")
plt.ylabel("Root Mean Square Error (m)")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    OUTPUT_DIR / "radar_comprehensive_mae_rmse.png",
    dpi=300
)

plt.show()


# ============================================================
# 11. GENERATE THE TEXT REPORT
# ============================================================

average_mae_by_noise = stage8_summary.set_index(
    "Timing Noise (microseconds)"
)["Average_MAE"]

average_rmse_by_noise = stage8_summary.set_index(
    "Timing Noise (microseconds)"
)["Average_RMSE"]

report_lines = [
    "RADAR MODELLING AND PERFORMANCE ANALYSIS",
    "COMPREHENSIVE PERFORMANCE REPORT",
    "=" * 60,
    "",
    "1. PROJECT OVERVIEW",
    "The project simulates radar range estimation using round-trip",
    "travel time and the speed of light.",
    "",
    "2. SIMULATION CONFIGURATION",
    "Target ranges: 1,000 m, 3,000 m, 5,000 m and 10,000 m.",
    "Timing-noise levels: 0.05, 0.10 and 0.20 microseconds.",
    "Measurements per Stage 8 scenario: 10,000.",
    "",
    "3. AVERAGE STAGE 8 PERFORMANCE",
]

for noise_level in average_rmse_by_noise.index:

    report_lines.append(
        f"Timing noise {noise_level:.2f} microseconds: "
        f"Average MAE = {average_mae_by_noise.loc[noise_level]:.3f} m; "
        f"Average RMSE = {average_rmse_by_noise.loc[noise_level]:.3f} m."
    )

report_lines.extend([
    "",
    "4. ENGINEERING INTERPRETATION",
    "Increasing timing noise increases range-estimation error.",
    "In the simplified model, range-error variability is independent",
    "of target distance when timing-noise variability is held constant.",
    "",
    "5. MODEL LIMITATIONS",
    "The simulation assumes idealised range estimation and does not",
    "model distance-dependent signal attenuation, target reflectivity,",
    "clutter, detection probability or false alarms.",
    "",
    "6. CONCLUSION",
    "The results demonstrate the relationship between timing precision",
    "and range precision under the assumptions of the simulation.",
    "Further work should introduce realistic signal and detection effects."
])

with open(
    TEXT_REPORT_FILE,
    "w",
    encoding="utf-8"
) as report_file:

    report_file.write("\n".join(report_lines))

print("\nText report saved:")
print(TEXT_REPORT_FILE)


# ============================================================
# 12. FINAL CONFIRMATION
# ============================================================

print("\n" + "=" * 80)
print("STAGE 9 COMPLETED SUCCESSFULLY")
print("=" * 80)

print("\nGenerated files:")
print("- radar_comprehensive_performance_report.csv")
print("- radar_comprehensive_report.txt")
print("- radar_comprehensive_noise_performance.png")
print("- radar_comprehensive_distance_performance.png")
print("- radar_comprehensive_mae_rmse.png")

print("\nReview the report and graphs before proceeding to Stage 10.")