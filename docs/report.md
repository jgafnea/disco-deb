# Project

> The project has two parts: Tooling and Documentation.
>
> **The Tooling**:
>
> The first half of the project is writing a program. It should **fetch** the
> relevant [“Contents” index](https://wiki.debian.org/DebianRepository/Format#A.22Contents.22_indices) from a Debian mirror for the particular
> architecture (e.g. arm64) passed as an argument, and then it must **parse** the
> file and **output** the 10 packages with the most associations and what the total
> count is.
>
> An example invocation could be:
>
> ```sh
> $ ./a.out amd64
> 01. <package name> <number of files>
> 02. <package name> <number of files>
> ...
> 10. <package name> <number of files>
> ```
>
> You can use any language, library, or runtime environment you wish, with two caveats:
>
> 1. try to follow best practices – e.g. tests – and to write idiomatic code
> 2. we will probably need to run the tool to evaluate your work
>
> The focus is not to write the perfect code, but to demonstrate how you
> approach a problem and how you organize your work.
>
> **The Documentation**:
>
> The second half of the project is a final report. It should journal the work
> done, cover the technical decisions made, recount any obstacles, outline
> limitations discovered, etc.

# Report

## Journal

I chose Python because it's easy to use (both writing and reading it) and has everything needed for the task. I tried first using only the standard library, wary of the complexities that might come with adding a virtual environment and dependencies, but I later changed my mind, knowing my audience is technically savvy and could likely handle whatever issues might come up. I used Make to (hopefully) simplify the setup process.

The description reminded me of an ETL process, so I began by creating utility functions to perform the actions described.

For fetching, I used `argparse` to handle basic input validation and `requests` to get the corresponding file. Given the small file size, I handled everything in memory, but for larger files, streaming  would become necessary at some point to avoid performance issues.

For parsing, I used a series of splits to break the contents down into lines and then into collections of files, each linked to one or more associated packages. For counting, I used `Counter` to count each file, incrementing the count for each associated package.

For output, I used `most_common` to get the top packages and `enumerate` to loop through and print each one. I created a utility function using running maximums to get the max widths (character lengths) for both the package names and the file counts and used those values with f-strings to print the results with columns aligned, like those shown in the example invocation.

Total time: 6 hours.

## Obstacles

The documentation was by far the biggest challenge. I'm okay with writing documentation in general, but explicitly stating my decision-making process is something new, and given the context, I'm pretty anxious about getting it all "right". Formatting was another similar issue. The term "final report" seems to be widely used, but there doesn't seem to be any standard-ish way of doing it. The guides I _could_ find offered essentially conflicting information on both the writing and formatting.

Other issues were small by comparison. The Debian wiki had obsolete information about the file format, which initially caused confusion until I realized it was simply outdated. Mocking and testing network resources also took longer than expected.
