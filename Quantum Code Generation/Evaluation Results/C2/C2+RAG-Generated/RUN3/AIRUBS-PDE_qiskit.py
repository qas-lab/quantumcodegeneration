from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def circuit1() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    circuit = QuantumCircuit(q0, q1, q2, q3)

    # Apply H gates
    circuit.h(q0)
    circuit.h(q1)
    circuit.h(q2)
    circuit.h(q3)

    # Apply P gates with parameters
    circuit.p(2 * (np.pi / 2), q0)
    circuit.p(2 * (np.pi / 2), q1)
    circuit.p(2 * (np.pi / 2), q2)
    circuit.p(2 * (np.pi / 2), q3)

    # Apply CNOT gates
    circuit.cx(q0, q1)
    circuit.cx(q0, q2)
    circuit.cx(q1, q2)
    circuit.cx(q0, q3)
    circuit.cx(q1, q3)
    circuit.cx(q2, q3)

    return circuit