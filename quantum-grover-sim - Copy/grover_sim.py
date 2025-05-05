# grover_sim.py  –  Monte Carlo Grover demo with optimized scaling search (Qiskit ≥ 1.0)
#
# Produces:
#   oscillations.png        — N = 256,  M = 1 / 4 / 16
#   scaling.png             — M = 1,    N = 16 … 1024  (log–log)
#   scaling_M1.png          — M = 1,    N = 16 … 16384 (log–log)
#   scaling_M4.png          — M = 4,    N = 16 … 16384 (log–log)
#   scaling_M16.png         — M = 16,   N = 16 … 16384 (log–log)
#   circuit_demo.png        — 4-qubit, two-iteration circuit diagram
#   unknown_M_summary.png   — bar chart of unknown-M vs. random
#
# Usage (inside your venv):
#     pip install qiskit qiskit-aer matplotlib numpy
#     python grover_sim.py

import random
import math
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

# reproducibility
random.seed(42)
np.random.seed(42)

# 1 ▸ Oracle & diffuser (unchanged)
def build_oracle(marked, n):
    qc = QuantumCircuit(n+1)
    anc = n
    for state in marked:
        for q in range(n):
            if ((state >> q) & 1) == 0:
                qc.x(q)
        qc.h(anc)
        qc.mcx(list(range(n)), anc)
        qc.h(anc)
        for q in range(n):
            if ((state >> q) & 1) == 0:
                qc.x(q)
    return qc.to_gate(label="O")

def diffuser(n):
    qc = QuantumCircuit(n+1)
    qc.h(range(n)); qc.x(range(n))
    qc.h(n-1); qc.mcx(list(range(n-1)), n-1); qc.h(n-1)
    qc.x(range(n)); qc.h(range(n))
    return qc.to_gate(label="D")

def grover_circuit(n, marked, k):
    qc = QuantumCircuit(n+1, n)
    qc.x(n); qc.h(range(n))
    O, D = build_oracle(marked, n), diffuser(n)
    for _ in range(k):
        qc.append(O, range(n+1))
        qc.append(D, range(n+1))
    qc.measure(range(n), range(n))
    return qc

# 2 ▸ Execution helper
backend = AerSimulator()
def run_grover_prob(n, marked, k, shots=4096):
    qc = grover_circuit(n, marked, k)
    tqc = transpile(qc, backend)
    counts = backend.run(tqc, shots=shots).result().get_counts()
    return sum(ct for b, ct in counts.items() if int(b,2) in marked)/shots

# 3 ▸ Unknown-M search (unchanged)
def search_grover_unknown_M(n, marked, threshold=0.95, shots=4096):
    M, N = len(marked), 2**n
    k_bound = math.ceil((math.pi/4)*math.sqrt(N/M))*2 + 5
    for k in range(1, k_bound+1):
        if run_grover_prob(n, marked, k, shots) >= threshold:
            return k, None
    return None, None

# 4 ▸ Plot A — oscillations (unchanged)
def plot_oscillations():
    n, shots = 8, 4096
    plt.figure(figsize=(7,4))
    for M in [1,4,16]:
        marked = random.sample(range(2**n), M)
        probs = [run_grover_prob(n, marked, k, shots) for k in range(17)]
        plt.plot(range(17), probs, 'o-', label=f"M = {M}")
    plt.xlabel("Grover iterations k")
    plt.ylabel("Success probability")
    plt.title("Grover amplification (N=256)")
    plt.ylim(0,1.05); plt.legend()
    plt.tight_layout(); plt.savefig("oscillations.png", dpi=300); plt.close()

# 5 ▸ Plot B — optimized scaling (M = 1)
def plot_scaling():
    shots = 16384
    records = []
    for n in range(4, 11):
        N = 2**n
        marked = [0]  # deterministic
        k0 = math.ceil((math.pi/4)*math.sqrt(N))
        candidates = [max(1, k0-1), k0, k0+1]
        best = max(candidates, key=lambda k: run_grover_prob(n, marked, k, shots))
        records.append((sqrt(N), best))
    x,y = zip(*records)
    slope, intercept = np.polyfit(np.log10(x), np.log10(y),1)
    fit = 10**intercept * np.array(x)**slope
    plt.figure(figsize=(5,4))
    plt.loglog(x,y,'o',label="data")
    plt.loglog(x,fit,'--',label=f"slope≈{slope:.2f}")
    plt.xlabel(r"$\sqrt{N}$ (log)"); plt.ylabel(r"$k_{\rm opt}$ (log)")
    plt.title("Optimized Grover scaling (M=1)")
    plt.grid(True, which='both', ls='--'); plt.legend()
    plt.tight_layout(); plt.savefig("scaling.png",dpi=300); plt.close()

# 6 ▸ Plot C — optimized scaling for fixed M
def plot_scaling_fixed_M(M):
    shots = 16384
    records = []
    for n in range(4, 15):
        N = 2**n
        marked = list(range(M))
        k0 = math.ceil((math.pi/4)*math.sqrt(N/M))
        candidates = [max(1, k0-1), k0, k0+1]
        best = max(candidates, key=lambda k: run_grover_prob(n, marked, k, shots))
        records.append((sqrt(N/M), best))
    x,y = zip(*records)
    slope, intercept = np.polyfit(np.log10(x), np.log10(y),1)
    fit = 10**intercept * np.array(x)**slope
    plt.figure(figsize=(5,4))
    plt.loglog(x,y,'o',label="data")
    plt.loglog(x,fit,'--',label=f"slope≈{slope:.2f}")
    plt.xlabel(r"$\sqrt{N/M}$ (log)"); plt.ylabel(r"$k_{\rm opt}$ (log)")
    plt.title(f"Optimized Grover scaling (M={M})")
    plt.grid(True, which='both', ls='--'); plt.legend()
    plt.tight_layout(); plt.savefig(f"scaling_M{M}.png",dpi=300); plt.close()

# 7 ▸ Circuit diagram example
def save_circuit_diagram():
    qc = grover_circuit(4, [3], k=2)
    fig = qc.draw(output="mpl", fold=-1, idle_wires=False)
    fig.savefig("circuit_demo.png", dpi=300, bbox_inches="tight"); plt.close()

# 8 ▸ Plot D — unknown-M summary (unchanged)
def plot_unknown_M_summary():
    n, shots = 8, 4096
    N=2**n; results=[]
    for M in [1,4,16]:
        marked = list(range(M))
        k,_ = search_grover_unknown_M(n, marked, shots=shots)
        if k:
            prob = run_grover_prob(n, marked, k, shots)
            results.append((M,k,prob))
    Ms, ks, ps = zip(*results)
    rand=[M/N for M in Ms]
    x=np.arange(len(Ms))
    fig,ax=plt.subplots(figsize=(6,4))
    ax.bar(x-0.15, ps, 0.3, label="Grover")
    ax.bar(x+0.15, rand, 0.3, label="Random", alpha=0.6)
    for i,k in enumerate(ks):
        ax.text(x[i], ps[i]+0.02, f"k={k}", ha="center")
    ax.set_xticks(x); ax.set_xticklabels([f"M={M}" for M in Ms])
    ax.set_ylim(0,1.1)
    ax.set_ylabel("Success probability")
    ax.set_title("Unknown-M Grover vs. Random")
    ax.legend()
    plt.tight_layout(); plt.savefig("unknown_M_summary.png", dpi=300); plt.close()

# 9 ▸ Main
if __name__ == "__main__":
    plot_oscillations()
    plot_scaling()
    for M in [1,4,16]:
        plot_scaling_fixed_M(M)
    save_circuit_diagram()
    plot_unknown_M_summary()
