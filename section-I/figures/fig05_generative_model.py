from graphviz import Digraph

# Create a new Digraph
dot = Digraph('GenerativeModel')
dot.attr(compound='true', rankdir='TB', splines='spline', fontname='Helvetica', fontsize='14')
dot.attr('graph', dpi='300', size='8,11!', ranksep='1.2', nodesep='0.6')
dot.attr('node', margin='0.1')

# Define the new global color palette
colors = {
    'biology': '#0D47A1',     # Dark Blue
    'measurement': '#2E7D32',# Dark Green
    'data': '#C62828'         # Dark Red
}

# --- Biological Process Subgraph ---
with dot.subgraph(name='cluster_biology') as c:
    c.attr(label='The Biological Process', color=colors['biology'], fontname='Helvetica-Bold', style='rounded')
    c.node('dna', 'DNA', shape='folder', style='filled', fillcolor=colors['biology'], fontcolor='white')
    c.node('mrna', 'mRNA Population', shape='ellipse')
    c.edge('dna', 'mrna', label=' Transcription (α)')
    c.edge('mrna', 'mrna', label='   Degradation (β)  ')

# --- Measurement Process Subgraph ---
with dot.subgraph(name='cluster_measurement') as c:
    c.attr(label='The Measurement Process', color=colors['measurement'], fontname='Helvetica-Bold', style='rounded')
    c.node('sampling', 'Sampling\\n(The Lottery)', shape='box', style='rounded')
    c.node('bias', 'Systematic Bias\\n(GC Content, Gene Length)', shape='box', style='rounded')
    c.node('noise', 'Technical Noise\\n(Sequencer Error)', shape='box', style='rounded')
    # Invisible edges to order them
    c.edge('sampling', 'bias', style='invis')
    c.edge('bias', 'noise', style='invis')

# --- Final Data Node ---
dot.node('counts_table', '{ <f0> Gene | <f1> Count } | { ... | ... } | { <f2> HSP104 | <f3> 157 }',
         shape='record', style='filled', fillcolor=colors['data'], fontcolor='white', labeljust='l')


# --- Edges connecting the main components ---
dot.edge('mrna', 'sampling', lhead='cluster_measurement', ltail='cluster_biology', label='True, Unseen RNA Population', fontsize='12')
dot.edge('noise', 'counts_table', label='Final Observed Data', fontsize='12')


# Save the figure
output_filename = 'figure_3_generative_model'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 3 saved as '{output_filename}.png'")
