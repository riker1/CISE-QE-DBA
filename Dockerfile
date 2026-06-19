FROM python:3.9-bullseye

WORKDIR /workspace

RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    g++ \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

COPY cleaned-requirements.txt .

RUN python -m pip install --upgrade "pip<24" setuptools wheel
RUN python -m pip install -r cleaned-requirements.txt

EXPOSE 8888
#HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
#  CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8888/', timeout=5)" || exit 1

CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=", "--NotebookApp.password="]