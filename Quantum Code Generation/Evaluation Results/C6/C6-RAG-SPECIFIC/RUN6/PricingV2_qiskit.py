from qiskit import QuantumCircuit, QuantumRegister

def europeanCallQuantumCircuit() -> QuantumCircuit:
    q0 = QuantumRegister(1, 'q0')
    q1 = QuantumRegister(1, 'q1')
    q2 = QuantumRegister(1, 'q2')
    europeanCallQuantumCircuit = QuantumCircuit(q0, q1, q2)

    # Apply Ry gates with specified theta values
    europeanCallQuantumCircuit.ry(1.43, q0[0])
    europeanCallQuantumCircuit.ry(2.9, q1[0])
    europeanCallQuantumCircuit.cx(q0[0], q1[0])
    europeanCallQuantumCircuit.ry(1.10, q0[0])
    europeanCallQuantumCircuit.ry(-0.93, q1[0])
    europeanCallQuantumCircuit.ry(1.47, q2[0])
    europeanCallQuantumCircuit.cx(q0[0], q2[0])
    europeanCallQuantumCircuit.ry(-0.10, q2[0])
    europeanCallQuantumCircuit.ry(0.10, q2[0])
    europeanCallQuantumCircuit.cx(q1[0], q2[0])
    europeanCallQuantumCircuit.ry(-0.29, q2[0])
    europeanCallQuantumCircuit.cx(q0[0], q2[0])
    europeanCallQuantumCircuit.cx(q1[0], q2[0])

    return europeanCallQuantumCircuit