from graphviz import Digraph

# Create a new Digraph
dot = Digraph('JourneyToShadow')
dot.attr(compound='true', rankdir='LR', splines='spline', fontname='Helvetica', fontsize='14')
dot.attr('graph', dpi='300', size='12,7!', ranksep='1.0')

# Define the new global color palette
colors = {
    'primary': '#0D47A1',     # Dark Blue
    'secondary': '#1E88E5',   # Blue
    'accent_green': '#2E7D32',# Dark Green
    'accent_orange': '#E65100',# Dark Orange
    'accent_red': '#C62828',   # Dark Red
    'neutral_light': '#CFD8DC',
    'neutral_dark': '#37474F'
}

# Panel 1: The Unseen Reality
with dot.subgraph(name='cluster_reality') as c:
    c.attr(label='Panel 1: The Unseen Reality', color=colors['primary'], fontname='Helvetica-Bold')
    c.node('cell', 'Yeast Cell', shape='doublecircle', style='filled', fillcolor=colors['primary'], fontcolor='white')
    c.node('proteins', 'Proteins', shape='ellipse')
    c.node('lipids', 'Lipids', shape='ellipse')
    c.node('metabolites', 'Metabolites', shape='ellipse')
    c.node('mrna', 'mRNA', shape='ellipse', style='filled', fillcolor=colors['secondary'])
    
    # Edges within reality to show complexity
    c.edge('cell', 'proteins', style='invis')
    c.edge('cell', 'lipids', style='invis')
    c.edge('cell', 'metabolites', style='invis')
    c.edge('cell', 'mrna', style='invis')


# Panel 2: The Great Abstraction
with dot.subgraph(name='cluster_abstraction') as c:
    c.attr(label='Panel 2: The Great Abstraction', color=colors['accent_green'], fontname='Helvetica-Bold')
    c.node('funnel', 'RNA-Seq Protocol\n(Poly-A Selection)', shape='invtrapezium', style='filled', fillcolor=colors['accent_green'], fontcolor='white')

# Panel 3: The Digital Translation
with dot.subgraph(name='cluster_translation') as c:
    c.attr(label='Panel 3: The Digital Translation', color=colors['accent_orange'], fontname='Helvetica-Bold')
    c.node('sequencer', 'Sequencing Machine', shape='cds', style='filled', fillcolor=colors['accent_orange'], fontcolor='white')
    c.node('reads', '"ATCG..." Sequence Reads', shape='note')

# Panel 4: The Final Shadow
with dot.subgraph(name='cluster_representation') as c:
    c.attr(label='Panel 4: The Final Shadow', color=colors['accent_red'], fontname='Helvetica-Bold')
    c.node('table', '{ <f0> Gene | <f1> Count } | { <f2> HSP104 | <f3> 157 }', shape='record', style='filled', fillcolor=colors['accent_red'], fontcolor='white')

# Edges connecting the panels
dot.edge('mrna', 'funnel', lhead='cluster_abstraction', label='  Information Loss  ', style='dashed', fontsize='12')
dot.edge('funnel', 'sequencer', lhead='cluster_translation', label='  (Biases Introduced)  ', style='dashed', fontsize='12')
dot.edge('sequencer', 'reads')
dot.edge('reads', 'table', lhead='cluster_representation', label='  (Alignment & Counting)  ', style='dashed', fontsize='12')


# Save the figure
output_filename = 'figure_1_journey'
dot.render(output_filename, format='png', cleanup=True)

print(f"Figure 1 (revised) saved as '{output_filename}.png'")