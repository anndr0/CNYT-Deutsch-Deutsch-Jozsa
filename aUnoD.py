import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
def Test():
    print("PRUEBAS EX. DEUTSCH FUNCIÓN A UNO")
    print("\nFunción Constante")
    res2 = []
    simulator = Aer.get_backend('qasm_simulator')
    circuit = QuantumCircuit(2, 1)

    circuit.x(1)

    circuit.barrier(0,1)
    circuit.h(0)
    circuit.h(1)
    circuit.barrier(0,1)

    circuit.x(1)

    circuit.barrier(0,1)
    circuit.h(0)
    circuit.barrier(0,1)

    circuit.measure([0], [0])
    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts(circuit)
    res2.append(counts)
    print("\nTotal count for 00 and 11 are:",counts)
    print(circuit)
    plot_histogram(counts)
    plt.show()
    res2 = list(res2)
    return res2