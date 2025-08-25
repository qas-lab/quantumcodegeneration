from qiskit import QuantumCircuit

def swap_test_quantum_circuit():
    # Create a quantum circuit with 3 qubits
    qc = QuantumCircuit(3)
    
    # Apply Hadamard gate to the first qubit (q0)
    qc.h(0)
    
    # Apply controlled-SWAP (Fredkin) gate with q0 as control and q1, q2 as targets
    qc.cswap(0, 1, 2)
    
    # Apply Hadamard gate to the first qubit (q0) again
    qc.h(0)
    
    return qc