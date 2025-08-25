from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    q = QuantumRegister(4, 'q')
    # Create a quantum circuit acting on the q register
    qc = QuantumCircuit(q)

    # Apply Ry gate with theta=0 on q[0]
    qc.ry(0, q[0])
    # Apply H gate on q[1]
    qc.h(q[1])
    # Apply H gate on q[2]
    qc.h(q[2])
    # Apply U gate with theta=-0.677, phi=-pi/2, lambda=pi/2 on q[0]
    qc.u(-0.677, -3.14159/2, 3.14159/2, q[0])
    # Apply P gate with theta=2 on q[1]
    qc.p(2, q[1])
    # Apply P gate with theta=2 on q[2]
    qc.p(2, q[2])
    # Apply P gate with theta=pi/2 on q[0]
    qc.p(3.14159/2, q[0])
    # Apply CNOT gate with control q[1] and target q[0]
    qc.cx(q[1], q[0])
    # Apply Ry gate with theta=-0.677 on q[0]
    qc.ry(-0.677, q[0])
    # Apply CNOT gate with control q[1] and target q[0]
    qc.cx(q[1], q[0])
    # Apply Ry gate with theta=0.677 on q[0]
    qc.ry(0.677, q[0])
    # Apply P gate with theta=(3 * pi) / 2 on q[0]
    qc.p(3 * 3.14159 / 2, q[0])
    # Apply P gate with theta=pi/2 on q[0]
    qc.p(3.14159/2, q[0])
    # Apply CNOT gate with control q[2] and target q[0]
    qc.cx(q[2], q[0])
    # Apply Ry gate with theta=-1.33 on q[0]
    qc.ry(-1.33, q[0])
    # Apply CNOT gate with control q[2] and target q[0]
    qc.cx(q[2], q[0])
    # Apply Ry gate with theta=1.33 on q[0]
    qc.ry(1.33, q[0])
    # Apply P gate with theta=3*pi/2 on q[0]
    qc.p(3 * 3.14159 / 2, q[0])
    # Apply H gate on q[2]
    qc.h(q[2])
    # Apply RZ gate with theta=-pi/4 on q[2]
    qc.rz(-3.14159/4, q[2])
    # Apply CNOT gate with control q[1] and target q[2]
    qc.cx(q[1], q[2])
    # Apply RZ gate with theta=pi/4 on q[2]
    qc.rz(3.14159/4, q[2])
    # Apply CNOT gate with control q[1] and target q[2]
    qc.cx(q[1], q[2])
    # Apply RZ gate with theta=-pi/4 on q[1]
    qc.rz(-3.14159/4, q[1])
    # Apply H gate on q[1]
    qc.h(q[1])
    # Apply CNOT gate with control q[2] and target q[3]
    qc.cx(q[2], q[3])
    # Apply RY gate with theta=-0.694 on q[3]
    qc.ry(-0.694, q[3])
    # Apply CNOT gate with control q[1] and target q[3]
    qc.cx(q[1], q[3])
    # Apply RY gate with theta=-0.877 on q[3]
    qc.ry(-0.877, q[3])
    # Apply CNOT gate with control q[2] and target q[3]
    qc.cx(q[2], q[3])
    # Apply RY gate with theta=0.354 on q[3]
    qc.ry(0.354, q[3])
    # Apply CNOT gate with control q[1] and target q[3]
    qc.cx(q[1], q[3])
    # Apply RY gate with theta=1.22 on q[3]
    qc.ry(1.22, q[3])

    return qc