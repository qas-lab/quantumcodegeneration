from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def circuit1() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    qc = QuantumCircuit(q0, q1, q2, q3)

    # Apply H gates
    qc.h(q0)
    qc.h(q1)
    qc.h(q2)
    qc.h(q3)

    # Apply P gates with specified theta
    qc.p(2 * (np.pi / 2), q0)
    qc.p(2 * (np.pi / 2), q1)
    qc.p(2 * (np.pi / 2), q2)
    qc.p(2 * (np.pi / 2), q3)

    # Apply CNOT gates
    qc.cx(q0, q1)
    qc.cx(q0, q2)
    qc.cx(q1, q2)
    qc.cx(q0, q3)
    qc.cx(q1, q3)
    qc.cx(q2, q3)

    return qc