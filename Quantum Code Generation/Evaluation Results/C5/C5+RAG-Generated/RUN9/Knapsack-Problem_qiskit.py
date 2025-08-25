from qiskit import QuantumCircuit, QuantumRegister
from math import pi

def QAOAcircuit():
    q = QuantumRegister(4, 'q')
    circuit = QuantumCircuit(q)

    # Initial U gates
    circuit.u(0, pi, 0, q[0])
    circuit.u(0, pi, 0, q[1])
    circuit.u(0, pi, 0, q[2])
    circuit.u(0, pi, 0, q[3])

    # CNOT gates
    circuit.cx(q[0], q[1])
    circuit.rz(2 * (pi / 2), q[1])
    circuit.cx(q[0], q[1])
    circuit.cx(q[0], q[3])
    circuit.rz(2 * (pi / 2), q[3])
    circuit.cx(q[0], q[3])
    circuit.cx(q[1], q[2])
    circuit.rz(2 * (pi / 2), q[2])
    circuit.cx(q[1], q[2])
    circuit.cx(q[2], q[3])
    circuit.rz(2 * (pi / 2), q[3])
    circuit.cx(q[2], q[3])

    return circuit