from qiskit import QuantumCircuit
from math import pi

def circuit1():
    # Create a quantum circuit with 4 qubits
    qc = QuantumCircuit(4)

    # Apply Hadamard gates
    qc.h(0)
    qc.h(1)
    qc.h(2)
    qc.h(3)

    # Apply phase gates
    qc.p(2 * (pi / 2), 0)
    qc.p(2 * (pi / 2), 1)
    qc.p(2 * (pi / 2), 2)
    qc.p(2 * (pi / 2), 3)

    # Apply CNOT gates
    qc.cx(0, 1)
    qc.cx(0, 1)
    qc.cx(0, 2)
    qc.cx(0, 2)
    qc.cx(1, 2)
    qc.cx(0, 3)
    qc.cx(1, 3)
    qc.cx(1, 3)
    qc.cx(2, 3)
    qc.cx(2, 3)

    return qc