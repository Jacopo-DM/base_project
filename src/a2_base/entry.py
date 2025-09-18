"""A basic script that has a few different things which should show up in the docs.

Examples
--------
>>> 1 + 1

References
----------
    [1]

Todo
----
    - [ ] Nothing

"""

# Standard library
from pathlib import Path

# Third-party libraries
from rich.console import Console
from rich.traceback import install

# Local libraries
# Global constants
# Global functions
# Warning Control
# Type Checking
# Type Aliases

# --- DATA SETUP ---
SCRIPT_NAME = __file__.split("/")[-1][:-3]
CWD = Path.cwd()
DATA = CWD / "__data__"
DATA.mkdir(exist_ok=True)

# --- TERMINAL OUTPUT SETUP ---
install(show_locals=True)
console = Console()


class TestAutoGen:
    """Class to test auto-generation of docstrings."""

    def __init__(self) -> None:
        """Initialize the TestAutoGen class."""

    @staticmethod
    def add(x: int, y: int) -> int:
        """
        Add two numbers.

        Parameters
        ----------
        x
            A number.
        y
            Another number.

        Returns
        -------
            The total from the addition of two numbers
        """
        return x + y


def main() -> None:
    """Entry point."""
    return


if __name__ == "__main__":
    main()
