# SEE Degeneration App
Interactive Degeneration Viewer for the Spiral Exponential Equation

This repository provides an interactive Python-based visualizer for exploring
the degeneration structure of the Spiral Exponential Equation (SEE).

It is designed as a research and visualization tool for analyzing how the
n-th order Spiral Exponential Equation degenerates into lower-order kinematic
states through a fixed geometric angle.
This tool provides an intuitive way to understand how higher-order derivative
structures collapse and how kinematic behavior emerges from the degeneration
process.

<img width="1200" height="500" alt="SEE_Degeneration_(Kinematic_Dictionary)" src="https://github.com/user-attachments/assets/3f8e77ea-0897-4f03-9515-b9340df8bb28" />

## Features
Interactive control of the derivative order n (1 ≤ n ≤ 10).
Automatic computation of the degeneration angle θ = π / (2n).
Display of the Spiral Exponential Equation:
f^(n)(t) = e^(inθ) f(t).
Display of the degenerate (real) form:
f^(n)(t) = cos(nθ) f(t).
Automatic derivation of the final degenerate equation:
f^(n)(t) = 0.
Visualization of derivative directions (0·θ, 1·θ, 2·θ, ..., n·θ) in the complex plane.
Color-coded vectors for position, velocity, acceleration, jerk, and snap.
Visualization of equal angular spacing θ using arc markers.
Automatic identification of the corresponding kinematic state
(e.g. rest, uniform motion, constant acceleration, constant jerk).

## Requirements
Python 3.8+
Install dependencies:
pip install numpy matplotlib

## Installation
You can install all dependencies using pip:
```bash
pip install -r requirements.txt
```

## Quick Start
Clone the repository and run the visualizer:
```bash
git clone https://github.com/KoheiAbeLab/see-degeneration-app
cd see-degeneration-app
python see_degeneration_app.py
```

## Usage
Run the visualizer:
python see_degeneration_app.py

Controls:
Slider n → change the order of the derivative
The left panel updates equations and kinematic interpretation automatically
The right panel shows derivative directions spaced by θ in the complex plane

## File Structure
see_degeneration_app.py — main visualization script
README.md — description and documentation

## Citation
Kohei Abe,
“SEE Degeneration App”,
GitHub repository,
https://github.com/KoheiAbeLab/see-degeneration-app

### BibTeX
```bibtex
@misc{abe2025_spiraldegeneration,
  author       = {Kohei Abe},
  title        = {SEE Degeneration App},
  year         = {2025},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/KoheiAbeLab/see-degeneration-app}}
}
```

## License
MIT License

## Download
Stable releases can be downloaded from the GitHub Releases page:
https://github.com/KoheiAbeLab/see-degeneration-app/releases

### Known Issues
- Rendering speed depends on Matplotlib and may vary across environments
- Large values of n may reduce visual clarity due to overlapping vectors

### Limitations
- Visualization focuses on geometric interpretation rather than numerical precision
- Degeneration is shown at the level of directional structure, not time evolution
- Intended for conceptual and theoretical exploration

## Contact
Kohei Abe

ORCID: https://orcid.org/0009-0001-1126-3282

GitHub: https://github.com/KoheiAbeLab
