# pyCalcErr
calculate Gauss error propagation and output corresponding latex formula
h<math xmlns="http://www.w3.org/1998/Math/MathML"><msub><mi>s</mi><mrow><mi>f</mi><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>)</mo></mrow></msub><mo>=</mo><msqrt><msup><mfenced><mrow><mfrac><mrow><mo>&#x2202;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>)</mo></mrow><mrow><mo>&#x2202;</mo><mi>x</mi></mrow></mfrac><msub><mi>s</mi><mi>x</mi></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><msup><mfenced><mrow><mfrac><mrow><mo>&#x2202;</mo><mi>f</mi><mo>(</mo><mi>x</mi><mo>,</mo><mi>y</mi><mo>,</mo><mo>.</mo><mo>.</mo><mo>.</mo><mo>)</mo></mrow><mrow><mo>&#x2202;</mo><mi>y</mi></mrow></mfrac><msub><mi>s</mi><mi>y</mi></msub></mrow></mfenced><mn>2</mn></msup><mo>+</mo><mo>.</mo><mo>.</mo><mo>.</mo></msqrt></math>h

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
