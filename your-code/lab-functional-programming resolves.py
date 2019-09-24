import pandas as pd
import numpy as np
#Ejercicio 1 de functional programming
def divisible2(iterator):
    c=0
    for i in iterator:
        if i%2==0:
            return i
            c=c+1
        else:
            continue
    if c==0:
        return 0
a=[1,2,3,9,90]
print(divisible2(a))
#Ejercicio 2 de funciontal programming
#Generators
def even_iterator(n):
    number = 0
    while number <= n:
        if number%2==0:
            yield number
        number = number + 1
iterator=even_iterator(5)
for i in iterator:
    print(i)
columns = ['sepal_length', 'sepal_width', 'petal_length','petal_width','iris_type']
iris = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data", names=columns)
iris_head=iris.head()
print(iris.head())
print(np.mean(iris.head()))
print(np.std(iris.head()))
#Observación en np.mean: Reconoce las columnas númericas flotantes y saca su mediana
#Observación en np.mean: Reconoce las columnas númericas flotantes y saca su desviación estándar
iris_numeric=iris.head().filter(items=['sepal_length', 'sepal_width', 'petal_length','petal_width'])
print(iris_numeric)
def cm_to_in(x):
         return x*(0.393701)
print(cm_to_in(1))
iris_inch=cm_to_in(iris_numeric)
print(iris_inch)
def add_constant(v): # no necesitamos argumentos porque le pasaremos valores
    return v+2
print(add_constant(2))
iris_constant=add_constant(iris_numeric)
print(iris_constant)