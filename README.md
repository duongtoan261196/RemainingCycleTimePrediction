# Remaining cycle time prediction with Graph Neural Networks for Predictive Process Monitoring

This repository provides materials to reproduce the results presented in the paper "**Remaining cycle time prediction with Graph Neural Networks for Predictive Process Monitoring**". 

## Dataset
The **1_Data** folder contains raw data of Helpdesk and BPIC20 datasets. We can not provide the EMS3141 data due to the confidentiality reasons.
The statistics of theses logs are shown in the table below:
Event log |  Num. cases | Num. activities | Num. events | Avg. case length | Max. case lenth | Avg. case duration (days) | Max. case duration (days) | Min. case duration (days) | Variants
---|---|---|---|---|---|---|---|---|---
Helpdesk | 4552 | 10 | 21197 | 4.66 | 15 | 40.85 | 59.99 | 30.64 | 207 
BPIC20 | 10043 | 15 | 55130 | 5.49 | 24 | 11.62 | 368.19 | 1.06 | 64 
EMS3141 | 99282 | 35 | 287117 | 28.76 | 44 | 7.01 | 80.87 | 0.69 | 296 

## Installation
The project is implemented with jupyter notebook in both python and pytorch.
* pytorch: Follow the instructions in the PyTorch website https://pytorch.org/get-started/locally/
* torch geometric: https://pytorch-geometric.readthedocs.io/en/latest/notes/installation.html
* PM4Py: 
  ``pip install pm4py``

## Implementation
There are 4 ``.ipynb`` files in **3_Notebooks** folder. The notebook **Data_processing.ipynb** must be run first to obtain the processed data. Three other notebooks each correspond to a model, i.e., LSTM, GCN and Gated GNN.


