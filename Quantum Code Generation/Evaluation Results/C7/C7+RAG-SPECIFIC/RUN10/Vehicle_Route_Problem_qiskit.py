from qiskit import QuantumCircuit, QuantumRegister
from math import pi

def ansatz() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    circuit = QuantumCircuit(q0, q1, q2, q3)

    # InitialNode to ActivityFinalNode sequence
    circuit.ry(pi/2, q0[0])
    circuit.ry(pi/2, q1[0])
    circuit.ry(pi/2, q2[0])
    circuit.ry(pi/2, q3[0])
    circuit.rz(pi/2, q0[0])
    circuit.rz(pi/2, q1[0])
    circuit.rz(pi/2, q2[0])
    circuit.rz(pi/2, q3[0])
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])

    return circuit