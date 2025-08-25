from qiskit import QuantumCircuit, QuantumRegister


def circuit1():
    # Create a quantum register with 4 qubits
    qreg = QuantumRegister(4, 'q')
    # Create a quantum circuit acting on the qreg register
    circuit = QuantumCircuit(qreg)

    # Apply gates as per the UML model
    circuit.ry(0, qreg[0])
    circuit.h(qreg[1])
    circuit.h(qreg[2])
    circuit.p(2, qreg[1])
    circuit.p(2, qreg[2])
    circuit.p(3.14159/2, qreg[0])
    circuit.cx(qreg[1], qreg[0])
    circuit.ry(-0.677, qreg[0])
    circuit.cx(qreg[1], qreg[0])
    circuit.ry(0.677, qreg[0])
    circuit.p(3 * 3.14159 / 2, qreg[0])
    circuit.p(3.14159/2, qreg[0])
    circuit.cx(qreg[2], qreg[0])
    circuit.ry(-1.33, qreg[0])
    circuit.cx(qreg[2], qreg[0])
    circuit.ry(1.33, qreg[0])
    circuit.p(3 * 3.14159 / 2, qreg[0])
    circuit.h(qreg[2])
    circuit.rz(-3.14159/4, qreg[2])
    circuit.cx(qreg[1], qreg[2])
    circuit.rz(3.14159/4, qreg[2])
    circuit.cx(qreg[1], qreg[2])
    circuit.h(qreg[1])
    circuit.cx(qreg[2], qreg[3])
    circuit.ry(-0.694, qreg[3])
    circuit.cx(qreg[1], qreg[3])
    circuit.ry(-0.877, qreg[3])
    circuit.cx(qreg[2], qreg[3])
    circuit.ry(0.354, qreg[3])
    circuit.cx(qreg[1], qreg[3])
    circuit.ry(1.22, qreg[3])

    return circuit