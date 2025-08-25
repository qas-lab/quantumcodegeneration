from qiskit import QuantumCircuit
import math

def ansatz():
    qc = QuantumCircuit(4)
    # Initial Ry and Rz rotations
    qc.ry(math.pi/2, 0)
    qc.ry(math.pi/2, 1)
    qc.ry(math.pi/2, 2)
    qc.ry(math.pi/2, 3)
    qc.rz(math.pi/2, 0)
    qc.rz(math.pi/2, 1)
    qc.rz(math.pi/2, 2)
    qc.rz(math.pi/2, 3)
    # First layer of CNOTs
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    # Second layer of Ry and Rz rotations
    qc.ry(math.pi/2, 0)
    qc.ry(math.pi/2, 1)
    qc.ry(math.pi/2, 2)
    qc.ry(math.pi/2, 3)
    qc.rz(math.pi/2, 0)
    qc.rz(math.pi/2, 1)
    qc.rz(math.pi/2, 2)
    qc.rz(math.pi/2, 3)
    # Second layer of CNOTs
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    # Third layer of Ry and Rz rotations
    qc.ry(math.pi/2, 0)
    qc.ry(math.pi/2, 1)
    qc.ry(math.pi/2, 2)
    qc.ry(math.pi/2, 3)
    qc.rz(math.pi/2, 0)
    qc.rz(math.pi/2, 1)
    qc.rz(math.pi/2, 2)
    qc.rz(math.pi/2, 3)
    # Third layer of CNOTs
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.cx(2, 3)
    # Final layer of Ry and Rz rotations
    qc.ry(math.pi/2, 0)
    qc.ry(math.pi/2, 1)
    qc.ry(math.pi/2, 2)
    qc.ry(math.pi/2, 3)
    qc.rz(math.pi/2, 0)
    qc.rz(math.pi/2, 1)
    qc.rz(math.pi/2, 2)
    qc.rz(math.pi/2, 3)
    return qc