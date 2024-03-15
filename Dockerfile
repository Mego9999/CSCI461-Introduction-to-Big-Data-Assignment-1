FROM ubuntu:latest
ENV PIP_TIMEOUT=2000
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*
RUN pip3 install pandas 
RUN pip3 install numpy 
RUN pip3 install seaborn
RUN pip3 install matplotlib 
RUN pip3 install scikit-learn 
RUN mkdir -p /home/doc-bd-a1/
WORKDIR /home/doc-bd-a1/
COPY load.py .
COPY model.py .
COPY dpre.py .
COPY eda.py .
COPY vis.py .
COPY Titanic-Dataset.csv .
CMD ["/bin/bash"]
