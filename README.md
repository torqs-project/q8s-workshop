# Qubernetes workshop

## Introduction

This workshop is designed to help you get started with Qiskit and Qubernetes. Qiskit is an open-source quantum computing software development framework for leveraging today's quantum processors in research, education, and business. Qubernetes is a Kubernetes distribution specialized for running quantum circuits on quantum GPU-accelerated simulators and computers.

## Pre-requisites

The following tools are required to complete the workshop:

- [Docker](https://docs.docker.com/get-docker/)
- [Python 3](https://www.python.org/downloads/)

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install python dependencies:

```bash
pip install -r requirements.txt
```

## Challenges

### Challenge 1 - Execute GPU accelerated quantum job

The default image used in Qubernetes has the following python dependencies installed:

- qiskit
- qiskit-aer-gpu

Modify the `main.py` file and submit it to the cluster using `q8sctl`.

### Challenge 2 - Execute quantum job with custom image

If the default image does not have the required dependencies or you want to use other quantum development kits than Qiskit (e.g. Pennylane), you can build a custom image and use it to run the quantum job.

Modify the `Dockerfile`, `requirements.txt` and `main.py` files and submit the job to the cluster using `q8sctl`.

### Challenge 3 - Execute quantum job on a remote QPU

Qubernetes supports running quantum jobs on remote quantum processing units (curently IQM Adonis 5-qubit), using the custom Qiskit backend described in `main.py`.

You need to create a custom image using the provided `Dockerfile` template. You can use the `q8sctl` command to submit a job to a remote QPU.
