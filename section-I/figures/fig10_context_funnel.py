from graphviz import Digraph

# Create a new Digraph
dot = Digraph('ContextFunnel')
dot.attr(rankdir='TB', splines='line', fontname='Helvetica', fontsize='14')
dot.attr('graph', dpi='300', size='8,11!')
dot.attr('node', shape='box', style='rounded,filled', margin='0.1')

# Define the new global color palette
colors = {
    'start': '#C62828',   # Dark Red
    'filter': '#1E88E5',  # Blue
    'end': '#2E7D32'     # Dark Green
}

# --- Nodes ---
dot.node('start', 'Statistically Significant Result\n(e.g., p < 0.05)', 
         shape='ellipse', fillcolor=colors['start'], fontcolor='white')

dot.node('filter1', 'Biological Context\n(Is the gene a known oncogene?)', 
         shape='invtrapezium', fillcolor=colors['filter'], fontcolor='white')

dot.node('filter2', 'Experimental Context\n(Was this a relevant cell line / time point?)', 
         shape='invtrapezium', fillcolor=colors['filter'], fontcolor='white')

dot.node('filter3', 'Analytical Context\n(How was the data normalized / tested?)', 
         shape='invtrapezium', fillcolor=colors['filter'], fontcolor='white')

dot.node('end', 'Meaningful Scientific Interpretation', 
         shape='egg', fillcolor=colors['end'], fontcolor='white', fontsize='16')

# --- Edges to create the funnel flow ---
dot.edge('start', 'filter1', style='bold')
dot.edge('filter1', 'filter2', style='bold')
dot.edge('filter2', 'filter3', style='bold')
dot.edge('filter3', 'end', style='bold')


# --- Save the figure ---
output_filename = 'figure_1_context_funnel'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 1 saved as '{output_filename}.png'")
