from qiskit import QuantumCircuit, QuantumRegister
from math import pi

def ansatz() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    circuit = QuantumCircuit(q0, q1, q2, q3)

    # InitialNode to Ry on q0
    circuit.ry(pi/2, q0)
    # Ry on q0 to Ry on q1
    circuit.ry(pi/2, q1)
    # Ry on q1 to Ry on q2
    circuit.ry(pi/2, q2)
    # Ry on q2 to Ry on q3
    circuit.ry(pi/2, q3)
    # Ry on q3 to Rz on q0
    circuit.rz(pi/2, q0)
    # Rz on q0 to Rz on q1
    circuit.rz(pi/2, q1)
    # Rz on q1 to Rz on q2
    circuit.rz(pi/2, q2)
    # Rz on q2 to Rz on q3
    circuit.rz(pi/2, q3)
    # CNOT(q0-q1)
    circuit.cx(q0, q1)
    # CNOT(q1-q2)
    circuit.cx(q1, q2)
    # CNOT(q2-q3)
    circuit.cx(q2, q3)
    # CNOT(q0-q1)
    circuit.cx(q0, q1)
    # CNOT(q1-q2)
    circuit.cx(q1, q2)
    # CNOT(q2-q3)
    circuit.cx(q2, q3)
    # CNOT(q0-q1)
    circuit.cx(q0, q1)
    # CNOT(q1-q2)
    circuit.cx(q1, q2)
    # CNOT(q2-q3)
    circuit.cx(q2, q3)

    return circuit