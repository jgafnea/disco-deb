# disco-deb

![Tests](https://github.com/jgafnea/disco-deb/actions/workflows/python.yml/badge.svg)

Project showing the top 10 packages (based on the number of associated files) from a Debian repo.

## Usage

1. Clone the project, cd into the directory
2. Run `make amd64` (or another architecture)

```sh
git clone https://github.com/jgafnea/disco-deb && cd disco-deb
make amd64

01. devel/piglit                53007
02. science/esys-particle       18408
03. math/acl2-books             17023
04. libdevel/libboost1.81-dev   15456
05. libdevel/libboost1.74-dev   14333
06. lisp/racket                  9599
07. net/zoneminder               8161
08. electronics/horizon-eda      8130
09. libdevel/libtorch-dev        8089
10. libdevel/liboce-modeling-dev 7458
```

## Reportage

Moved [here](/docs/report.md).
