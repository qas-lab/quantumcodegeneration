import numpy as np
from qiskit import QuantumCircuit, QuantumRegister

def ansatz() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    circuit = QuantumCircuit(q0, q1, q2, q3)

    circuit.ry(np.pi/2, q0)
    circuit.ry(np.pi/2, q1)
    circuit.ry(np.pi/2, q2)
    circuit.ry(np.pi/2, q3)
    circuit.rz(np.pi/2, q0)
    circuit.rz(np.pi/2, q1)
    circuit.rz(np.pi/2, q2)
    circuit.rz(np.pi/2, q3)

    circuit.cx(q0, q1)
    circuit.cx(q1, q2)
    circuit.cx(q2, q3)
    circuit.cx(q0, q1)
    circuit.cx(q1, q2)
    circuit.cx(q2, q3)
    circuit.cx(q0, q1)
    circuit.cx(q1, q2)
    circuit.cx(q2, q3)

    circuit.ry(np.pi/2, q0)
    circuit.ry(np.pi/2, q1)
    circuit.ry(np.pi/2, q2)
    circuit.ry(np.pi/2, q3)
    circuit.rz(np.pi/2, q0)
    circuit.rz(np.pi/2, q1)
    circuit.rz(np.pi/2, q2)
    circuit.rz(np.pi/2, q3)

    return circuit