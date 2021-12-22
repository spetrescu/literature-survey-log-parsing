# literature-survey-log-parsing

## Experiments
This section contains detalied information regarding the Experiments section of [Log Parsing Literature Survey](). <br>
There are two environments available for running the experiments, namely Python 2 and Python 3. 
Based on the method that you would like to experiment with, please follow the appropriate setup.

### Setup Py2
In order to reproduce the experiments, make sure to run the steps below.
```
1. mkdir logparser && docker run --name logparser_py2 -it -v logparser:/logparser logpai/logparser:py2 bash
2. cd ~
3. git clone https://github.com/spetrescu/literature-survey-log-parsing.git
4. cd literature-survey-log-parsing/
5. cd experiments/
6. cd python2/
cd logparser/
7. sh fetch_data.sh
8. cd benchmark/
9. sh <METHOD>.sh
```
## Results
Each method below has been run 10 times for each dataset size.

### Scalability
<details>
  <summary><code>AEL</code></summary>
  
  - BGL
      - <details>
        <summary>[1k, ..., 300k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k]
        </details>
  - HDFS
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - OpenSSH
      - <details>
        <summary>[1k, ..., 500k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  
</details>

<details>
  <summary><code>Drain WIP</code></summary>
  
  - BGL
      - <details>
        <summary>[1k, ..., 300k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k]
        </details>
  - HDFS
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - OpenSSH
      - <details>
        <summary>[1k, ..., 500k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  
</details>

<details>
  <summary><code>LogMine</code></summary>
  
  - Android
      - <details>
        <summary>[1k, ..., 20k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k]
        </details>
  - BGL
      - <details>
        <summary>[1k, ..., 20k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  - HDFS
      - <details>
        <summary>[1k, ..., 20k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 20k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
<!--   - OpenSSH
      - <details>
        <summary>[1k, ..., 500k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 500k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details> -->
  
</details>

<details>
  <summary><code>SLCT</code></summary>
  
  - HDFS
      - <details>
        <summary>[1k, ..., 1M] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k, 1M]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 20k] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 10k] => <code>NO 20k</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  
</details>

<details>
  <summary><code>Spell</code></summary>
  
  - BGL
      - <details>
        <summary>[1k, ..., 300k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k]
        </details>
  - HDFS
      - <details>
        <summary>[1k, ..., 1M] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k, 1M]
        </details>
  - OpenSSH
      - <details>
        <summary>[1k, ..., 500k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 1M] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k, 1M]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 20k] => <code>NO 50k</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  
</details>

### Accuracy
<details>
  <summary><code>Spell</code></summary>
  
  - BGL
      - <details>
        <summary>[1k, ..., 300k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k]
        </details>
  - HDFS
      - <details>
        <summary>[1k, ..., 1M] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k, 1M]
        </details>
  - OpenSSH
      - <details>
        <summary>[1k, ..., 500k] => <code>NO 10k</code></summary>
         
        [1k, 2k, 4k, 20k, 50k, 100k, 200k, 300k, 500k]
        </details>
  - Thunderbird
      - <details>
        <summary>[1k, ..., 1M] => <code>ALL</code></summary>
         
        [1k, 2k, 4k, 10k, 20k, 50k, 100k, 200k, 300k, 500k, 1M]
        </details>
  - Windows
      - <details>
        <summary>[1k, ..., 20k] => <code>NO 50k</code></summary>
         
        [1k, 2k, 4k, 10k, 20k]
        </details>
  
</details>

## Algorithms
<details>
  <summary><code>Python 2 methods</code></summary>

- [X] AEL
- [X] Drain
- [X] IPLoM
- [X] LenMa
- [X] LFA
- [X] LKE (prblms w Android & BGL)
- [X] LogCluster (prblms w Android)
- [X] LogMine
- [X] LogSig
- [ ] MoLFI
- [X] SHISO
- [X] SLCT (no Android)
- [X] Spell ✅ (no Windows >= 50k; no Android >= 50k)
  
Although implemented, methods with * are not scalable.
</details>

<details>
  <summary><code>Python 3 methods</code></summary>
  
- [ ] MoLFI
</details>


### Setup Python 2
In order to reproduce the experiments, make sure to run the steps below.
```
1. mkdir logparser && docker run --name logparser_py2 -it -v logparser:/logparser logpai/logparser:py2 bash
2. cd ~
3. git clone https://github.com/spetrescu/literature-survey-log-parsing.git
4. cd literature-survey-log-parsing/
5. cd scripts/
6. sh fetch_data_for_experiments.sh
7. sh setup_experiments_py2.sh
8. sh test/test_scalability_experiments_py2.sh
9. sh scalability_experiments_py3.sh
```

### Setup Python 3
In order to reproduce the experiments, make sure to run the steps below.
```
1. mkdir logparser && docker run --name logparser_py3 -it -v logparser:/logparser logpai/logparser:py3 bash
2. cd ~
3. git clone https://github.com/spetrescu/literature-survey-log-parsing.git
4. cd literature-survey-log-parsing/
5. cd scripts/
6. sh fetch_data_for_experiments.sh
7. sh setup_experiments_py3.sh
8. sh test/test_scalability_experiments_py3.sh
9. sh scalability_experiments_py3.sh
```

## Method

This section contains detalied information regarding the Method section of [Log Parsing Literature Survey](). <br>
The queries used for the survey can be found under [Queries](#queries). <br>
Overall statistics can be found below.

```
Databases queried: Google Scholar, Scopus.

Number of queries (Google Scholar): 7
Number of queries (Scopus): 1

Number of papers selected after running queries (Google Scholar): 59
Number of papers selected after running queries (Scopus): 13

Number of papers selected after snowballing (Google Scholar): 34
Number of papers selected after snowballing (Scopus): 0

Total references checked while snowballing (Google Scholar): 1707
Total references checked while snowballing (Scopus): 344
Total references checked while snowballing: 2051

Total number of papers selected for survey: 93
```

### <a name="queries"></a>Queries
Find below the queries used for the survey.
#### Google Scholar
<details>
  <summary>[QUERY 1] <code>log parsing</code></summary>
  
  1. <details>
     <summary><a href="https://arxiv.org/abs/1811.03509">Tools and Benchmarks for Automated Log Parsing</a> <b>(57)</b></summary>
 
     1. [SherLog: Error Diagnosis by Connecting Clues from Run-time Logs](https://dl.acm.org/doi/10.1145/1735971.1736038)
     2. [DeepLog: Anomaly Detection and Diagnosis from System Logs through Deep Learning](https://dl.acm.org/doi/10.1145/3133956.3134015)
     3. [Detecting Large-Scale System Problems by Mining Console Logs](https://dl.acm.org/doi/10.1145/1629575.1629587)
     4. [A Data Clustering Algorithm for Mining Patterns From Event Logs](https://ieeexplore.ieee.org/document/1251233)
     5. [LogCluster - A Data Clustering and Pattern Mining Algorithm for Event Logs](https://ieeexplore.ieee.org/document/7367331)
     6. [Clustering Event Logs Using Iterative Partitioning](https://dl.acm.org/doi/10.1145/1557019.1557154)
     7. [Length Matters: Clustering System Log Messages using Length of Words](https://arxiv.org/abs/1611.03213)
     8. [LogMine: Fast Pattern Recognition for Log Analytics](https://dl.acm.org/doi/10.1145/2983323.2983358)
     9. [Abstracting Log Lines to Log Event Types for Mining Software System Logs](https://ieeexplore.ieee.org/document/5463281)
     10. [LogSig: Generating System Events from Raw Textual Logs](https://dl.acm.org/doi/10.1145/2063576.2063690)
     11. [Incremental Mining of System Log Format](https://ieeexplore.ieee.org/document/6649746)
     12. [Abstracting Execution Logs to Execution Events for Enterprise Applications (Short Paper)](https://ieeexplore.ieee.org/document/4601543)
     </details>
  2. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/8067504">Towards Automated Log Parsing for Large-Scale Log Data Analysis</a> <b>(54)</b></summary>
  
     1. [Execution Anomaly Detection in Distributed Systems through Unstructured Log Analysis](https://ieeexplore.ieee.org/document/5360240)
     2. [A Lightweight Algorithm for Message Type Extraction in System Application Logs](https://ieeexplore.ieee.org/document/5936060)
     </details>
  3. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/7579781">An Evaluation Study on Log Parsing and Its Use in Log Mining</a> <b>(41)</b></summary>
  
     1. [Mining Event Logs with SLCT and LogHound](https://ieeexplore.ieee.org/abstract/document/4575281)
     </details>
  4. [Drain: An Online Log Parsing Approach with Fixed Depth Tree](https://ieeexplore.ieee.org/document/8029742) **(35)**
  5. [A Directed Acyclic Graph Approach to Online Log Parsing](https://arxiv.org/abs/1806.04356) **(41)**
  6. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/9134790">Logram: Efficient Log Parsing Using n-Gram Dictionaries</a> <b>(74)</b></summary>
  
     1. [Mining Invariants from Console Logs for System Problem Detection](https://www.usenix.org/conference/usenix-atc-10/mining-invariants-console-logs-system-problem-detection)
     2. [An automated approach for abstracting execution logs to execution events](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.332.9832&rep=rep1&type=pdf)
     3. [Efficiently Extracting Operational Profiles from Execution Logs Using Suffix Arrays](https://ieeexplore.ieee.org/document/5362080)
     </details>
  7. [Self-Supervised Log Parsing](https://arxiv.org/abs/2003.07905) **(20)**
  8. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/9209681">LogParse: Making Log Parsing Adaptive through Word Classification</a> <b>(34)</b></summary>
  
     1. [Learning Latent Events from Network Message Logs](https://arxiv.org/abs/1804.03346)
     </details>
  9. [Improving Performances of Log Mining for Anomaly Prediction Through NLP-Based Log Parsing](https://arxiv.org/abs/2003.07905) **(19)**
  1. <details>
     <summary><a href="https://ieeexplore.ieee.org/document/7837916">Spell: Streaming Parsing of System Event Logs</a> <b>(18)</b></summary>
  
     1. [LogTree: A Framework for Generating System Events from Raw Textual Logs](https://ieeexplore.ieee.org/document/5694003)
     2. [HLAer: a System for Heterogeneous Log Analysis](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.714.8589&rep=rep1&type=pdf)
     </details>
  2. [LPV: A Log Parser Based on Vectorization for Offline and Online Log Parsing](https://ieeexplore.ieee.org/abstract/document/9338336) **(21)**
  3. [An Efficient Log Parsing Algorithm Based on Heuristic Rules](https://link.springer.com/chapter/10.1007/978-3-030-29611-7_10) **(30)**
  4. [Paddy: An Event Log Parsing Approach using Dynamic Dictionary](https://ieeexplore.ieee.org/abstract/document/9110435) **(21)**
  5. [A Theoretical Framework for Understanding the Relationship Between Log Parsing and Anomaly Detection](https://link.springer.com/chapter/10.1007/978-3-030-88494-9_16) **(25)**
  6. [Spell: Online Streaming Parsing of Large Unstructured System Logs](https://ieeexplore.ieee.org/document/8489912) **(36)**
  7. [A Confidence-Guided Evaluation for Log Parsers Inner Quality](https://link.springer.com/article/10.1007/s11036-019-01501-6) **(48)**
  8. <details>
     <summary><a href="https://arxiv.org/abs/2110.15473">AWSOM-LP: An Effective Log Parsing Technique Using Pattern Recognition and Frequency Analysis</a> <b>(45)</b></summary>
  
     1. [Towards an NLP-based log template generation algorithm for system log analysis](https://dl.acm.org/doi/abs/10.1145/2619287.2619290)
     </details>
  9. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/9458609">Prefix-Graph: A Versatile Log Parsing Approach Merging Prefix Tree with Probabilistic Graph</a> <b>(27)</b></summary>
  
     1. [LogAnomaly: Unsupervised Detection of Sequential and Quantitative Anomalies in Unstructured Logs](https://www.ijcai.org/proceedings/2019/658)
     2. [Logan: A Distributed Online Log Parser](https://ieeexplore.ieee.org/document/8731527)
     </details>
  1. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/8988255">Efficient and Robust Syslog Parsing for Network Devices in Datacenter Networks</a> <b>(47)</b></summary>
  
     1. [Device-Agnostic Log Anomaly Classification with Partial Labels](https://ieeexplore.ieee.org/document/8624141)
     </details>
  2. <details>
     <summary><a href="https://dl.acm.org/doi/10.1145/3338906.3338931">Robust Log-Based Anomaly Detection on Unstable Log Data</a> <b>(48)</b></summary>
  
     1. [Experience Report: Log Mining Using Natural Language Processing and Application to Anomaly Detection](https://www.semanticscholar.org/paper/Experience-Report%3A-Log-Mining-Using-Natural-and-to-Bertero-Roy/bf06e55ccae276d39fa7476ff7a4a6ac8437579e)
     </details>
  3. [LogStamp: Automatic Online Log Parsing Based on Sequence Labelling](https://www.performance2021.deib.polimi.it/wp-content/uploads/2021/10/WAIN_2021_paper_12_Tao.pdf) **(23)**
  4. [A Review of Unstructured Data Analysis and Parsing Methods](https://ieeexplore.ieee.org/abstract/document/9167588) **(33)**
  5. [OLMPT: Research on Online Log Parsing Method Based on Prefix Tree](https://dl.acm.org/doi/10.1145/3452940.3452951) **(13)**
  6. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/8989069">A Parallel Approach of Weighted Edit Distance Calculation for Log Parsing</a> <b>(10)</b></summary>
  
     1. [LogMaster: Mining Event Correlations in Logs of Large-scale Cluster Systems](https://arxiv.org/abs/1003.0951)
     </details>
  7. <details>
     <summary><a href="https://arxiv.org/abs/2001.01216">Flexible Log File Parsing using Hidden Markov Models</a> <b>(13)</b></summary>
  
     1. [A Breadth-First Algorithm for Mining Frequent Patterns from Event Logs](https://link.springer.com/content/pdf/10.1007%2F978-3-540-30179-0_27.pdf)
     </details>
  8. <details>
     <summary><a href="https://ieeexplore.ieee.org/abstract/document/7883294">Log Clustering Based Problem Identification for Online Service Systems</a> <b>(30)</b></summary>
  
     1. [Experience Mining Google’s Production Console Logs](https://www.usenix.org/legacy/events/slaml10/tech/full_papers/Xu.pdf)
     </details>
  9. [Unsupervised Noise Detection in Unstructured data for Automatic Parsing](https://ieeexplore.ieee.org/abstract/document/9269096) **(21)**
</details>

<details>
  <summary>[QUERY 2] <code>log parsing survey</code></summary>
  
  1. <details>
     <summary><a href="https://www.sciencedirect.com/science/article/pii/S0167404820300250">System log clustering approaches for cyber security applications: A survey</a> <b>(80)</b></summary>
  
     1. [One Graph Is Worth a Thousand Logs: Uncovering Hidden Structures in Massive System Event Logs](https://link.springer.com/chapter/10.1007/978-3-642-04180-8_32)
     2. [GenLog: Accurate Log Template Discovery for Stripped X86 Binaries](https://ieeexplore.ieee.org/document/8029626)
     </details>
  2. [A Survey on Automated Log Analysis for Reliability Engineering](https://dl.acm.org/doi/abs/10.1145/3460345) **(205)**
</details>

<details>
  <summary>[QUERY 3] <code>log abstraction</code></summary>
  
  1. <details>
     <summary><a href="https://www.sciencedirect.com/science/article/abs/pii/S0950584920300264?casa_token=iZOiGEqQoKwAAAAA:b6CTyhaGiai9R-prLmP3HLhFETQgr6H7b4oTIv17-iWQrAOemWF5Wslj35wvpHqXDTxWSnkvQjG8">A systematic literature review on automated log abstraction techniques</a> <b>(55)</b></summary>
  
     1. [A Method of Large - Scale Log Pattern Mining](https://link.springer.com/chapter/10.1007/978-3-319-74521-3_9)
     </details>
  2. [Symptom-based Problem Determination Using Log Data Abstraction](https://dl.acm.org/doi/10.1145/1923947.1923979) **(37)**
  3. [Unsupervised Event Abstraction using Pattern Abstraction and Local Process Models](https://arxiv.org/abs/1704.03520) **(15)**
  4. [Automatic Event Log Abstraction to Support Forensic Investigation](https://dl.acm.org/doi/10.1145/3373017.3373018) **(28)**
  5. [Event-Log Abstraction using Batch Session Identification and Clustering](https://dl.acm.org/doi/10.1145/3341105.3373861) **(20)**
  6. [Event Log Abstraction in Client-Server Applications](https://www.researchgate.net/publication/355763915_Event_Log_Abstraction_in_Client-Server_Applications) **(24)**
  7. <details>
     <summary><a href="https://dl.acm.org/doi/10.1145/3465481.3470083">Log Abstraction for Information Security: Heuristics and Reproducibility</a> <b>(39)</b></summary>
  
     1. [amulog: A General Log Analysis Framework for Diverse Template Generation Methods](https://ieeexplore.ieee.org/document/9269049)
     </details>
  8. [Practical Multi-pattern Matching Approach for Fast and Scalable Log Abstraction](https://www.semanticscholar.org/paper/Practical-Multi-pattern-Matching-Approach-for-Fast-Tovarnák/29d33b370ccd63c56e796a3aadcd45605f325a63) **(15)**
  
</details>

<details>
  <summary>[QUERY 4] <code>log abstraction survey</code></summary>
  
  &mdash;
  
</details>

<details>
  <summary>[QUERY 5] <code>event log parsing</code></summary>
  
  1. [LogLens: A Real-Time Log Analysis System](https://ieeexplore.ieee.org/document/8416368) **(36)**
  2. [Loghub: A Large Collection of System Log Datasets towards Automated Log Analytics](https://arxiv.org/abs/2008.06448) **(69)**
  3. [Experience Report: System Log Analysis for Anomaly Detection](https://ieeexplore.ieee.org/document/7774521) **(49)**
  4. [LOGAIDER: A Tool for Mining Potential Correlations of HPC Log Events](https://ieeexplore.ieee.org/document/7973730) **(23)**
  5. <details>
     <summary><a href="https://link.springer.com/article/10.1007/s10796-020-10026-3">LogGAN: a Log-level Generative Adversarial Network for Anomaly Detection using Permutation Event Modeling</a> <b>(32)</b></summary>
  
     1. [Event Extraction from Streaming System Logs](https://link.springer.com/chapter/10.1007%2F978-981-13-1056-0_47)
     </details>
  6. [A Search-based Approach for Accurate Identification of Log Message Formats](https://dl.acm.org/doi/10.1145/3196321.3196340) **(36)**
  
</details>

<details>
  <summary>[QUERY 6] <code>log signature extraction</code></summary>
  
  1. [Unsupervised Signature Extraction from Forensic Logs](https://link.springer.com/chapter/10.1007/978-3-319-71273-4_25) **(27)**
  2. [Towards a neural language model for signature extraction from forensic logs](https://ieeexplore.ieee.org/document/7916497) **(16)**
  3. [A hybrid approach for log signature generation](https://www.emerald.com/insight/content/doi/10.1016/j.aci.2019.05.002/full/html) **(17)**
  
</details>

<details>
  <summary>[QUERY 7] <code>event log signature extraction</code></summary>
  
  &mdash;
  
</details>

#### Scopus

<details>
  <summary>[Query Scopus] <code>TITLE-ABS-KEY(log AND parsing) OR ((logs OR log OR logging OR events OR "event log" OR "event logs" OR "event logs templates" OR "event log signatures" ) AND (abstractionOR parsing))</code></summary>
  
  1. [Log and Execution Trace Analytics System](https://ieeexplore.ieee.org/document/9548437) **(26)**
  2. [Virtual Knowledge Graphs for Federated Log Analysis](https://dl.acm.org/doi/abs/10.1145/3465481.3465767) **(23)**
  3. [The Use of Template Miners and Encryption in Log Message Compression](https://www.researchgate.net/publication/352688634_The_Use_of_Template_Miners_and_Encryption_in_Log_Message_Compression) **(39)**
  4. [LogEA: Log Extraction and Analysis Tool to Support Forensic Investigation of Linux-based System](https://www.semanticscholar.org/paper/LogEA%3A-Log-Extraction-and-Analysis-Tool-to-Support-Dusane-Sujatha/f39071d3a82c92a36d8260c86618e9cb08e33541) **(27)**
  5. [On Automatic Parsing of Log Records](https://arxiv.org/abs/2102.06320) **(36)**
  6. [MoniLog: An Automated Log-Based Anomaly Detection System for Cloud Computing Infrastructures](https://www.semanticscholar.org/paper/MoniLog%3A-An-Automated-Log-Based-Anomaly-Detection-Vervaet/24ea86f660260e95768a341a47965907d0046793) **(38)**
  7. [An Improved KNN-Based Efficient Log Anomaly Detection Method with Automatically Labeled Samples](https://dl.acm.org/doi/10.1145/3441448) **(34)**
  8. [An Extensible Parsing Pipeline for Unstructured Data Processing](https://www.researchgate.net/publication/349984905_An_Extensible_Parsing_Pipeline_for_Unstructured_Data_Processing) **(22)**
  9. [A Dynamic Processing Algorithm for Variable Data in Intranet Security Monitoring](https://link.springer.com/chapter/10.1007/978-3-030-78612-0_12) **(14)**
  1. [METING: A Robust Log Parser Based on Frequent n-Gram Mining](https://ieeexplore.ieee.org/document/9283937) **(19)**
  2. [Log Parser with One-to-One Markup](https://ieeexplore.ieee.org/document/9092114) **(36)**
  3. [FastLogSim: A Quick Log Pattern Parser Scheme Based on Text Similarity](https://link.springer.com/chapter/10.1007/978-3-030-55130-8_19) **(17)**
  4. [AECID-PG: A Tree-Based Log Parser Generator To Enable Log Analysis](https://ieeexplore.ieee.org/document/8717887) **(13)**
  
</details>

