from qiskit import QuantumCircuit
import math

def QAOAcircuit():
    qc = QuantumCircuit(4)
    # Apply U gates
    qc.u(0, math.pi, 0, 0)
    qc.u(0, math.pi, 0, 1)
    qc.u(0, math.pi, 0, 2)
    qc.u(0, math.pi, 0, 3)
    # Apply CNOT gates
    qc.cx(0, 1)
    qc.rz(2 * (math.pi / 2), 1)
    qc.cx(0, 1)
    qc.cx(0, 3)
    qc.rz(2 * (math.pi / 2), 3)
    qc.cx(0, 3)
    qc.cx(1, 2)
    qc.rz(2 * (math.pi / 2), 2)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.rz(2 * (math.pi / 2), 3)
    qc.cx(2, 3)
    return qc