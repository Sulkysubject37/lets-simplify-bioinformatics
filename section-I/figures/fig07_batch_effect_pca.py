import numpy as np
import matplotlib.pyplot as plt

# --- Simulation Parameters ---
n_samples_per_group = 50
# Batch 1 will be centered around (-2, 2)
# Batch 2 will be centered around (2, -2)
batch_centers = {
    'Batch 1': np.array([-2, 2]),
    'Batch 2': np.array([2, -2])
}
# Biological groups will be slightly offset from batch centers
condition_offsets = {
    'Control': np.array([-0.5, -0.5]),
    'Treated': np.array([0.5, 0.5])
}
scatter = 1.0

# --- Generate Data ---
data = []
for batch_name, batch_center in batch_centers.items():
    for cond_name, cond_offset in condition_offsets.items():
        # Generate random points for this specific group
        points = np.random.normal(0, scatter, (n_samples_per_group // 2, 2))
        points += batch_center + cond_offset
        for point in points:
            data.append({'pc1': point[0], 'pc2': point[1], 'batch': batch_name, 'condition': cond_name})

# --- Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 8))

# Define colors and markers
colors = {'Batch 1': '#E65100', 'Batch 2': '#1E88E5'}
markers = {'Control': 'o', 'Treated': 'X'}

# Plot the data
for item in data:
    ax.scatter(item['pc1'], item['pc2'], 
               c=colors[item['batch']],
               marker=markers[item['condition']],
               s=100, alpha=0.7)

# --- Aesthetics and Legends ---
# ax.set_title('Figure 2: A Simulated PCA Plot Showing a Strong Batch Effect', fontsize=16, pad=20) # Removed to avoid duplicate captions
ax.set_xlabel('Principal Component 1 (PC1)', fontsize=12)
ax.set_ylabel('Principal Component 2 (PC2)', fontsize=12)

# Create custom legends outside the plot area
from matplotlib.lines import Line2D
legend_elements_batch = [Line2D([0], [0], marker='s', color='w', label='Batch 1', markerfacecolor=colors['Batch 1'], markersize=10),
                         Line2D([0], [0], marker='s', color='w', label='Batch 2', markerfacecolor=colors['Batch 2'], markersize=10)]
# Place batch legend outside on the right
legend1 = ax.legend(handles=legend_elements_batch, title="Batch", loc="upper left", bbox_to_anchor=(1.02, 1), fontsize=10)

legend_elements_cond = [Line2D([0], [0], marker='o', color='w', label='Control', markerfacecolor='gray', markersize=10),
                        Line2D([0], [0], marker='X', color='w', label='Treated', markerfacecolor='gray', markersize=10)]
# Place condition legend below the first one
legend2 = ax.legend(handles=legend_elements_cond, title="Condition", loc="upper left", bbox_to_anchor=(1.02, 0.8), fontsize=10)
ax.add_artist(legend1) # Add the first legend back

ax.grid(True)

# --- Save Figure ---
output_filename = 'figure_2_batch_effect_pca.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
