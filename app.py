import argparse
import gzip
from collections import Counter
from typing import Optional

import requests


def get_contents(arch: str) -> Optional[str]:
    """Get the contents for the specified architecture."""
    BASE_URL = "https://deb.debian.org/debian/dists/stable/main"

    url = f"{BASE_URL}/Contents-{arch}.gz"

    try:
        response = requests.get(url)
        response.raise_for_status()
        # response content > decompress > bytes > decode > string
        contents_ = gzip.decompress(response.content).decode("utf-8")
        return contents_

    except Exception:
        print(f"Error fetching url: {url}")
        return None


def get_counts(contents: Optional[str]) -> Counter:
    """Count the number of files associated with each package."""
    counts = Counter()

    if contents is None:
        return counts

    for line in contents.splitlines():
        try:
            # FILE      LOCATION
            # /bin/file packageA,packageB
            _, packages = line.rsplit(maxsplit=1)
            for package in packages.split(","):
                counts[package] += 1
        except ValueError:
            print(f"Error parsing line: {line}")
            continue

    return counts


def show_top(counts: Counter, number: int = 10) -> None:
    """Show the top N packages with the most associated files."""
    top = counts.most_common(number)

    def get_widths() -> tuple:
        """Get the max column widths using running max."""
        package_len, count_len = 0, 0
        for package, count in top:
            package_len = max(package_len, len(package))
            count_len = max(count_len, len(str(count)))
        return package_len, count_len

    package_len, count_len = get_widths()

    for i, (package, count) in enumerate(top, start=1):
        # Print column widths using maxes found above.
        print(f"{i:02d}. {package:<{package_len}}{count:>{count_len}}")


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
