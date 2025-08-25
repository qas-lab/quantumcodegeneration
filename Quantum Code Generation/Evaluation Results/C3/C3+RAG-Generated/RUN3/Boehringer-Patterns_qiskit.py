from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def swap_test_quantum_circuit() -> QuantumCircuit:
    q = QuantumRegister(3, 'q')
    qc = QuantumCircuit(q)
    
    # Apply H gate to q[0]
    qc.h(q[0])
    
    # Apply CSWAP (controlled swap) between q[0] (control), q[1] and q[2]
    qc.cswap(q[0], q[1], q[2])
    
    # Apply H gate to q[0] again
    qc.h(q[0])
    
    return qc