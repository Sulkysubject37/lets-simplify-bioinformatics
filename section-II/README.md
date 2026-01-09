# Section II: Biological Sequences as Information

This directory contains the second section of the "Let's Simplify Bioinformatics" book project.

**Author:** MD. Arshad

## Overview

This section transforms the reader’s mental model of biological sequences from linear text into spatial, probabilistic, and structural objects. It covers:
-   **Chapter 5: DNA as Information, Not Text** (Alphabet vs language, Entropy, Redundancy, Evolutionary constraint)
-   **Chapter 6: Alignment as Geometry** (Similarity as distance, Scoring as assumptions, Alignment as optimization in space)
-   **Chapter 7: Assembly as Graph Construction** (Reads → overlaps → graphs, Ambiguity, Why perfect assembly is often impossible)
-   **Chapter 8: Variation as Biological Signal** (Variation ≠ error, Null expectation, Context-dependence of impact)

## Section Summary

Section II has dismantled the "textual" view of biology. By reframing DNA as a physical information carrier (Chapter 5), we moved from characters to signal density. This foundation allowed us to redefine alignment as a geometric search in a metric manifold (Chapter 6) and assembly as a topological reconstruction from fragmented echoes (Chapter 7). Finally, we reframed variation not as an error, but as the high-resolution signal of biological individuality and evolution (Chapter 8). The reader is now equipped to view genomic data as a dynamic, 3D coordinate system rather than a static 1D string.

## Contents

-   `section-II.md`: The master Markdown file for this section, containing metadata and including all chapters for compilation.
-   `chapter-05.md` through `chapter-08.md`: Individual Markdown files for each chapter.
-   `figures/`: A subdirectory containing generated PNG and SVG image files embedded in the chapters.
-   `Section-II_Biological-Sequences-as-Information_v0.1.pdf`: The compiled PDF version of this section.

## Compilation

The PDF can be compiled using Pandoc. Navigate to this directory (`section-II/`) and run:

```bash
pandoc section-II.md chapter-05.md chapter-06.md chapter-07.md chapter-08.md -o Section-II_Biological-Sequences-as-Information_v0.1.pdf --pdf-engine=xelatex --from markdown --syntax-highlighting=tango
```

## Citation

If you use this section in your work, please cite it as:

Arshad, M. (2026). *Section II: Biological Sequences as Information*. In: Let's Simplify Bioinformatics: A Conceptual, Computational, and Interpretability-First Atlas of Biological Data Science. v0.2.