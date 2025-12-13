import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_dartboard(ax, title, shots, bias_x=0, bias_y=0):
    """Helper function to plot a single dartboard."""
    # Dartboard rings
    for i in range(1, 6):
        ax.add_patch(patches.Circle((0, 0), i, fill=False, edgecolor='gray', alpha=0.5))
    
    # Bullseye
    ax.add_patch(patches.Circle((0, 0), 0.5, fill=True, color='#C62828', alpha=0.7))
    
    # Shots
    x = shots[:, 0] + bias_x
    y = shots[:, 1] + bias_y
    ax.plot(x, y, 'o', color='#0D47A1', markersize=8, alpha=0.8)
    
    # Aesthetics
    ax.set_title(title, fontsize=14, pad=10)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_aspect('equal', adjustable='box')
    ax.set_xticks([])
    ax.set_yticks([])

# --- Simulation Parameters ---
num_shots = 30

# --- Create Figure ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
# fig.suptitle('Figure 1: Noise (Scatter) vs. Bias (Offset)', fontsize=18, y=0.95) # Removed to avoid duplicate captions

# 1. Low Noise, Low Bias
shots_lnlb = np.random.normal(0, 0.5, (num_shots, 2))
plot_dartboard(axs[0, 0], 'Low Noise, Low Bias', shots_lnlb)

# 2. High Noise, Low Bias
shots_hnlb = np.random.normal(0, 1.5, (num_shots, 2))
plot_dartboard(axs[0, 1], 'High Noise, Low Bias', shots_hnlb)

# 3. Low Noise, High Bias
shots_lnhb = np.random.normal(0, 0.5, (num_shots, 2))
plot_dartboard(axs[1, 0], 'Low Noise, High Bias', shots_lnhb, bias_x=2.5, bias_y=-2)

# 4. High Noise, High Bias
shots_hnhb = np.random.normal(0, 1.5, (num_shots, 2))
plot_dartboard(axs[1, 1], 'High Noise, High Bias', shots_hnhb, bias_x=2.5, bias_y=-2)

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.93])

# --- Save Figure ---
output_filename = 'figure_1_noise_bias_dartboards.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
