from qiskit import QuantumCircuit
import numpy as np

def QAOAcircuit():
    # Create a quantum circuit with 4 qubits
    qc = QuantumCircuit(4)

    # Apply U gates with parameters (0, pi, 0) to each qubit
    qc.u(0, np.pi, 0, 0)
    qc.u(0, np.pi, 0, 1)
    qc.u(0, np.pi, 0, 2)
    qc.u(0, np.pi, 0, 3)

    # Apply CNOT gates as per the UML model
    qc.cx(0, 1)
    qc.rz(2 * (np.pi / 2), 1)
    qc.cx(0, 1)
    qc.cx(0, 3)
    qc.rz(2 * (np.pi / 2), 3)
    qc.cx(0, 3)
    qc.cx(1, 2)
    qc.rz(2 * (np.pi / 2), 2)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.rz(2 * (np.pi / 2), 3)
    qc.cx(2, 3)

    return qc