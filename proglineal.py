# Importamos OR-Tools para programación lineal
from ortools.linear_solver import pywraplp
#Crear un solucionador utilizando GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

'''Creamos las variables que queremos optimizar: espadachines, arqueros y jinetes.'''

espadachin = solver.IntVar(0, solver.infinity(), 'espadachin')    #solver.IntVar() por ser variables enteras y solver.infinity() porque el limite superior de espadachines es infinito.
arquero = solver.IntVar(0, solver.infinity(), 'arquero')   #lo mismo
jinete = solver.IntVar(0, solver.infinity(), 'jinete')   #lo mismo


'''Creamos las restricciones para cada recurso mediante ecuaciones. En este caso, no podemos gastar mas recursos de los que tenemos: comida 1200, madera 800 y oro 600
Con solver.Add() añadimos las restricciones'''

#Añadimos las restricciones
solver.Add(espadachin*60 + arquero*80 + jinete*140 <=1200)  #ecuación comida
solver.Add(espadachin*20 + arquero*10 <= 800)  #ecuación madera
solver.Add(arquero*40 + jinete*100 <= 600)  #ecuación oro


'''Creamos nuestra función objetivo. En este caso, queremos maximizar el poder del ejército, lo hacemos maximizando la suma del poder de cada unidad. 
Existen dos tipos de funciones objetivos: maximizar y minimizar. En este caso, queremos maximizar, por lo que usamos solver.Maximize(), si no sería solver.Minimize()'''

#Maximizamos la función objetivo
solver.Maximize(espadachin*70 + arquero*95 + jinete*230)


'''Calculamos la solución óptima con solver.Solve()'''

