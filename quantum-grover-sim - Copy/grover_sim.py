"""
grover_sim.py  –  Multiple-solution Grover demo  (Qiskit ≥ 1.0)

Produces:
    oscillations.png   — N = 256,  M = 1 / 4 / 16
    scaling.png        — M = 1,    N = 16 … 1024  (slope ≈ 1)
    circuit_demo.png   — 4-qubit, two-iteration Grover circuit diagram

Usage (inside your venv):
    pip install qiskit qiskit-aer matplotlib numpy pylatexenc
    python grover_sim.py
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# reproducibility
random.seed(42)
np.random.seed(42)

# ────────────────────────────────────────────────────────────────
# 1 ▸ Oracle & diffuser (ancilla = qubit n; diffuser on 0…n-1 only)
# ────────────────────────────────────────────────────────────────

def build_oracle(marked, n):
    qc = QuantumCircuit(n + 1)
    anc = n
    for state in marked:
        # flip zeros so that only |state⟩ → all-ones
        for q in range(n):
            if ((state >> q) & 1) == 0:
                qc.x(q)
        # MCZ via H–MCX–H on ancilla
        qc.h(anc)
        qc.mcx(list(range(n)), anc)
        qc.h(anc)
        # undo X flips
        for q in range(n):
            if ((state >> q) & 1) == 0:
                qc.x(q)
    return qc.to_gate(label="O")

def diffuser(n):
    qc = QuantumCircuit(n + 1)
    # H and X on index qubits only
    qc.h(range(n))
    qc.x(range(n))
    # multi-controlled Z on qubit n-1
    qc.h(n - 1)
    qc.mcx(list(range(n - 1)), n - 1)
    qc.h(n - 1)
    qc.x(range(n))
    qc.h(range(n))
    return qc.to_gate(label="D")

def grover_circuit(n, marked, k):
    qc = QuantumCircuit(n + 1, n)
    qc.x(n)              # ancilla into |1⟩
    qc.h(range(n))       # uniform superposition on data qubits
    O = build_oracle(marked, n)
    D = diffuser(n)
    for _ in range(k):
        qc.append(O, range(n + 1))
        qc.append(D, range(n + 1))
    qc.measure(range(n), range(n))
    return qc

# ────────────────────────────────────────────────────────────────
# 2 ▸ Execute & return empirical success probability
# ────────────────────────────────────────────────────────────────

backend = AerSimulator()

def run_grover(n, marked, k, shots=4096):
    tqc = transpile(grover_circuit(n, marked, k), backend)
    counts = backend.run(tqc, shots=shots).result().get_counts()
    # bitstrings are little-endian, so direct int(bitstr,2) works
    return sum(ct for bitstr, ct in counts.items()
               if int(bitstr, 2) in marked) / shots

# Quick print sanity check (expect ~0.96)
print("Sanity check N=16, M=1, k=3 →", run_grover(4, [3], 3))

# ────────────────────────────────────────────────────────────────
# 3 ▸ Plot A — oscillations (N = 256)
# ────────────────────────────────────────────────────────────────

def plot_oscillations():
    n = 8                # N = 256
    k_vals = range(17)
    plt.figure(figsize=(7,4))
    for M in [1, 4, 16]:
        marked = random.sample(range(2**n), M)
        probs = [run_grover(n, marked, k) for k in k_vals]
        plt.plot(k_vals, probs, marker='o', label=f"M = {M}")
    plt.xlabel("Grover iterations k")
    plt.ylabel("Success probability")
    plt.ylim(0,1.05)
    plt.title("Grover amplification (N = 256)")
    plt.legend()
    plt.tight_layout()
    plt.savefig("oscillations.png", dpi=300)
    plt.close()

# ────────────────────────────────────────────────────────────────
# 4 ▸ Plot B — scaling law (fixed M = 1)
# ────────────────────────────────────────────────────────────────

def plot_scaling():
    target = 0.95
    records = []
    for n in [4,6,8,10]:           # N = 16…1024
        marked = [random.randrange(2**n)]
        for k in range(1,40):
            if run_grover(n, marked, k) >= target:
                records.append((sqrt(2**n), k))
                break
    x, y = zip(*records)
    plt.figure(figsize=(5,4))
    plt.loglog(x, y, 'o', label="data")
    slope, intercept = np.polyfit(np.log10(x), np.log10(y), 1)
    fit_y = 10**intercept * np.array(x)**slope
    plt.loglog(x, fit_y, '--', label=f"slope ≈ {slope:.2f}")
    plt.xlabel(r"$\sqrt{N}$   (M = 1)")
    plt.ylabel("Iterations k (≥0.95 success)")
    plt.title("Grover scaling law")
    plt.legend()
    plt.tight_layout()
    plt.savefig("scaling.png", dpi=300)
    plt.close()

# ────────────────────────────────────────────────────────────────
# 5 ▸ Circuit diagram example
# ────────────────────────────────────────────────────────────────

def save_circuit_diagram():
    qc = grover_circuit(4, [3], k=2)
    # Capture the Figure object when drawing:
    fig = qc.draw(output="mpl", fold=-1, idle_wires=False)
    # Save *that* figure directly:
    fig.savefig("circuit_demo.png", dpi=300, bbox_inches="tight")
    # Close it so it doesn’t linger in memory:
    import matplotlib.pyplot as plt
    plt.close(fig)

# ────────────────────────────────────────────────────────────────
# 6 ▸ Main
# ────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("Running simulations …")
    plot_oscillations()
    plot_scaling()
    save_circuit_diagram()
    print("Done!  Images saved:")
    print("  • oscillations.png")
    print("  • scaling.png")
    print("  • circuit_demo.png")
