from qiskit import QuantumCircuit, QuantumRegister
import math

def QAOAcircuit():
    q = QuantumRegister(4, 'q')
    circuit = QuantumCircuit(q)

    # Initial U gates
    circuit.u(0, math.pi, 0, q[0])
    circuit.u(0, math.pi, 0, q[1])
    circuit.u(0, math.pi, 0, q[2])
    circuit.u(0, math.pi, 0, q[3])

    # CNOT(q0, q1)
    circuit.cx(q[0], q[1])

    # Rz on q1
    circuit.rz(2 * (math.pi / 2), q[1])

    # CNOT(q0, q1)
    circuit.cx(q[0], q[1])

    # CNOT(q0, q3)
    circuit.cx(q[0], q[3])

    # Rz on q3
    circuit.rz(2 * (math.pi / 2), q[3])

    # CNOT(q0, q3)
    circuit.cx(q[0], q[3])

    # CNOT(q1, q2)
    circuit.cx(q[1], q[2])

    # Rz on q2
    circuit.rz(2 * (math.pi / 2), q[2])

    # CNOT(q1, q2)
    circuit.cx(q[1], q[2])

    # CNOT(q2, q3)
    circuit.cx(q[2], q[3])

    # Rz on q3
    circuit.rz(2 * (math.pi / 2), q[3])

    # CNOT(q2, q3)
    circuit.cx(q[2], q[3])

    return circuit