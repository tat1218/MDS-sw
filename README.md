# Workload Scheduling in Smart Camera Edge Cluster: DAG Hybrid Scheduling Algorithm

This repository is based on [https://github.com/yhjh5302/Multiple-DNN-Scheduling]

## About the project

*  Get data from testing various cases in workload deviation and total sum
*  From data, design new scheduling algorithm for DAG

## Prerequisites
#### General
*  python>=3.6
*  numpy
*  matplotlib

## How to run
#### 1. Build C++ functions
>  python3 build_script.py build_ext --inplace

#### 2. Run example
*4 local server(smart camera), 1 edge server and workload remain and use HEFT scheduling algorithm
    [0, 0.1, 0.2, 0.03   ,     0.1] (sec)
>  python3 main.py --workload_remain 0 0.1 0.2 0.03 0.1 --offloading "HEFT"
