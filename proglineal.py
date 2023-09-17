# Importamos OR-Tools para programación lineal
from ortools.linear_solver import pywraplp
#Crear un solucionador utilizando GLOP backend
solver = pywraplp.Solver('Maximize army power', pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

'''Creamos las variables que queremos optimizar: espadachines, arqueros y jinetes.'''

esapdachines = solver.IntVar(0, solver.infinity(), 'espadachines')    #.IntVar por ser variables enteras y solver.infinity() porque el limite superior de espadachines es infinito.
arqueros = solver.IntVar(0, solver.infinity(), 'arqueros')   #lo mismo
jinetes = solver.IntVar(0, solver.infinity(), 'jinetes')   #lo msimo