# Section I: How to Think About Biological Data

This directory contains the first section of the "Let's Simplify Bioinformatics" book project.

## Overview

This section establishes the conceptual and epistemological foundation for understanding biological data. It covers:
-   **Chapter 1: How to Think About Biological Data** (Data as a shadow of reality)
-   **Chapter 2: Generative Processes and Measurement** (How biology becomes numbers)
-   **Chapter 3: Noise, Bias, and Uncertainty** (Identifying and characterizing imperfections)
-   **Chapter 4: Context, Scale, and Interpretation** (Making robust scientific conclusions)

## Contents

-   `section-I.md`: The master Markdown file for this section, containing metadata and including all chapters for compilation.
-   `chapter-01.md` through `chapter-04.md`: Individual Markdown files for each chapter.
-   `figures/`: A subdirectory containing all Python scripts (`.py`) used to generate the figures, and the resulting PNG image files (`.png`) embedded in the chapters.
-   `Section-I_How-to-Think-About-Biological-Data_v0.1.pdf`: The compiled PDF version of this section.

## Compilation

The PDF can be compiled using Pandoc. Navigate to this directory (`section-I/`) and run:

```bash
pandoc section-I.md chapter-01.md chapter-02.md chapter-03.md chapter-04.md -o Section-I_How-to-Think-About-Biological-Data_v0.1.pdf --pdf-engine=xelatex --from markdown --syntax-highlighting=tango
```

Ensure Pandoc and a LaTeX distribution (like TeX Live) with `xelatex` are installed.
