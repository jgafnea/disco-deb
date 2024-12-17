import argparse
import gzip
from collections import Counter

import requests


def get_contents(arch: str) -> str:
    BASE_URL = "https://deb.debian.org/debian/dists/stable/main"
    url = f"{BASE_URL}/Contents-{arch}.gz"
    response = requests.get(url)
    response.raise_for_status()

    contents_ = gzip.decompress(response.content).decode("utf-8")
    return contents_


def get_counts(contents: str) -> Counter:
    counts = Counter()
    for line in contents.splitlines():
        try:
            # bin/file packageA,packageB,packageC
            _, packages = line.rsplit(maxsplit=1)
            for package in packages.split(","):
                counts[package] += 1
        except ValueError:
            print("Error parsing line:\n", line)
            continue
    return counts


def show_top(counts: Counter, number: int = 10) -> None:
    top = counts.most_common(number)
    for i, (package, count) in enumerate(top, start=1):
        # Hacky solution to align columns with hardcoded widths.
        print(f"{i:02d}. {package:<30}{count:>10}")


def main() -> None:
    CHOICES = (
        "all",
        "amd64",
        "arm64",
        "armel",
        "armhf",
        "i386",
        "mips64el",
        "mipsel",
        "ppc64el",
        "s390x",
    )
    parser = argparse.ArgumentParser()
    parser.add_argument("arch", choices=CHOICES)
    args = parser.parse_args()
    try:
        contents = get_contents(args.arch)
        counts = get_counts(contents)
        show_top(counts)
    except Exception as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
