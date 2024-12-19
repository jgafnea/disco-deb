# disco-deb

Project showing the top 10 packages (based on the number of associated files) from a Debian repo 

## Usage

1. Clone the project, cd into the directory
2. Create venv, activate it, install deps
3. Run `python app.py arm64` (or another architecture)

   
```sh
git clone https://github.com/jgafnea/disco-deb && cd disco-deb

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python app.py arm64
01. devel/piglit                       53007
02. science/esys-particle              18408
03. math/acl2-books                    17023
04. libdevel/libboost1.81-dev          15456
05. libdevel/libboost1.74-dev          14333
06. lisp/racket                         9599
07. net/zoneminder                      8161
08. electronics/horizon-eda             8130
09. libdevel/libtorch-dev               8089
10. libdevel/liboce-modeling-dev        7458
```

## Reportage

I chose Python because it's normally what I use once tasks become too much for shell scripts.

I started by breaking the project down into three functions, each performing one of the tasks described in the instructions: fetching, parsing, and output.

For fetching, I used `requests` because it generally makes HTTP things easier. Work is currently done in memory and works well given the small file sizes, but would need to be updated for significantly larger files.

For parsing, I used a series of splits (`splitlines`, `rsplit`, and `split`) to break the contents down into lines and then into collections of files and associated packages. One challenge was mentally parsing lines like

```
bin/example libdevel/packageA,libdevel/packageB
```

which seemed "backward". Writing the parsing logic and adding explicit variables helped clarify the formatting and make it easier to follow.

For counting, I used `Counter` because it performs as well as a hash table but it's easier to use and read, especially coming back to it months later.

For printing, I used `most_common` to get the top 10 packages (optionally accepting a different number) and `enumerate` to loop through and print each one. I added a utility function using running maximums and used those values with f-strings to print results with columns aligned.

For parsing arguments, I used `argparse` because it handles basic validation and shows accepted arguments on usage.

For main functionality, I wrapped everything in a `main()` function and called it at the end.

For testing, I used `pytest` to mock the `Contents` and shorten the testing cycle. I admittedly didn't go crazy on networking edge cases, I instead focused on the areas I wanted to ensure worked correctly, namely the parsing, counting, and handling of malformatted lines.

This documentation was, by far, the hardest part of the project. I'm okay with code, testing, and documentation in general, but framing my thoughts explicitly was new and I'm especially terrified of doing it all "wrong." I tried to "think out loud" and translate that into written form, I hope the result conveys the what and why effectively. 🤞🙏

Total time was 6 hours.
