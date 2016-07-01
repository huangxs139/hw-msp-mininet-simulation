## Overview

This is codes of my experiment to simulate a 2- or 3-level switches topo-tree for msp project of huawei.
As time goes by, I cannot remember the design details of each test. A good thing is, all meta-tests are
written by python2 with small sizes. Try to read through to find how you can use them for your targets.
Please notice that the codes are only for experiments as they were not considered with robustment. Even 
a small change of file's name or folder's place would lead to a series of bugs. Keep everything where 
they were as far as possible. But take easy to modify any contents of them.

## Previous Work

Please install mininet and configure it properly.

```bash
git clone git://github.com/mininet/mininet
mininet/util/install.sh -a
sudo mn --test pingall
```

If you need more information about config options or you want to install it from other sources, please 
refer to http://mininet.org

Moreover, you need to prepare Python2 of version 2.7.6 at least. I guess I were writing with Python2.7.8 
and all tests were running well.

## Tests

+ run.sh
This shell script is aimed to make sub-folder in directory 'result' which relate to all host-nodes in 
simulated network by their ID. Change this script to fit your network's scale and run it first.

+ bwsim.py
This is the main test to build the topo-tree in mininet platform and then to run a perf test among the 
simulated network. It seems that I had merged all parameters inside, as a result, the test may output a
mass of logs which will be sorted into different folders in directory 'result/'.
If you are going to adjust the scale of your simulated network, or to modify cyclic granularity of data
to transfered in perfing, you are suggested to read over this script clearly.
By the way, you must run this script as root due to it calls mininet which needs authority of access to 
your hardwares, especially the NIC. 

+ gather.py
When all tests executed by bwsim.py have been finished, this script may help you to gather scattered raw
test outputs together as been classified into different test groups. You might see files named like
'100nodes.20MB.2pipes.out' be generated in directory 'result/'. The three fields splited by dot(.) could
map to number of nodes, size of data transfered per perf and number of pipes. The 2 pipes stands for 
cutting total 20MB data into 2 slices with 10MB each then sending them sequentially. See details in the 
project design document, which should not open public on github.
This script does another work to dump all test results into '.ana' files in directory 'analysis/' with the 
format of adjacency list. Each line may contains 4 fields corresponding to child_node, current_node, 
parent_switch, consuming time. These '.ana' files make custom analysis and drawing graphs much easier.

+ analy2.py
By running this tool, '.ana' files are analyzed to figure out the total time overhead for every test group,
the final result will be saved both as text in 'ans' and as parameters in 'fig_data', which could be used as
the input file to draw graphs via Python-matplotlib.

+ check.py
This tool can check whether all tests run out legal results into output files. It will raise error messages 
when missing or redundant results are detected.

+ dataGather.py, ts.py, analy.py, in
These files seems have been discarded yet, but I did not remove them into trush.

+ fig*.py
These scripts are response to drawing graphs on experiment's results, but they were written in bad manner. 
Try to re-write them to meet your own needs.

## Other comments

1. Current files under directory 'results/' only show you how test results would be named and placed while 
all tests run correctly. Most of them contain nothing now due to my last clean-up operation before uploaded
them

2. There remains some graphs here to show you what experiments I had run before. Please DO NOT use them
directly instead of running new, authentic results. Please hold your faith to your work.

## License