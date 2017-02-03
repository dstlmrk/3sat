# 3-SAT problem

## Usage

```
Usage: 3sat.py [OPTIONS]

Options:
  -p, --path TEXT            Input file. [./data/example.data]
  -v, --variables INTEGER    Number of variables [20]
  -t, --temperature INTEGER  Init temperature for simulated annealing. [1000]
  -c, --cooling FLOAT        Cooling for simulated annealing. [0.85]
  -i, --inner-loop INTEGER   Number of iterations in inner loop for simulated
                             annealing. [200]
  -r, --ratio FLOAT          Ratio between satisfaction and weight from closed
                             interval from 0 to 1 [0.85]
  --help                     Show this message and exit.
```