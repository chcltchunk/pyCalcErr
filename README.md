# pyCalcErr
calculate Gauss error propagation and output corresponding latex formula
  h<sub>&theta;</sub>(x) = &theta;<sub>o</sub> x + &theta;<sub>1</sub>x

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
