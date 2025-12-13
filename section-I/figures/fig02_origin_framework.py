from graphviz import Digraph

# Create a new Digraph
dot = Digraph('ORIGIN_Framework_Mind_Map')
dot.attr(beautify='true', layout='twopi', overlap='false', splines='curved', fontname='Helvetica')
dot.attr('graph', dpi='300', ratio='auto', root='CENTER')
dot.attr('node', shape='box', style='rounded,filled', fontname='Helvetica-Bold', fontsize='14')

# Define the new global color palette
colors = {
    'center': '#37474F',      # Blue Grey Dark
    'O': '#0D47A1',           # Dark Blue
    'R': '#2E7D32',           # Dark Green
    'I1': '#E65100',          # Dark Orange
    'G': '#FFC107',           # Amber
    'I2': '#E65100',          # Dark Orange (same as I1)
    'N': '#C62828'            # Dark Red
}

# Central Node
dot.node('CENTER', 'A Single\\nData Point', 
         shape='doublecircle', 
         fillcolor=colors['center'], 
         fontcolor='white',
         fontsize='14')

# ORIGIN Nodes with proper line breaks
nodes_info = {
    'O': 'Objective\\nWhat was the question?',
    'R': 'Reality\\nWhat was the system?',
    'I1': 'Instrument\\nWhat was the technology?',
    'G': 'Generation\\nWhat was the wet lab process?',
    'I2': 'Interpretation\\nWhat was the dry lab process?',
    'N': 'Number\\nWhat does it finally represent?'
}

for key, label in nodes_info.items():
    dot.node(key, label, fillcolor=colors[key], fontcolor='white')

# Edges from Center to ORIGIN nodes
dot.edge('CENTER', 'O', color=colors['O'])
dot.edge('CENTER', 'R', color=colors['R'])
dot.edge('CENTER', 'I1', color=colors['I1'], label=' I ')
dot.edge('CENTER', 'G', color=colors['G'])
dot.edge('CENTER', 'I2', color=colors['I2'], label=' I ')
dot.edge('CENTER', 'N', color=colors['N'])


# Save the figure
output_filename = 'figure_2_origin'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 2 (revised) saved as '{output_filename}.png'")