import numpy as np
import matplotlib.pyplot as plt

# --- Data ---
observed_measurement = 157
confidence_interval = (140, 174)
true_value = 165 # An example true value that falls within the interval

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 4))

# --- Create the Error Bar Plot ---
# The error bar will represent the confidence interval
lower_error = observed_measurement - confidence_interval[0]
upper_error = confidence_interval[1] - observed_measurement
error = np.array([[lower_error], [upper_error]])

ax.errorbar(y=[1], x=[observed_measurement], xerr=error, fmt='o', color='#0D47A1', 
            markersize=12, capsize=8, elinewidth=3, markeredgewidth=2, label='Observed Measurement & 95% C.I.')

# --- Add "True Value" ---
ax.plot(true_value, 1, '*', color='#E65100', markersize=22, markeredgecolor='black', label='Hypothetical "True Value"')


# --- Aesthetics ---
ax.set_title('Quantifying Uncertainty with a Confidence Interval', fontsize=16, pad=20)
ax.set_xlabel('Measured Expression Level', fontsize=12)

# Y-axis is not meaningful, so we remove its labels and ticks
ax.set_yticks([])
ax.set_ylim(0.5, 1.5)

# Set x-axis limits to give some space
ax.set_xlim(130, 185)

ax.legend(loc='best', ncol=1, fontsize=10)
ax.grid(axis='y') # Only keep horizontal grid lines if desired, or turn off all

# --- Save Figure ---
output_filename = 'figure_4_quantifying_uncertainty.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
