from qiskit import QuantumCircuit, QuantumRegister
import numpy as np

def swap_test_quantum_circuit() -> QuantumCircuit:
    qreg = QuantumRegister(3, 'q')
    qc = QuantumCircuit(qreg)
    
    # Apply H gate to q[0]
    qc.h(qreg[0])
    
    # Apply CSWAP gate with q[0] as control and q[1], q[2] as targets
    qc.cswap(qreg[0], qreg[1], qreg[2])
    
    # Apply H gate to q[0] again
    qc.h(qreg[0])
    
    return qc