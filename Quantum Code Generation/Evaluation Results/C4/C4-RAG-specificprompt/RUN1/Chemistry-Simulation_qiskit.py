from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def ansatz() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    q3 = QuantumRegister(1, 'q3')
    circuit = QuantumCircuit(q0, q1, q2, q3)

    # InitialNode to Ry on q0
    circuit.ry(np.pi/2, q0[0])
    # Ry on q1
    circuit.ry(np.pi/2, q1[0])
    # Ry on q2
    circuit.ry(np.pi/2, q2[0])
    # Ry on q3
    circuit.ry(np.pi/2, q3[0])

    # Rz on q0
    circuit.rz(np.pi/2, q0[0])
    # Rz on q1
    circuit.rz(np.pi/2, q1[0])
    # Rz on q2
    circuit.rz(np.pi/2, q2[0])
    # Rz on q3
    circuit.rz(np.pi/2, q3[0])

    # CNOT gates
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])
    circuit.cx(q0[0], q1[0])
    circuit.cx(q1[0], q2[0])
    circuit.cx(q2[0], q3[0])

    # Final Ry and Rz gates
    circuit.ry(np.pi/2, q0[0])
    circuit.rz(np.pi/2, q0[0])
    circuit.ry(np.pi/2, q1[0])
    circuit.rz(np.pi/2, q1[0])
    circuit.ry(np.pi/2, q2[0])
    circuit.rz(np.pi/2, q2[0])
    circuit.ry(np.pi/2, q3[0])
    circuit.rz(np.pi/2, q3[0])

    return circuit