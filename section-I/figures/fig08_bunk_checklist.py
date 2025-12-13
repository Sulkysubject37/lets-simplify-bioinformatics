from graphviz import Digraph

# Create a new Digraph
dot = Digraph('BUNK_Checklist')
dot.attr(beautify='true', layout='twopi', overlap='false', splines='curved', fontname='Helvetica')
dot.attr('graph', dpi='300', ranksep='0.8', root='CENTER')
dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica-Bold', fontsize='14', margin='0.2')

# Define the new global color palette
colors = {
    'center': '#37474F',      # Blue Grey Dark
    'B': '#E65100',           # Orange
    'U': '#C62828',           # Red
    'N': '#0D47A1',           # Blue
    'K': '#2E7D32'            # Green
}

# Central Node
dot.node('CENTER', 'Any Result or\n"Discovery"', 
         shape='diamond', 
         style='filled,diagonals',
         fillcolor=colors['center'], 
         fontcolor='white',
         fontsize='16')

# B.U.N.K. Nodes (re-ordered for clockwise layout)
nodes_info = {
    'N': 'Noise\nCould this be due to\nrandom chance alone?',
    'B': 'Bias\nWhat systematic errors\ncould create this pattern?',
    'K': 'Kontext (Context)\nDoes this make sense\nin the known biological context?',
    'U': 'Uncertainty\nHow confident are we?\n(e.g., error bars, p-value)'
}

for key, label in nodes_info.items():
    dot.node(key, label, fillcolor=colors[key], fontcolor='white')

# Edges from Center to B.U.N.K. nodes (re-ordered)
dot.edge('CENTER', 'N', color=colors['N'])
dot.edge('CENTER', 'B', color=colors['B'])
dot.edge('CENTER', 'K', color=colors['K'])
dot.edge('CENTER', 'U', color=colors['U'])


# Save the figure
output_filename = 'figure_3_bunk_checklist'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 3 saved as '{output_filename}.png'")
