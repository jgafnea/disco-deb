# Report

I started by breaking the project down into three functions, each performing one of the tasks described in the instructions: fetching, parsing, and output.

For fetching, I used `requests` because it generally makes HTTP things easier. Processing is done in memory which works fine for the small file sizes but would need something with streaming or chunking to help manage memory for significantly larger file sizes.

For parsing, I used a series of splits (`splitlines`, `rsplit`, and `split`) to break the contents down into lines and then into collections of files and associated packages. One challenge was mentally parsing lines like

```
bin/example libdevel/packageA,libdevel/packageB
```

which seemed "backward". Writing the parsing logic and adding explicit variables helped clarify the formatting and make it easier to follow.

For counting, I used `Counter` because it performs as well as a hash table but it's easier to use and read, especially coming back to it months later.

For printing, I used `most_common` to get the 10 top packages (optionally accepting a different number) and `enumerate` to go over those and print each one. I added a ~~hacky fix~~ heuristic solution with f-strings to format columns neatly.

For parsing arguments, I used `argparse` because it handles basic validation and shows accepted arguments on usage.

For main functionality, I wrapped everything in `main()` and then called that at the end.

For testing, I didn't go crazy with edge cases, just tested the things I wanted to make sure would work as expected, namely the parsing of `Contents`, getting accurate numbers, and handling malformatted lines.

This documentation was, by far, the hardest part of the assignment. I'm okay with code, testing, and documentation in general, but framing my thoughts explicitly was new and I'm rather nervous about doing everything "wrong." I tried to "think out loud" and translate that into written form, I hope the result conveys the what and why effectively. 🤞
