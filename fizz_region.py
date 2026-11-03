"""Check whether a Canadian postal code is in a province where Fizz mobile is sold.

Fizz is offered in Quebec, Ontario, Manitoba, Alberta and British Columbia.
The first letter of a Canadian postal code identifies the province or territory,
so a simple lookup is enough for a first answer.

Usage:
    python fizz_region.py H2X 1Y4
"""

import re
import sys

# First letter of the postal code -> province or territory.
FIRST_LETTER = {
    "A": "Newfoundland and Labrador",
    "B": "Nova Scotia",
    "C": "Prince Edward Island",
    "E": "New Brunswick",
    "G": "Quebec",
    "H": "Quebec",
    "J": "Quebec",
    "K": "Ontario",
    "L": "Ontario",
    "M": "Ontario",
    "N": "Ontario",
    "P": "Ontario",
    "R": "Manitoba",
    "S": "Saskatchewan",
    "T": "Alberta",
    "V": "British Columbia",
    "X": "Northwest Territories or Nunavut",
    "Y": "Yukon",
}

# Provinces where you can open a Fizz plan.
FIZZ_PROVINCES = {
    "Quebec",
    "Ontario",
    "Manitoba",
    "Alberta",
    "British Columbia",
}

POSTAL_RE = re.compile(r"^[ABCEGHJ-NPRSTVXY]\d[A-Z]\s?\d[A-Z]\d$")


def normalize(postal_code: str) -> str:
    """Upper-case the code and drop extra spaces, e.g. ' h2x1y4 ' -> 'H2X1Y4'."""
    return re.sub(r"\s+", "", postal_code).upper()


def province_of(postal_code: str) -> str:
    """Return the province or territory for a postal code, or raise ValueError."""
    code = normalize(postal_code)
    if not POSTAL_RE.match(code):
        raise ValueError(f"Not a valid Canadian postal code: {postal_code!r}")
    return FIRST_LETTER[code[0]]


def fizz_available(postal_code: str) -> bool:
    """True if the postal code is in a province where Fizz is sold."""
    return province_of(postal_code) in FIZZ_PROVINCES


def main(argv) -> int:
    if not argv:
        print("Usage: python fizz_region.py <postal code>")
        return 2
    code = " ".join(argv)
    try:
        province = province_of(code)
    except ValueError as err:
        print(err)
        return 2
    if province in FIZZ_PROVINCES:
        print(f"{province}: Fizz is sold here.")
        return 0
    print(f"{province}: Fizz is not sold here yet.")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
