# Final Project

## Content we have to implement

- classical int ALU operations
  - and
  - or
  - xor
  - add/sub
  - bit shift
  - multiply
  - divide?
  - less/greater/equal compare
- operations unique to QC
  - create equal superpositional states of two numbers
    - e.g. |0010> |+| |1000> = 1/sqrt(2)(|0010> + |1000>)
  - remove a number from a superpositional state - by setting its amplitude to 0
    - e.g. 1/2(|000> + |001> + |010> + |011>) --remove-|011>--> 1/sqrt(3)(|000> + |001> + |010>)
  - increase the amplitude of a target number in a state to 1 (and decrease other numbers in that state to 0)
    - if impossible, use ancila bits with xor to achieve similar results on the target number
- From these, we can create a unique QC that specifically handles database queries
  - find equals/less than/greater than from among a database
  - get the operations time complexities O(?)
- Other algorithms for fun?


## Required material

- online shared drive (google drive)
  - write-up to place our results (include sources cited)
  - slide/poster presentation (do last, but before poster deadline)
  - final report (https://bcourses.berkeley.edu/courses/1542626/discussion_topics/7040534)
- cpu simulator (Qiskit)
- gpu simulator (CUDA-Q / cuQuantum)
- shared code repo (GitHub)
- lots of googling/reading


## Individual responsibilities

- Lindsey: Qiskit, and
- Alex: Qiskit, xor
- Joseph: Qiskit


## Deadlines
- this week 4/13 - write down methods for all ALU ops, simulate on Qiskit and CU-
- next week 4/20 - 
- last week 4/27 - 
