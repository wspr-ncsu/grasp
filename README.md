# GRASP
This repository contains the implementation and analysis scripts for the paper
["GRASP: Hardening Serverless Applications through Graph Reachability Analysis
of Security Policies"](https://dl.acm.org/doi/10.1145/3589334.3645436),
published in WWW 2024. GRASP is a graph-based analysis framework for modeling
serverless access control policies as queryable reachability graphs.

# Accessing the original dataset analyzed in the paper
The dataset of serverless projects analyzed in the GRASP paper is too large to
host in a git repository. Please send a request for the original dataset.

# How to run
To run the analysis on your dataset:
* List serverless.yml paths to analyze in the
`misc-scripts/data/sec-policy-only.csv` file. 
* `cd checkov/checkov/`
* `python3 tool_name.py -l FILE_LIST` : This command generates the model facts for each yml file in the
  `misc-scripts/data/new-results` directory and outputs the parsed-permissions
  in the `misc-scripts/data/parsed-permissions.csv` file.  
* `python3 misc-scripts/graph_stats.py`: This command analyzes the fact files
  from the `misc-scripts/data/new-results` directory and computes public and
  private functions, exfiltration paths, and other attributes. The output is
  written to the `misc-scripts/data/prolog-results.csv` file. 

* Some additional analysis scripts and files used for the evaluation are in the
  `additional` directory. 