from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    q = QuantumRegister(4, 'q')
    qc = QuantumCircuit(q)

    # Apply gates as per the UML model
    qc.ry(0, q[0])  # Ry gate with theta=0 on q0
    qc.h(q[1])      # H gate on q1
    qc.h(q[2])      # H gate on q2
    qc.p(2, q[1])   # P gate with theta=2 on q1
    qc.p(2, q[2])   # P gate with theta=2 on q2
    qc.p(3.14159/2, q[0])  # P gate with theta=pi/2 on q0
    qc.cx(q[1], q[0])  # CNOT gate from q1 to q0
    qc.ry(-0.677, q[0])  # Ry gate with theta=-0.677 on q0
    qc.cx(q[1], q[0])  # CNOT gate from q1 to q0
    qc.ry(0.677, q[0])  # Ry gate with theta=0.677 on q0
    qc.p(3*3.14159/2, q[0])  # P gate with theta=3*pi/2 on q0
    qc.p(3.14159/2, q[0])  # P gate with theta=pi/2 on q0
    qc.cx(q[2], q[0])  # CNOT gate from q2 to q0
    qc.ry(-1.33, q[0])  # Ry gate with theta=-1.33 on q0
    qc.cx(q[2], q[0])  # CNOT gate from q2 to q0
    qc.ry(1.33, q[0])  # Ry gate with theta=1.33 on q0
    qc.p(3*3.14159/2, q[0])  # P gate with theta=3*pi/2 on q0
    qc.h(q[2])  # H gate on q2
    qc.rz(-3.14159/4, q[2])  # RZ gate with theta=-pi/4 on q2
    qc.cx(q[1], q[2])  # CNOT gate from q1 to q2
    qc.rz(3.14159/4, q[2])  # RZ gate with theta=pi/4 on q2
    qc.cx(q[1], q[2])  # CNOT gate from q1 to q2
    qc.h(q[1])  # H gate on q1
    qc.cx(q[2], q[3])  # CNOT gate from q2 to q3
    qc.ry(-0.694, q[3])  # Ry gate with theta=-0.694 on q3
    qc.cx(q[1], q[3])  # CNOT gate from q1 to q3
    qc.ry(-0.877, q[3])  # Ry gate with theta=-0.877 on q3
    qc.cx(q[2], q[3])  # CNOT gate from q2 to q3
    qc.ry(0.354, q[3])  # Ry gate with theta=0.354 on q3
    qc.cx(q[1], q[3])  # CNOT gate from q1 to q3
    qc.ry(1.22, q[3])  # Ry gate with theta=1.22 on q3

    return qc