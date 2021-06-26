# GreenCodeEvaluator
<img align="right" width="200" height="200" alt="bertha" src="bertha.png"></img>
This is our proposal for Mercedes' HerHackaton Challenge. 

## Installation

```commandline
pip install git+https://github.com/martasls/GreenCodeEvaluator.git
```

## Usage

From your command line you can run:
```commandline
gcode analyze /home/user/example.py /home/user/results
```

The 'results' folder doesn't need to exist. If it doesn't, the tool will create it for you and populate it with the 
output coming from the analysis.

## Memory Profiling 

See how memory is being used with the [memory-profiling](https://pypi.org/project/memory-profiler/) package. 

```commandline
pip install memory-profiling
```

- To check your file code_to_analyse, and then the corresponding plot, run on your terminal :
```console
mprof run code_to_analyse.py 
mprof plot
```


Note : In order to have the corresponding functions appearing in the plot across time, '@profile' decorators are needed above each function definition. Read here for more info http://fa.bianp.net/blog/2014/plot-memory-usage-as-a-function-of-time/ 

Example with bad_function.py 
```console
mprof run bad_functions.py 
mprof plot
```
![Results](experiments/romaissa/result/result_bad_func.png)

----

Repository for the HerHackathon 2021


- Every participant should have her own GitHub account
- For each team, a participant forks this repo and gives her teammates access rights accordingly
- Each team works on their own repository. It is probably beneficial to be familiar with GitHub Actions to have a common development environment
- At the end, teams can submit pull requests back to this repo, where appropriate. Please note that we ask you to sign our [Contributor License Agreement](https://github.com/Daimler/daimler-foss/blob/master/cla/2019-09-11_Daimler_FOSS_CLA_DaimlerTSS.pdf) and then submit to [Daimler TSS CLA team](mailto:CLA-TSS@daimler.com) so that we can accept your contribution.


Don't know where to get started? Click [here](https://github.com/Daimler/GreenCodeEvaluator/blob/main/HerHackathon-Challenge.pdf).
