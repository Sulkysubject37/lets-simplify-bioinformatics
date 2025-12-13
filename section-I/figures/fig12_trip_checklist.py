from graphviz import Digraph

# Create a new Digraph
dot = Digraph('TRIP_Checklist')
dot.attr(rankdir='TB', splines='ortho', fontname='Helvetica', fontsize='14')
dot.attr('graph', dpi='300', nodesep='0.6')
dot.attr('node', shape='box', style='rounded,filled', margin='0.2', fontname='Helvetica-Bold')

# Define the new global color palette
colors = {
    'T': '#0D47A1',      # Dark Blue
    'R': '#2E7D32',      # Dark Green
    'I': '#E65100',      # Dark Orange
    'P': '#C62828',      # Dark Red
    'start': '#37474F'   # Blue Grey Dark
}

# --- Nodes ---
dot.node('start', 'Scientific Observation\\nor Conclusion', shape='ellipse', fillcolor=colors['start'], fontcolor='white')

dot.node('T', 'Triangulate\\n(Support from other data types?)', fillcolor=colors['T'], fontcolor='white')
dot.node('R', 'Replicate\\n(Seen in other studies/samples?)', fillcolor=colors['R'], fontcolor='white')
dot.node('I', 'Interrogate (B.U.N.K.)\\n(Check for bias, noise, etc.?)', fillcolor=colors['I'], fontcolor='white')
dot.node('P', 'Propose Mechanism\\n(Is there a plausible biological story?)', fillcolor=colors['P'], fontcolor='white')


# --- Edges to create a cycle/checklist flow ---
dot.edge('start', 'T', style='dashed')
dot.edge('T', 'R')
dot.edge('R', 'I')
dot.edge('I', 'P')
dot.edge('P', 'start', style='dashed', constraint='false', label='  Refine/Accept Conclusion  ')

# --- Save the figure ---
output_filename = 'figure_3_trip_checklist'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 3 saved as '{output_filename}.png'")
