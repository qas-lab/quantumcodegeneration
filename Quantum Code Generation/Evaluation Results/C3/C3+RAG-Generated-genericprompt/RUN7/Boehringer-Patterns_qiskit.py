from qiskit import QuantumCircuit

def swap_test_quantum_circuit():
    # Create a quantum circuit with 3 qubits
    qc = QuantumCircuit(3, 1)

    # Apply a Hadamard gate on the first qubit (q0)
    qc.h(0)

    # Apply a controlled-SWAP (Fredkin) gate with q0 as control and q1, q2 as targets
    qc.cswap(0, 1, 2)

    # Apply another Hadamard gate on the first qubit (q0)
    qc.h(0)

    # Measure the first qubit
    qc.measure(0, 0)

    return qc