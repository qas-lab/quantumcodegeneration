from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    q = QuantumRegister(4, 'q')
    # Create a quantum circuit acting on the q register
    qc = QuantumCircuit(q)

    # Apply gates as per the UML model
    qc.ry(0, q[0])
    qc.h(q[1])
    qc.h(q[2])
    qc.u(-0.677, -3.14159/2, 3.14159/2, q[0])
    qc.p(2, q[1])
    qc.p(2, q[2])
    qc.p(3.14159/2, q[0])
    qc.cx(q[1], q[0])
    qc.ry(-0.677, q[0])
    qc.cx(q[1], q[0])
    qc.ry(0.677, q[0])
    qc.p((3 * 3.14159) / 2, q[0])
    qc.p(3.14159/2, q[0])
    qc.cx(q[2], q[0])
    qc.ry(-1.33, q[0])
    qc.cx(q[2], q[0])
    qc.ry(1.33, q[0])
    qc.p(3*3.14159/2, q[0])
    qc.h(q[2])
    qc.rz(-3.14159/4, q[2])
    qc.cx(q[1], q[2])
    qc.rz(3.14159/4, q[2])
    qc.cx(q[1], q[2])
    qc.rz(-3.14159/4, q[1])
    qc.h(q[1])
    qc.cx(q[2], q[3])
    qc.ry(-0.694, q[3])
    qc.cx(q[1], q[3])
    qc.ry(-0.877, q[3])
    qc.cx(q[2], q[3])
    qc.ry(0.354, q[3])
    qc.cx(q[1], q[3])
    qc.ry(1.22, q[3])

    return qc