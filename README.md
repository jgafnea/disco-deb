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

I chose Python because it's normally what I use once tasks become too much for shell scripts.

I started by breaking the project down into three functions, each performing one of the tasks described in the instructions: fetching, parsing, and output.

For fetching, I used `requests` because it generally makes HTTP things easier. Work is done in memory and performs well given the small file sizes. For significantly larger files, this is something that would need to be adjusted, possibly with streaming, to process data in chunks.

For parsing, I used a series of splits (`splitlines`, `rsplit`, and `split`) to break the contents down into lines and then into collections of files and associated packages.

For counting, I used `Counter` because it performs as well as hash tables and it's a lot easier to use and understand, especially coming back to something months later.

For printing, I used `most_common` to get the top 10 packages (optionally accepting a different number) and `enumerate` to loop through and print each one. I added a utility function using running maximums and used those values with f-strings to print results with columns aligned.

For parsing arguments, I used `argparse` because it handles basic validation and shows accepted arguments on usage. Not the prettiest CLI, but it works.

For main functionality, I wrapped everything in `main()` and called it at the end.

For testing, I used `pytest` because it does everything `unittest` does with much less work. I focused on areas where I had actual issues, namely the parsing and counting, rather than writing tests just for the sake of coverage.

Total time: ~~6~~ 7 hours.

## Obstacles

Things that were harder than they prob should have been:

#### Mentally parsing items
   
```
bin/file libdevel/packageA,libdevel/packageB
```
For whatever reason I kept getting files and packages backwards and ending up with wrong totals. Writing out the parsing logic and adding variables made the format much easier to follow.

#### Naming things

This is especially hard when there's ambiguity, like [in the fetching function](./assets/contents.png). Normally I'll rename something like `contents_` to point out that _this_ is the key element, and in this case, that meant the value being returned. I don't know if that's a good or bad practice, but it's something I picked up somewhere.

#### Documentation

This documentation was, by far, the hardest part of the project. I'm okay with code, testing, and documentation in general, but framing my thoughts explicitly was new and I'm especially terrified of doing it all "wrong." I tried to "think out loud" and translate that into written form, I hope the result conveys the what and why effectively. 🤞🙏



