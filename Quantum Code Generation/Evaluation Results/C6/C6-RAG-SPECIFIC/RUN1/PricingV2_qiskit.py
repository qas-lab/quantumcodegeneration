from qiskit import QuantumCircuit, QuantumRegister

def europeanCallQuantumCircuit() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    europeanCallQuantumCircuit = QuantumCircuit(q0, q1, q2)

    # Ry gates
    europeanCallQuantumCircuit.ry(1.43, q0)
    europeanCallQuantumCircuit.ry(2.9, q1)
    europeanCallQuantumCircuit.cx(q0, q1)  # CNOT(q0-q1)
    europeanCallQuantumCircuit.ry(1.10, q0)
    europeanCallQuantumCircuit.ry(-0.93, q1)
    europeanCallQuantumCircuit.ry(1.47, q2)
    europeanCallQuantumCircuit.cx(q0, q2)  # CNOT(q0-q2)
    europeanCallQuantumCircuit.ry(-0.10, q2)
    europeanCallQuantumCircuit.cx(q1, q2)  # CNOT(q1-q2)
    europeanCallQuantumCircuit.ry(0.10, q2)
    europeanCallQuantumCircuit.cx(q0, q2)  # CNOT(q0-q2)
    europeanCallQuantumCircuit.ry(-0.29, q2)
    europeanCallQuantumCircuit.cx(q1, q2)  # CNOT(q1-q2)

    return europeanCallQuantumCircuit