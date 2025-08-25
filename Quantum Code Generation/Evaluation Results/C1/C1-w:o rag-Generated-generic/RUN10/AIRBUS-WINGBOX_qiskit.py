from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    q = QuantumRegister(4, 'q')
    qc = QuantumCircuit(q)

    # Apply gates as per the UML model
    qc.ry(0, q[0])  # Ry gate on q0 with theta=0
    qc.h(q[1])      # H gate on q1
    qc.h(q[2])      # H gate on q2
    qc.u(-0.677, -3.14159/2, 3.14159/2, q[0])  # U gate on q0
    qc.p(2, q[1])   # P gate on q1
    qc.p(2, q[2])   # P gate on q2
    qc.p(3.14159/2, q[0])  # P gate on q0
    qc.cx(q[1], q[0])  # CNOT gate with q1 as control and q0 as target
    qc.ry(-0.677, q[0])  # Ry gate on q0
    qc.cx(q[1], q[0])  # CNOT gate with q1 as control and q0 as target
    qc.ry(0.677, q[0])  # Ry gate on q0
    qc.p(3*3.14159/2, q[0])  # P gate on q0
    qc.p(3.14159/2, q[0])  # P gate on q0
    qc.cx(q[2], q[0])  # CNOT gate with q2 as control and q0 as target
    qc.ry(-1.33, q[0])  # Ry gate on q0
    qc.cx(q[2], q[0])  # CNOT gate with q2 as control and q0 as target
    qc.ry(1.33, q[0])  # Ry gate on q0
    qc.p(3*3.14159/2, q[0])  # P gate on q0
    qc.h(q[2])  # H gate on q2
    qc.rz(-3.14159/4, q[2])  # RZ gate on q2
    qc.cx(q[1], q[2])  # CNOT gate with q1 as control and q2 as target
    qc.rz(3.14159/4, q[2])  # RZ gate on q2
    qc.cx(q[1], q[2])  # CNOT gate with q1 as control and q2 as target
    qc.rz(-3.14159/4, q[1])  # RZ gate on q1
    qc.h(q[1])  # H gate on q1
    qc.cx(q[2], q[3])  # CNOT gate with q2 as control and q3 as target
    qc.ry(-0.694, q[3])  # Ry gate on q3
    qc.cx(q[1], q[3])  # CNOT gate with q1 as control and q3 as target
    qc.ry(-0.877, q[3])  # Ry gate on q3
    qc.cx(q[2], q[3])  # CNOT gate with q2 as control and q3 as target
    qc.ry(0.354, q[3])  # Ry gate on q3
    qc.cx(q[1], q[3])  # CNOT gate with q1 as control and q3 as target
    qc.ry(1.22, q[3])  # Ry gate on q3

    return qc