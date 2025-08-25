from qiskit import QuantumCircuit
import math

def circuit1():
    qc = QuantumCircuit(4)
    # Initial H gates
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)
    # P gates
    qc.p(2 * (math.pi / 2), 0)
    qc.p(2 * (math.pi / 2), 1)
    qc.p(2 * (math.pi / 2), 2)
    qc.p(2 * (math.pi / 2), 3)
    # CNOT gates
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.cx(0, 3)
    qc.cx(1, 2)
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 3)
    qc.cx(2, 3)
    qc.cx(2, 3)
    return qc