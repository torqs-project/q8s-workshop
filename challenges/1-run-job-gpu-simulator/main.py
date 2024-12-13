from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer, AerSimulator


def demo_function(shotsAmount=1000):
    simulator = AerSimulator(method="statevector", device="GPU")

    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    circuit.measure([0, 1], [0, 1])

    compiled_circuit = transpile(circuit, simulator)
    job = simulator.run(compiled_circuit, shots=shotsAmount)
    result = job.result()
    counts = result.get_counts()

    print("Total count for 00 and 11 are:", counts)
    print(circuit)
    return counts


result = demo_function(4000)
