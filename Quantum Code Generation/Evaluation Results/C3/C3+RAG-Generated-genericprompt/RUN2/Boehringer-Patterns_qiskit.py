from qiskit import QuantumCircuit

def swap_test_quantum_circuit():
    # Create a quantum circuit with 3 qubits
    qc = QuantumCircuit(3)

    # Apply a Hadamard gate on qubit 0
    qc.h(0)

    # Apply a controlled-SWAP (Fredkin) gate with qubit 0 as control and qubits 1 and 2 as targets
    qc.cswap(0, 1, 2)

    # Apply another Hadamard gate on qubit 0
    qc.h(0)

    return qc