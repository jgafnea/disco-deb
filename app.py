import argparse
import gzip
from collections import Counter

import requests


def get_contents(arch: str) -> str:
    """Get contents (contents of Contents.gz) of given architecture."""
    BASE_URL = "https://deb.debian.org/debian/dists/stable/main"
    url = f"{BASE_URL}/Contents-{arch}.gz"
    try:
        response = requests.get(url)
        response.raise_for_status()
        contents = gzip.decompress(response.content).decode("utf-8")
        return contents
    except Exception:
        print(f"Error fetching url: {url}")
        return ""


def get_counts(contents: str) -> Counter:
    """Get file counts of each package."""
    counts = Counter()
    # If no data, return empty counter.
    if contents == "":
        return counts
    # Otherwise, parse the data and count packages.
    for line in contents.splitlines():
        try:
            # bin/file packageA,packageB,packageC
            _, packages = line.rsplit(maxsplit=1)
            for package in packages.split(","):
                counts[package] += 1
        except ValueError:
            print(f"Error parsing line: {line}")
            continue
    return counts


def show_top(counts: Counter, number: int = 10) -> None:
    """Show top packages by file count."""
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
