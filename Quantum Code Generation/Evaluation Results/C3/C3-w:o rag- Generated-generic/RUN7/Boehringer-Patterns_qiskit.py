from qiskit import QuantumCircuit, QuantumRegister
from numpy import pi

def swap_test_quantum_circuit() -> QuantumCircuit:
    q = QuantumRegister(3, 'q')
    qc = QuantumCircuit(q)
    
    # Apply H gate to q[0]
    qc.h(q[0])
    
    # Apply CSWAP (controlled swap) with q[0] as control, q[1] and q[2] as targets
    qc.cswap(q[0], q[1], q[2])
    
    # Apply H gate to q[0] again
    qc.h(q[0])
    
    return qc