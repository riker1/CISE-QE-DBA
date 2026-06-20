# QE-DBA (Query-Efficient Bayesian Optimization Decision Based Adversarial Attacks)

QE-DBA is a research project that explores query-efficient decision-based adversarial attacks using Bayesian Optimization. The goal is to generate adversarial examples that cause a classifier to misclassify an image while minimizing the perceptual difference between the original and perturbed images.

---

## Overview

This repository contains:

- Bayesian Optimization Decision-Based Attack (BO-DBA) implementation
- Evaluation notebooks and experiments
- ImageNet validation dataset preprocessing tools
- Comparative evaluation against alternative adversarial attack methods
- A Docker-based runtime environment for reproducing experiments

---

## Quick Start

The fastest way to get started is with Docker.

```bash
git clone https://github.com/riker1/CISE-QE-DBA
cd CISE-QE-DBA

docker buildx build \
  --platform linux/amd64 \
  -t cise-qe-dba-old .

docker run \
  --platform linux/amd64 \
  --rm \
  -it \
  -p 8888:8888 \
  -v "$PWD:/workspace" \
  -w /workspace \
  cise-qe-dba-old
```

Then open:

```text
http://localhost:8888/tree
```

and launch:

```text
Demo.ipynb
```

---

## Recommended Setup (Docker)

The easiest and most reliable way to run this project is with Docker.

The original project dependencies are several years old and can be difficult to install on modern operating systems. The provided Docker image recreates a compatible environment and eliminates the need to manually resolve legacy TensorFlow, OpenCV, GPy, and scientific computing dependencies.

### Why Docker?

This project was originally developed using a machine learning software stack that has changed significantly over time.

Modern operating systems, Python versions, and package repositories no longer provide many of the exact library versions originally used by the project. As a result, attempting to install dependencies directly on a host system often leads to version conflicts and build failures.

The provided Docker image recreates a compatible Linux environment using a carefully curated dependency stack that allows the original experiments to run consistently on:

- Linux
- Windows
- Intel-based macOS systems
- Apple Silicon (M1/M2/M3/M4) Macs

The image is built for the `linux/amd64` platform to maximize compatibility with older machine learning libraries and research dependencies.

---

## Prerequisites

Install one of the following:

### Windows / macOS

- Docker Desktop

Download:

https://docs.docker.com/get-started/introduction/get-docker-desktop/

### Linux

- Docker Engine
- Docker Buildx

Verify Docker is working:

```bash
docker --version
docker buildx version
```

---

## Build the Container

Clone the repository:

```bash
git clone https://github.com/riker1/CISE-QE-DBA
cd CISE-QE-DBA
```

Build the Docker image:

```bash
docker buildx build \
  --platform linux/amd64 \
  -t cise-qe-dba-old .
```

The first build may take several minutes because Docker must download the base image and install all project dependencies.

---

## Run the Environment

Start the container:

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

The container automatically launches Jupyter Notebook.

Open your browser and navigate to:

```text
http://localhost:8888/tree
```

No authentication token or password is required.

---

## Expected Startup Output

When the container starts successfully, you should see output similar to:

```text
Jupyter Notebook 6.x is running at:
http://localhost:8888/
```

TensorFlow may display messages such as:

```text
Could not find CUDA drivers on your machine
TF-TRT Warning: Could not find TensorRT
```

These messages are expected when running on systems without NVIDIA GPUs and can safely be ignored.

---

## Running the Demo

After Jupyter loads:

1. Open `Demo.ipynb`
2. Execute notebook cells sequentially
3. Experiment with configuration settings and attack parameters
4. Review generated adversarial examples and evaluation metrics

The notebook provides the primary implementation of the BO-DBA attack and demonstrates how Bayesian Optimization can be used to generate query-efficient adversarial examples.

---

## Dataset Preparation

Download the ImageNet 2012 validation dataset:

https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5

Place the following files in the `DataSet/` directory:

```text
DataSet/
├── ILSVRC2012_img_val.tar
├── imagenet_2012_validation_synset_labels.txt
└── preprocess_imagenet_validation_data.py
```

Extract the validation archive:

```bash
cd DataSet

mkdir -p ILSVRC2012_img_val

tar -xf ILSVRC2012_img_val.tar \
    -C ILSVRC2012_img_val
```

Preprocess the validation dataset:

```bash
python preprocess_imagenet_validation_data.py \
    ILSVRC2012_img_val \
    imagenet_2012_validation_synset_labels.txt
```

After preprocessing, the directory structure should resemble:

```text
DataSet/
└── ILSVRC2012_img_val/
    ├── n01440764/
    ├── n01443537/
    ├── n01592084/
    └── ...
```

### Common Issue

Do **not** run the preprocessing script against the current directory (`.`). Doing so will create the ImageNet class folders directly under `DataSet/` instead of under `DataSet/ILSVRC2012_img_val/`, causing the notebooks to fail with errors such as:

```text
FileNotFoundError:
./DataSet/ILSVRC2012_img_val
```

The project expects all ImageNet class directories to exist beneath:

```text
DataSet/ILSVRC2012_img_val/
```

---

## Configuration

Classifier settings are controlled through:

```text
Configuration.yaml
```

Supported classifier options include:

- Inception
- ResNet

Additional configuration examples and attack parameters can be found in:

```text
Demo.ipynb
```

---

## Evaluation Experiments

Additional evaluation notebooks are located in:

```text
Evaluation/
```

These notebooks compare BO-DBA against alternative adversarial attack techniques and provide performance measurements across different attack scenarios.

---

## Legacy Manual Installation

A historical `requirements.txt` file is included for reference.

Direct installation on a host operating system is not recommended because many of the original package versions have been deprecated, replaced, or removed from modern package repositories.

For reproducibility and ease of use, the Docker-based workflow described above is the recommended installation method.

---

## Authors

- Prashant Jadiya
- Zhensheng Sun
- Nathan McDermott

## Project Preservation Notes

Docker-based modernization, dependency restoration, and Apple Silicon compatibility updates were added to preserve reproducibility of the original research environment and allow the experiments to continue running on modern hardware and operating systems.