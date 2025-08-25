from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    q = QuantumRegister(4, 'q')
    qc = QuantumCircuit(q)

    # Apply gates as per the UML model
    qc.ry(0, q[0])  # Ry gate on q0 with theta=0
    qc.h(q[1])      # H gate on q1
    qc.h(q[2])      # H gate on q2
    qc.p(2, q[1])   # P gate on q1 with theta=2
    qc.p(2, q[2])   # P gate on q2 with theta=2
    qc.p(3.14159/2, q[0])  # P gate on q0 with theta=pi/2
    qc.cx(q[1], q[0])  # CNOT gate with q1 as control and q0 as target
    qc.ry(-0.677, q[0])  # Ry gate on q0 with theta=-0.677
    qc.cx(q[1], q[0])  # CNOT gate with q1 as control and q0 as target
    qc.ry(0.677, q[0])  # Ry gate on q0 with theta=0.677
    qc.p(3*3.14159/2, q[0])  # P gate on q0 with theta=(3*pi)/2
    qc.p(3.14159/2, q[0])  # P gate on q0 with theta=pi/2
    qc.cx(q[2], q[0])  # CNOT gate with q2 as control and q0 as target
    qc.ry(-1.33, q[0])  # Ry gate on q0 with theta=-1.33
    qc.cx(q[2], q[0])  # CNOT gate with q2 as control and q0 as target
    qc.ry(1.33, q[0])  # Ry gate on q0 with theta=1.33
    qc.p(3*3.14159/2, q[0])  # P gate on q0 with theta=3*pi/2
    qc.h(q[2])  # H gate on q2
    qc.rz(-3.14159/4, q[2])  # RZ gate on q2 with theta=-pi/4
    qc.cx(q[1], q[2])  # CNOT gate with q1 as control and q2 as target
    qc.rz(3.14159/4, q[2])  # RZ gate on q2 with theta=pi/4
    qc.cx(q[1], q[2])  # CNOT gate with q1 as control and q2 as target
    qc.h(q[1])  # H gate on q1
    qc.cx(q[2], q[3])  # CNOT gate with q2 as control and q3 as target
    qc.ry(-0.694, q[3])  # Ry gate on q3 with theta=-0.694
    qc.cx(q[1], q[3])  # CNOT gate with q1 as control and q3 as target
    qc.ry(-0.877, q[3])  # Ry gate on q3 with theta=-0.877
    qc.cx(q[2], q[3])  # CNOT gate with q2 as control and q3 as target
    qc.ry(0.354, q[3])  # Ry gate on q3 with theta=0.354
    qc.cx(q[1], q[3])  # CNOT gate with q1 as control and q3 as target
    qc.ry(1.22, q[3])  # Ry gate on q3 with theta=1.22

    return qc