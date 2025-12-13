import numpy as np
import matplotlib.pyplot as plt

# --- Simulation Parameters ---
time_points = 50
true_amplitude = 2.0
true_phase = np.pi / 4
noise_strength = 0.5

# --- Generate Data ---
# Time axis
time = np.linspace(0, 4 * np.pi, time_points)

# True biological signal (a clean sine wave)
true_signal = true_amplitude * np.sin(time + true_phase) + 3.0

# Measured data (true signal + random sampling noise)
measurement_noise = np.random.normal(0, noise_strength, time_points)
measured_data = true_signal + measurement_noise

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
# fig.suptitle('Figure 2: The Effect of Measurement Noise', fontsize=18, y=0.95) # Removed to avoid duplicate captions


# --- Top Panel: True Signal ---
axs[0].plot(time, true_signal, color='#0D47A1', linewidth=3, label='True Signal')
axs[0].set_title('The True, Unseen Biological Signal', fontsize=14, pad=10)
axs[0].set_ylabel('True Expression Level', fontsize=12)
axs[0].legend(loc='upper right')
axs[0].tick_params(axis='y', labelsize=10)
axs[0].set_ylim(0, 6)

# --- Bottom Panel: Measured Data ---
axs[1].plot(time, true_signal, color='gray', linestyle='--', linewidth=2, label='True Signal (Hidden)')
axs[1].plot(time, measured_data, 'o', color='#C62828', markersize=8, alpha=0.8, label='Measured Data Points')
axs[1].set_title('The Observed, Noisy Measurements', fontsize=14, pad=10)
axs[1].set_xlabel('Time (Arbitrary Units)', fontsize=12)
axs[1].set_ylabel('Measured Expression Level', fontsize=12)
axs[1].legend(loc='upper right')
axs[1].tick_params(axis='both', which='major', labelsize=10)
axs[1].set_ylim(0, 6)

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.93])

# --- Save Figure ---
output_filename = 'figure_2_noise_simulation.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
