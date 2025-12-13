import numpy as np
import matplotlib.pyplot as plt

# --- Simulation Parameters ---
steady_state = 100  # Average mRNA count
time_points = 200
fluctuation_strength = 10

# --- Generate Data ---
# Create a time axis
time = np.arange(time_points)

# Generate some smooth, random fluctuations around the steady state
# Using a combination of sine waves to create a pseudo-random, "biological" look
noise = np.random.normal(0, fluctuation_strength, time_points)
long_wave = fluctuation_strength * 2 * np.sin(2 * np.pi * time / 80)
short_wave = fluctuation_strength * np.sin(2 * np.pi * time / 20)

# Combine to get final mRNA count
mrna_counts = steady_state + noise + long_wave + short_wave
# Ensure counts don't go below zero
mrna_counts[mrna_counts < 0] = 0

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the steady state line
ax.axhline(steady_state, color='#C62828', linestyle='--', linewidth=2, label='Average Steady State')

# Plot the fluctuating mRNA counts
ax.plot(time, mrna_counts, label='True mRNA Count', color='#0D47A1', linewidth=2)

# --- Aesthetics ---
ax.set_title('Natural Fluctuation of a Biological Process', fontsize=16, pad=20)
ax.set_xlabel('Time (Arbitrary Units)', fontsize=12)
ax.set_ylabel('True mRNA Molecule Count', fontsize=12)
ax.legend(fontsize=10)
ax.tick_params(axis='both', which='major', labelsize=10)
ax.set_ylim(bottom=0) # mRNA count cannot be negative

# --- Save Figure ---
output_filename = 'figure_1_biological_fluctuation.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
