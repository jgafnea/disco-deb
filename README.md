# disco-deb

Project showing the top 10 packages (based on the number of associated files) from a Debian repo

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

## Journal

I chose Python for its readability, familiarity, and extensive library of tools. I began by breaking the project into three functions, each performing one of the tasks described in the instructions: fetching, parsing, and formatting. 

For fetching, I used `requests` to simplify the request and error handling. I downloaded, decompressed, and decoded the response object working in memory. Performance was fine given the smaller file sizes, but for handling larger files, it'd be necessary at some point to implement streaming to process the response in chunks to avoid memory issues.

For parsing, I used a series of splits to break the contents down into lines and then into pairs of filenames and associated packages. For counting, I used `Counter` for its performance and ease of use compared to a DIY hash table.

For output, I used `most_common` to get the top N packages and `enumerate` to loop through and print each one. I added a utility function using running maximums to get the max widths of the columns and used those values with f-strings to print results with columns neatly aligned.

For the main functionality, I used `argparse` to perform basic validation and print usage information on error. I wrapped everything in `main()` and called it at the end.

Total time: 6 hours.

## Obstacles

This documentation was, by far, the most challenging part of the project. I'm okay with documentation in general, but explicitly expressing my thoughts is something new. Also the term "Final Report" seems widely used, but lacks a standardized (or even standard-ish) structure, which added to the challenge. The existing guides I could find were often contradictory, offering conflicting advice on how to write and format everything.

Other issues were relatively small in comparison. The Debian Wiki contained some outdated information about the Contents file, which initially led to confusion until I realized it was no longer accurate. Additionally, setting up network mocking and testing proved to be more time-consuming than I had anticipated.
