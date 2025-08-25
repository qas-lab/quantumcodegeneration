from qiskit import QuantumCircuit
from math import pi

def ansatz():
    qc = QuantumCircuit(4, 4)
    # Apply Ry and Rz gates with theta=pi/2
    qc.ry(pi/2, 0)
    qc.ry(pi/2, 1)
    qc.ry(pi/2, 2)
    qc.ry(pi/2, 3)
    qc.rz(pi/2, 0)
    qc.rz(pi/2, 1)
    qc.rz(pi/2, 2)
    qc.rz(pi/2, 3)
    # Apply CNOT gates
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    # Apply Ry and Rz gates with theta=pi/2
    qc.ry(pi/2, 0)
    qc.ry(pi/2, 1)
    qc.ry(pi/2, 2)
    qc.ry(pi/2, 3)
    qc.rz(pi/2, 0)
    qc.rz(pi/2, 1)
    qc.rz(pi/2, 2)
    qc.rz(pi/2, 3)
    # Measure
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
    return qc