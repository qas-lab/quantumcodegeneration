from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    qreg = QuantumRegister(4, 'q')
    qc = QuantumCircuit(qreg)

    # Apply gates as per the UML model
    qc.ry(0, qreg[0])  # Ry gate on q0 with theta=0
    qc.h(qreg[1])      # H gate on q1
    qc.h(qreg[2])      # H gate on q2
    qc.p(2, qreg[1])   # P gate on q1 with theta=2
    qc.p(2, qreg[2])   # P gate on q2 with theta=2
    qc.p(3.14159/2, qreg[0])  # P gate on q0 with theta=pi/2
    qc.cx(qreg[1], qreg[0])   # CNOT gate with control q1 and target q0
    qc.ry(-0.677, qreg[0])    # Ry gate on q0 with theta=-0.677
    qc.cx(qreg[1], qreg[0])   # CNOT gate with control q1 and target q0
    qc.ry(0.677, qreg[0])     # Ry gate on q0 with theta=0.677
    qc.p(3*3.14159/2, qreg[0])  # P gate on q0 with theta=(3*pi)/2
    qc.p(3.14159/2, qreg[0])  # P gate on q0 with theta=pi/2
    qc.cx(qreg[2], qreg[0])   # CNOT gate with control q2 and target q0
    qc.ry(-1.33, qreg[0])     # Ry gate on q0 with theta=-1.33
    qc.cx(qreg[2], qreg[0])   # CNOT gate with control q2 and target q0
    qc.ry(1.33, qreg[0])      # Ry gate on q0 with theta=1.33
    qc.p(3*3.14159/2, qreg[0])  # P gate on q0 with theta=3*pi/2
    qc.h(qreg[2])             # H gate on q2
    qc.rz(-3.14159/4, qreg[2])  # RZ gate on q2 with theta=-pi/4
    qc.cx(qreg[1], qreg[2])   # CNOT gate with control q1 and target q2
    qc.rz(3.14159/4, qreg[2])  # RZ gate on q2 with theta=pi/4
    qc.cx(qreg[1], qreg[2])   # CNOT gate with control q1 and target q2
    qc.h(qreg[1])             # H gate on q1
    qc.cx(qreg[2], qreg[3])   # CNOT gate with control q2 and target q3
    qc.ry(-0.694, qreg[3])    # Ry gate on q3 with theta=-0.694
    qc.cx(qreg[1], qreg[3])   # CNOT gate with control q1 and target q3
    qc.ry(-0.877, qreg[3])    # Ry gate on q3 with theta=-0.877
    qc.cx(qreg[2], qreg[3])   # CNOT gate with control q2 and target q3
    qc.ry(0.354, qreg[3])     # Ry gate on q3 with theta=0.354
    qc.cx(qreg[1], qreg[3])   # CNOT gate with control q1 and target q3
    qc.ry(1.22, qreg[3])      # Ry gate on q3 with theta=1.22

    return qc