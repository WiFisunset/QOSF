#!/usr/bin/env python
# coding: utf-8

# In[8]:


### Imports
from numpy import pi
import numpy as np

### Import Qiskit library tools
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit import Aer, execute, IBMQ
from qiskit.tools.visualization import plot_histogram, plot_state_city
get_ipython().run_line_magic('matplotlib', 'inline')
from qiskit.tools.monitor import job_monitor
from qiskit.providers.aer.noise import NoiseModel
from qiskit.test.mock import FakeVigo    

### TASK 2 Code for Open Quantum Source.
qreg_q = QuantumRegister(2, 'q')
creg_c = ClassicalRegister(2, 'c')
c = QuantumCircuit(qreg_q, creg_c)

# Use only CNOT's, Rx's, and Ry Gates.
c.rx(pi/2, qreg_q[0])
c.cx(qreg_q[0], qreg_q[1])
c.ry(pi/2, qreg_q[0])
c.rx(pi/2, qreg_q[1])
c.rx(pi/2, qreg_q[0])
c.ry(pi/2, qreg_q[1])
c.cx(qreg_q[0], qreg_q[1])
c.rx(pi/2, qreg_q[0])
c.ry(pi/2, qreg_q[1])
c.cx(qreg_q[0], qreg_q[1])
c.rx(pi/2, qreg_q[0])
c.ry(pi/2, qreg_q[1])
c.cx(qreg_q[0], qreg_q[1])
c.measure(qreg_q[0], creg_c[0])
c.measure(qreg_q[1], creg_c[1])

# Get the basis gates for the noise model
device_backend = FakeVigo()
coupling_map = device_backend.configuration().coupling_map

# Get the basis gates for the noise model
noise_model = NoiseModel.from_backend(device_backend)
basis_gates = noise_model.basis_gates

# Select the QasmSimulator from the Aer provider
simulator = Aer.get_backend('qasm_simulator')

###NOTE: I attempted to pass a variable to the shot count, but it gave an error each attempt, so 1000 shots were set.
# Execute noisy simulation and get counts
result_noise = execute(c, simulator,
                       noise_model=noise_model,
                       coupling_map=coupling_map,
                       basis_gates=basis_gates, shots=1000).result()
counts_noise = result_noise.get_counts(c)
plot_histogram(counts_noise, title="depolarizing noise model")

###NOTE: Visual of the Circuit; commented out since Jupyter Notebook will only show one graph per cell,
#     and I'm not sure what will be used to compile and run this program. Uncomment below to see the visual circuit diagram.
#style = {'backgroundcolor': 'lightgreen'}
#c.draw(output='mpl', style=style)

