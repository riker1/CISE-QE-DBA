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

## Recommended Workflow

Follow these steps in order for a clean setup.

### 1. Clone the Repository

```bash
git clone https://github.com/riker1/CISE-QE-DBA
cd CISE-QE-DBA
```

### 2. Prepare the ImageNet Validation Dataset

The BO-DBA experiments require the ImageNet 2012 validation dataset.

Download the dataset from Academic Torrents:

https://academictorrents.com/details/5d6d0df7ed81efd49ca99ea4737e0ae5e3a5f2e5

Students unfamiliar with BitTorrent may use one of the following clients:

- Transmission (macOS, Linux)
- qBittorrent (Windows, macOS, Linux)

After opening the torrent file in your BitTorrent client, download:

```text
ILSVRC2012_img_val.tar
```

The completed archive should be approximately **6.3 GB**.

Place the following files in the `DataSet/` directory:

```text
DataSet/
├── ILSVRC2012_img_val.tar
├── imagenet_2012_validation_synset_labels.txt
└── preprocess_imagenet_validation_data.py
```

Extract the validation archive into the directory expected by the project:

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

### 3. Build the Docker Environment

```bash
docker buildx build \
  --platform linux/amd64 \
  -t cise-qe-dba-old .
```

The first build may take several minutes while Docker downloads and installs the required machine learning libraries.

### 4. Start the Environment

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

### 5. Open Jupyter Notebook

Navigate to:

```text
http://localhost:8888/tree
```

Open:

```text
Demo.ipynb
```

### 6. Run the Demo

Execute the notebook cells sequentially.

For an initial functionality test, temporarily reduce:

```python
queryBudgets = 500
```

to:

```python
queryBudgets = 2
```

This allows the notebook to complete quickly and confirms that the environment, dataset, and attack pipeline are functioning correctly before launching longer experiments.

---

## Expected Startup Messages

When a notebook kernel starts, the container uses a compatibility launcher that preloads TensorFlow and Matplotlib before starting `ipykernel`.

You should see messages similar to:

```text
Preloading TensorFlow before ipykernel starts...
Preloading matplotlib Agg backend before ipykernel starts...
Preloads complete. Starting ipykernel...
```

These messages are expected.

TensorFlow may also report missing CUDA or TensorRT libraries when running on systems without NVIDIA GPUs. These warnings are expected and do not prevent the experiments from running.

---

## Verification

A quick verification path is:

1. Start the Docker container.
2. Open `Demo.ipynb`.
3. Set `queryBudgets = 2` for a short test run.
4. Execute the notebook cells sequentially.

If the environment is working, the notebook should load the dataset, initialize the classifier, and begin running model predictions. The first execution may take several minutes while TensorFlow downloads pre-trained model weights. Longer runs with the default query budget may take significant time, especially on Apple Silicon systems running the `linux/amd64` image through Docker Desktop emulation.

---

## Dataset Notes and Common Issues

The project expects all ImageNet class directories to exist beneath:

```text
DataSet/ILSVRC2012_img_val/
```

Do **not** run the preprocessing script against the current directory (`.`). Doing so will create the ImageNet class folders directly under `DataSet/` instead of under `DataSet/ILSVRC2012_img_val/`.

If the class folders are created directly under `DataSet/`, the notebooks may fail with an error similar to:

```text
FileNotFoundError:
./DataSet/ILSVRC2012_img_val
```

If this happens, rerun the preprocessing step using the correct path shown in the Recommended Workflow, or move the generated `n*` class directories into:

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

---

## Project Preservation Notes

Docker-based modernization, dependency restoration, Jupyter compatibility fixes, TensorFlow startup workarounds, and Apple Silicon compatibility updates were added to preserve reproducibility of the original research environment and allow the experiments to continue running on modern hardware and operating systems.