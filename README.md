# pyCalcErr
calculate Gauss propagation of uncertainty and output corresponding latex equation

propagation of uncertainty (used in this package):
<br/>
<br/>
<img src="https://latex.codecogs.com/gif.latex?s_f%20=%20\sqrt{%20\left(\frac{\partial%20f}{\partial%20x}\right)^2%20s_x^2%20+%20\left(\frac{\partial%20f}{\partial%20y}%20\right)^2%20s_y^2%20+%20\left(\frac{\partial%20f}{\partial%20z}%20\right)^2%20s_z^2%20+%20\cdots}" /> 
<br/>
<br/>
install using pip:

```
pip install pyCalcErr
```
Usage:
```
pyCalcErr <equation left side>", "<equation_right_side> <deriveAfter_1,...>"
```

Example: 
```
pyCalcErr E_pot 1/2*k*x**2 'x'
```


