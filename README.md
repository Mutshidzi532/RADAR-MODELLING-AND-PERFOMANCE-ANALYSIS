# RADAR-MODELLING-AND-PERFOMANCE-ANALYSIS
A python based radar simulation analysing range estimation,timing noise,measurement errors and system sensitivity through mathematical modelling,statistical evaluation and data visualisation.
Radar Modelling and Performance Analysis

The project explores how timing uncertainty affects radar distance measurements and evaluates the relationship between timing noise and range estimation accuracy.

Objectives

* Implement the mathematical relationship between signal travel time and estimated target range.
* Simulate timing noise and investigate its effect on range measurements.
* Quantify estimation errors using statistical performance metrics.
* Analyse how timing uncertainty influences measurement accuracy.
* Visualise simulation results to communicate technical findings.

Mathematical Model

The project uses the basic radar ranging equation:

[
R = \frac{ct}{2}
]

Where:

* (R) is the estimated target range in metres.
* (c) is the speed of light in metres per second.
* (t) is the measured round-trip signal travel time in seconds.
* The factor of 2 accounts for the signal travelling to the target and returning.

Timing uncertainty is introduced into the simulated measurements to investigate its effect on the estimated range.

Methodology

1. Calculate target range from simulated signal travel time.
2. Introduce timing noise into the measurements.
3. Estimate target range using the radar ranging equation.
4. Calculate measurement errors and evaluate performance using statistical metrics.
5. Investigate the effect of different noise levels and target distances.
6. Generate visualisations to compare simulation results.

Key Findings

* Increasing timing noise increases range estimation error.
* Under the simplified model, fixed timing uncertainty produces approximately distance-independent range error.
* The simulation demonstrates the relationship between measurement uncertainty and ranging accuracy.

Tools and Technologies

* Python
* NumPy
* pandas
* Matplotlib
* Numerical modelling
* Statistical error analysis
* Data visualisation

Project Structure

radar-modelling-performance-analysis/
├── src/
├── README.md
└── [simulation outputs and supporting files]

The src directory contains the project’s source code. Supporting files contain relevant simulation results and visualisations.

Limitations

This project is a simplified mathematical simulation for learning and analysis. It does not model every aspect of a practical radar system, including antenna characteristics, propagation losses, clutter, multipath effects, or hardware implementation.

The results should therefore be interpreted within the assumptions of the model.

Future Improvements

* Investigate frequency-domain signal processing using the Fast Fourier Transform (FFT).
* Implement target detection under different noise conditions.
* Evaluate detection probability and false-alarm probability.
* Compare simulated results with theoretical expectations.

Author

Mutshidzi Madavha

BSc in Mathematics and Applied Mathematics

GitHub: Mutshidzi532
