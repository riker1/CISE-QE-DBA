# QE-DBA (Query-Efficient Bayesian Optimization Decision Based Adversarial Attacks)

QE-DBA is a research project that explores query-efficient decision-based adversarial attacks using Bayesian Optimization. The goal is to generate adversarial examples that cause a classifier to misclassify an image while minimizing the perceptual difference between the original and perturbed images.

## Overview

This repository contains:

- Bayesian Optimization Decision-Based Attack (BO-DBA) implementation
- Evaluation notebooks and experiments
- ImageNet validation dataset preprocessing tools
- Comparative evaluation against alternative adversarial attack methods
- A Docker-based runtime environment for reproducing experiments

---

## Recommended Setup (Docker)

The easiest and most reliable way to run this project is with Docker.

The original project dependencies are several years old and can be difficult to install on modern operating systems. A Docker image is provided to create a reproducible environment.

### Prerequisites

Install one of the following:

- Docker Desktop (Windows/macOS)
- Docker Engine (Linux)

#### Get Docker:

- https://docs.docker.com/get-started/introduction/get-docker-desktop/

Verify Docker is working:

```bash
docker --version
```

---

## Build the Container

Clone the repository:

```bash
git clone <repository-url>
cd CISE-QE-DBA
```

Build the image:

```bash
docker buildx build \
  --platform linux/amd64 \
  -t cise-qe-dba-old .
```

The build may take several minutes the first time.

---

## Run the Environment

Start the container and launch Jupyter Notebook:

```bash
docker run \
  --platform linux/amd64 \
  --rm \
  -it \
  -p 8888:8888 \
  -v "$PWD:/workspace" \
  -w /workspace \
  cise-qe-dba-old
```

Once the container starts, Jupyter Notebook will automatically launch.

Open your browser and navigate to:

```text
http://localhost:8888/tree
```

No authentication token is required.

---

## Running the Demo

After Jupyter loads:

1. Open `Demo.ipynb`
2. Execute notebook cells sequentially
3. Experiment with configuration settings and attack parameters
4. Review generated adversarial examples and evaluation metrics

---

## Dataset Preparation

Download the ImageNet validation dataset:

https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5

Place the archive in:

```text
DataSet/
```

Then preprocess the dataset:

```bash
cd DataSet
python preprocess_imagenet_validation_data.py
```

---

## Configuration

Classifier settings are controlled through:

```text
Configuration.yaml
```

Supported models include:

- Inception
- ResNet

Additional configuration examples are available in:

```text
Demo.ipynb
```

---

## Evaluation Experiments

Additional evaluation notebooks can be found under:

```text
Evaluation/
```

These notebooks compare BO-DBA against other adversarial attack approaches and provide performance measurements.

---

## Authors

- Prashant Jadiya
- Zhensheng Sun
- Nathan McDermott

Docker modernization and dependency restoration by contributors to this repository.