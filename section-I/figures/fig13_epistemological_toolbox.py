from graphviz import Digraph

# Create a new Digraph
dot = Digraph('EpistemologicalToolbox')
dot.attr(rankdir='TB', splines='ortho', fontname='Helvetica', fontsize='14')
dot.attr('graph', dpi='300', ranksep='0.8', nodesep='0.5')
dot.attr('node', shape='box', style='rounded,filled', margin='0.2', fontname='Helvetica-Bold')

# Define the new global color palette
colors = {
    'origin': '#0D47A1',      # Dark Blue
    'model': '#2E7D32',       # Dark Green
    'bunk': '#E65100',       # Dark Orange
    'trip': '#5E35B1',       # Deep Purple
    'conclusion': '#C62828'   # Dark Red
}

# --- Nodes representing each framework ---
dot.node('origin', 'ORIGIN Framework\n(Data Provenance)', fillcolor=colors['origin'], fontcolor='white')
dot.node('model', 'Generative Model\n(Conceptualizing the Process)', fillcolor=colors['model'], fontcolor='white')
dot.node('bunk', 'B.U.N.K. Checklist\n(Result Sanity Check)', fillcolor=colors['bunk'], fontcolor='white')
dot.node('trip', 'T.R.I.P. Check\n(Conclusion Robustness)', fillcolor=colors['trip'], fontcolor='white')
dot.node('conclusion', 'Robust, Hypothesis-Driven\nInterpretation', shape='egg', fillcolor=colors['conclusion'], fontcolor='white', fontsize='16')

# --- Invisible nodes for layout help ---
with dot.subgraph() as s:
    s.attr(rank='same')
    s.node('raw_data', 'Raw Data', shape='folder')
    s.node('initial_result', 'Initial Result / Pattern', shape='note')

# --- Edges to create the flow ---
dot.edge('raw_data', 'origin', label=' Apply to')
dot.edge('origin', 'model')
dot.edge('model', 'initial_result', lhead='initial_result', label=' Leads to')
dot.edge('initial_result', 'bunk', label=' Apply to')
dot.edge('bunk', 'trip')
dot.edge('trip', 'conclusion')

# --- Save the figure ---
output_filename = 'figure_4_epistemological_toolbox'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 4 saved as '{output_filename}.png'")
