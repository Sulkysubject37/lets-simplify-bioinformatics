import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# --- Setup ---
plt.style.use('seaborn-v0_8-whitegrid')
fig = plt.figure(figsize=(12, 12))
# fig.suptitle('Figure 2: Interpretation Depends on the Scale of Observation', fontsize=18, y=0.97) # Removed to avoid duplicate captions

# --- Panel 1: Tissue Scale ---
ax1 = fig.add_subplot(2, 2, 1)
ax1.set_title('A) Tissue Scale', fontsize=14, pad=10)
# Simulate a mix of cells
ax1.add_patch(patches.Rectangle((0.1, 0.1), 0.8, 0.8, fill=True, color='lightgray', alpha=0.3))
# "Active" cells (rare)
ax1.plot([0.2, 0.5, 0.7], [0.3, 0.8, 0.5], 'o', color='#C62828', markersize=10)
# "Inactive" cells (common)
ax1.plot(np.random.rand(20) * 0.8 + 0.1, np.random.rand(20) * 0.8 + 0.1, 'o', color='gray', markersize=10, alpha=0.5)
ax1.text(0.5, 0.05, '"Gene X appears lowly expressed on average"', ha='center', style='italic')
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_xlim(0, 1)
ax1.set_ylim(0, 1)

# --- Panel 2: Single-Cell Scale ---
ax2 = fig.add_subplot(2, 2, 2)
ax2.set_title('B) Single-Cell Scale (Zoomed In)', fontsize=14, pad=10)
# A single active cell
ax2.add_patch(patches.Circle((0.5, 0.5), 0.4, fill=True, color='#C62828', alpha=0.3))
ax2.text(0.5, 0.5, 'Gene X\\nActive', ha='center', va='center', fontsize=12, color='white')
ax2.text(0.5, 0.05, '"Gene X is highly active in this cell type"', ha='center', style='italic')
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)

# --- Panel 3: Chromosome Scale ---
ax3 = fig.add_subplot(2, 2, 3)
ax3.set_title('C) Chromosome Scale', fontsize=14, pad=10)
# Draw a chromosome shape
ax3.add_patch(patches.Ellipse((0.5, 0.5), 0.2, 0.8, angle=20, color='#1E88E5', alpha=0.6))
ax3.add_patch(patches.Ellipse((0.5, 0.5), 0.2, 0.8, angle=-20, color='#1E88E5', alpha=0.6))
# Highlight a large region
ax3.add_patch(patches.Rectangle((0.4, 0.6), 0.2, 0.2, fill=True, color='#C62828', alpha=0.5))
ax3.text(0.5, 0.05, '"A large chromosomal deletion is visible"', ha='center', style='italic')
ax3.set_xticks([])
ax3.set_yticks([])
ax3.set_xlim(0, 1)
ax3.set_ylim(0, 1)

# --- Panel 4: Gene Scale ---
ax4 = fig.add_subplot(2, 2, 4)
ax4.set_title('D) Gene Scale (Zoomed In)', fontsize=14, pad=10)
# Draw a gene structure
ax4.plot([0.1, 0.9], [0.5, 0.5], color='gray', linewidth=4)
# Exons
ax4.add_patch(patches.Rectangle((0.2, 0.4), 0.1, 0.2, fill=True, color='#2E7D32'))
ax4.add_patch(patches.Rectangle((0.6, 0.4), 0.2, 0.2, fill=True, color='#2E7D32'))
# A single SNP
ax4.plot(0.45, 0.6, 'v', color='#E65100', markersize=15)
ax4.text(0.45, 0.7, 'SNP', ha='center')
ax4.text(0.5, 0.05, '"A single nucleotide variant is visible"', ha='center', style='italic')
ax4.set_xticks([])
ax4.set_yticks([])
ax4.set_xlim(0, 1)
ax4.set_ylim(0, 1)

# --- Final Touches ---
plt.tight_layout(rect=[0, 0, 1, 0.95])

# --- Save Figure ---
output_filename = 'figure_2_scales_of_biology.png'
plt.savefig(output_filename, dpi=300, bbox_inches='tight')

print(f"Figure saved as '{output_filename}'")
