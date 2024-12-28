# Task

> The first half of the project is writing a program. It should fetch the
> relevant “Contents” index from a Debian mirror for the particular
> architecture (e.g. arm64) passed as an argument, and then it must parse the
> file and output the 10 packages with the most associations and what the total
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
> The Documentation:
>
> The second half of the project is a final report. It should journal the work
> done, cover the technical decisions made, recount any obstacles, outline
> limitations discovered, etc.

# Journal

I chose Python because its readable, familiar, and has everything needed for
the task. The project reminded me of an ETL process so I began by creating a
sequence of utility functions to perform the actions described:

```mermaid
flowchart LR
id[(Contents.gz)] -- fetch --> contents
contents -- parse --> counts
counts -- show --> output
```

For fetching, I used `requests` because it's generally faster and easier than
using `urlib.request`. I prepared the file working in memory and performance
was fine given the small size, but for larger files, streaming would become
necessary to avoid memory issues.

For parsing, I used a series of splits to break the object down into lines and
then into collections of files and packages, with each file being associated
with one or more packages. For counting, I used `collections.Counter` because
it performs as well (sometimes better) than a hash table and its easier to work
with.

For output, I used `most_common` to get the top N results (default=10) and
`enumerate` to loop through and print each one. I added a utility function
using running maximums to get the max widths for each column and used those
values with f-strings to print the results with columns aligned.

For main functionality I used `argparse` to handle basic validation and print
"usage" information on error. I wrapped everything in a main function and
called it at the end.

Total time: 6 hours.

# Obstacles

The documentation was by far the biggest obstacle. I'm okay with writing
documentation in general, but explicitly stating my decision-making process is
something new and I'm admittedly anxious about doing it all "right". Formatting
was another issue. The term "final report" seems to be a widely used term but
there doesn't seem to be any standard-ish way of doing it. The guides I could
find offered essentially conflicting information about both the writing itself
and the formatting.

Other issues were small by comparison. Mocking and testing network resources
took longer than expected. The Debian wiki also had some misleading information
about the Contents format, which threw me off until realizing it was outdated.
