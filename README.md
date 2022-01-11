# Linear Algebra Helper

##### Author: Isaac Lee

### Summary
This notebook is designed to aid with tedious matrix related calculations.  
Input a matrix with a given number of rows.  
For each row input a space seperated list of elements, e.g 1 0 0 2 1  

*The following will be calculated for the input matrix A:*  
1. The eigenvectors, eigenvalues and multiplicities.  
2. The characteristic polynomial.
3. Interactive minimal polynomial calculator. (Pretty epic imo).
4. JCF, Jordan Basis and RCF Helper (Doesn't actually find RCF)
5. Gram Schmidt
6. Freeform calculator, rank, kernel, ... any sympy operation
7. Polynomials, factor over Finite fields, lcm, gcd, solve for x, ...

### Files
Both lag_helper_jupyter.ipynb and lag_helper_functions.py should
be in the same directory.
- lag_helper_jupyter.ipynb is the notebook to be run.
- lag_helper_functions.py is imported into lag_helper_jupyter and
should not be run directly.

### Requirements

```
pip install sympy
pip install jupyterlab
```

Then to run the notebook do:

```
jupyterlab lag_helper_jupyter.ipynb
```
