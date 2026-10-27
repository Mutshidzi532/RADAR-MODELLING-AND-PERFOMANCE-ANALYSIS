# RADAR-MODELLING-AND-PERFOMANCE-ANALYSIS
Overview

A radar modelling and performance analysis project combining Excel-based engineering calculations with Python simulation to investigate range estimation, timing noise, measurement errors, and system sensitivity.

The project applies mathematical modelling, numerical simulation, statistical error analysis, scenario comparison, and data visualisation to examine how measurement uncertainty affects radar ranging accuracy.

Project Objectives

* Implement the mathematical relationship between radar signal travel time and estimated target range.
* Simulate timing noise and investigate its effect on range measurements.
* Calculate and analyse range estimation errors using statistical performance metrics.
* Evaluate the sensitivity of ranging accuracy to different timing-noise levels.
* Compare simulation scenarios and interpret the resulting performance differences.
* Apply mathematical and computational techniques to a simplified radar engineering problem.

Mathematical Model

The project uses the basic radar ranging equation:

[
R = \frac{ct}{2}
]

Where:

* (R) is the estimated target range in metres.
* (c) is the speed of light, approximately (3 \times 10^8) metres per second.
* (t) is the measured round-trip signal travel time in seconds.
* The factor of 2 accounts for the signal travelling to the target and returning to the radar.

Timing uncertainty is introduced into simulated measurements to investigate its effect on the estimated target range.

The simplified measurement model can be expressed as:

[
t_{\text{measured}} = t_{\text{true}} + \epsilon
]

Where:

* (t_{\text{measured}}) is the simulated measured travel time.
* (t_{\text{true}}) is the true round-trip travel time.
* (\epsilon) represents timing measurement error.

The estimated range is then calculated using the measured travel time:

[
R_{\text{estimated}} = \frac{c t_{\text{measured}}}{2}
]

The range estimation error is:

[
e = R_{\text{estimated}} - R_{\text{true}}
]

These equations provide the foundation for evaluating the effect of timing uncertainty on radar ranging performance.

Methodology

1. Excel-Based Modelling

Develop an integrated spreadsheet model for radar range estimation, timing-noise simulation, statistical error analysis, and performance evaluation.

2. Python Simulation

Implement the radar ranging equation in Python and simulate range measurements under different timing-noise conditions.

3. Statistical Error Analysis

Evaluate estimation accuracy using statistical performance metrics, including mean absolute error, root mean squared error, signed error, and error variability.

4. Scenario Comparison

Investigate how different timing-noise levels influence range estimation accuracy and compare the resulting performance metrics.

5. Performance Interpretation

Analyse numerical results and visualisations to identify relationships between timing uncertainty and ranging accuracy.

Excel-Based Radar Performance Model

The workbook Radar_Modelling_and_Performance_Analysis.xlsx provides an integrated environment for modelling and analysing radar ranging performance.

The workbook includes the following components:

* Radar Inputs: Configuration of model parameters and simulation inputs.
* Integrated Noise Simulation: Simulation of radar range measurements under timing uncertainty.
* Integrated Noise Analysis: Calculation of measurement errors and statistical performance metrics.
* Radar Performance Summary: Consolidated performance results and interpretations.
* Scenario Comparison: Comparison of simulation outcomes under different conditions.
* Dashboard Data: Structured data prepared for performance visualisation.

The Excel model supports the evaluation of range estimation accuracy, measurement consistency, and sensitivity to timing noise.

Python Simulation

The Python component implements the simplified radar ranging model and investigates the effects of timing uncertainty through numerical simulation.

The analysis includes:

* Radar range estimation from signal travel time.
* Simulation of timing measurement noise.
* Calculation of range estimation errors.
* Evaluation of error metrics across different noise conditions.
* Analysis of the relationship between timing noise and range estimation accuracy.
* Generation of visualisations to communicate simulation results.

Performance Metrics

The project uses the following metrics to evaluate ranging accuracy.

Mean Absolute Error (MAE)

Measures the average magnitude of the range estimation errors:

[
MAE = \frac{1}{N}\sum_{i=1}^{N}|e_i|
]

Root Mean Squared Error (RMSE)

Measures the square root of the average squared estimation errors:

[
RMSE = \sqrt{\frac{1}{N}\sum_{i=1}^{N}e_i^2}
]

Signed Error

Measures the difference between the estimated range and the true range:

[
e_i = R_{\text{estimated},i} - R_{\text{true},i}
]

A positive error indicates an overestimate, while a negative error indicates an underestimate.

Error Standard Deviation

Measures the variability of the estimation errors and helps assess the consistency of the simulated measurements.

Together, these metrics provide complementary measures of estimation accuracy, bias, and variability.

Key Findings

The simulations demonstrate the following relationships under the assumptions of the simplified model:

* Increasing timing noise increases range estimation error.
* Greater timing uncertainty produces larger deviations between estimated and true ranges.
* With fixed additive timing noise, the absolute range error is approximately independent of target distance.
* Statistical performance metrics provide a quantitative basis for comparing different simulation conditions.

For example, the Python simulation produced approximate RMSE values of 7.5 m, 15 m, and 30 m for timing-noise standard deviations of 0.05 μs, 0.10 μs, and 0.20 μs, respectively.

These results illustrate the direct relationship between timing uncertainty and range estimation error in the simplified ranging model.

Tools and Technologies

* Microsoft Excel: Engineering calculations, model inputs, integrated noise analysis, scenario comparison, and performance summaries.
* Python: Numerical simulation and computational analysis.
* NumPy: Numerical computations.
* pandas: Data handling and analysis.
* Matplotlib: Data visualisation.
* Statistical analysis: Error metrics and performance evaluation.

Project Structure

radar-modelling-performance-analysis/
│
├── src/
│   └── Python simulation scripts
│
├── Radar_Modelling_and_Performance_Analysis.xlsx
│
├── CSV results and supporting data
│
├── PNG visualisations
│
└── README.md

This is a representative overview of the project structure. Actual filenames and subfolders may differ.

Limitations

This project is a simplified mathematical simulation designed to investigate radar range estimation and timing uncertainty.

It does not represent a complete operational radar system and does not model all practical effects, including:

* Antenna characteristics and beam patterns.
* Signal propagation losses.
* Multipath propagation.
* Clutter and interference.
* Detailed receiver and transmitter characteristics.
* Hardware implementation and real-time processing constraints.

The results should therefore be interpreted within the assumptions of the mathematical model.

Future Improvements

Potential extensions include:

* Frequency-domain signal analysis using the Fast Fourier Transform (FFT).
* Simulated target detection under different noise conditions.
* Evaluation of detection probability and false-alarm probability.
* Investigation of signal-to-noise ratio and its effect on detection performance.
* Further verification of numerical results against theoretical expectations.

These extensions would build on the existing ranging model and introduce additional radar signal-processing concepts.

Author

Mutshidzi Madavha

BSc in Mathematics and Applied Mathematics
University of Venda

GitHub: Mutshidzi532

Disclaimer

This project is an educational engineering simulation developed to explore mathematical modelling, numerical computation, and radar performance analysis. It is not intended to represent a certified radar design or operational radar system.
