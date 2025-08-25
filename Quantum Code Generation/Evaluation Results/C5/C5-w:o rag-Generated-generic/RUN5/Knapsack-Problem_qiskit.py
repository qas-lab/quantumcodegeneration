from qiskit import QuantumCircuit
from qiskit.circuit.library import U3Gate, RZGate

def QAOAcircuit():
    qc = QuantumCircuit(4)
    # Apply U3 gates
    qc.append(U3Gate(0, 3.141592653589793, 0), [0])
    qc.append(U3Gate(0, 3.141592653589793, 0), [1])
    qc.append(U3Gate(0, 3.141592653589793, 0), [2])
    qc.append(U3Gate(0, 3.141592653589793, 0), [3])
    # Apply CNOT gates
    qc.cx(0, 1)
    qc.rz(3.141592653589793, 1)
    qc.cx(0, 1)
    qc.cx(0, 3)
    qc.rz(3.141592653589793, 3)
    qc.cx(0, 3)
    qc.cx(1, 2)
    qc.rz(3.141592653589793, 2)
    qc.cx(1, 2)
    qc.cx(2, 3)
    qc.rz(3.141592653589793, 3)
    qc.cx(2, 3)
    return qc