"""Nox sessions.

Author:     jmdm
Date:       2025-09-13
Py Ver:     3.12
OS:         macOS  Sequoia 15.3.1
Hardware:   M4 Pro
Status:     Completed ✅
"""

# Standard library
import shutil
from pathlib import Path

# Third-party libraries
import nox

# Local libraries
# Global constants
# Global functions
# Warning Control
# Type Checking
# Type Aliases

# --- NOX SETUP ---
nox.options.default_venv_backend = "uv"
package = "a2_base"
python_versions = ["3.12", "3.13"]

# @nox.session(python=python_versions)
# def tests(session: nox.Session) -> None:
#     """Run the test suite."""
#     session.run(
#         "uv",
#         "sync",
#         "--group",
#         "dev",
#         "--group",
#         "lint",
#         external=True,
#     )

#     session.install("pytest", "coverage", "pytest-mock")
#     session.install("-e", ".")
#     session.run("pytest", *session.posargs)


# @nox.session(name="pre-commit", python=python_versions[0])
# def precommit(session: nox.Session) -> None:
#     """Lint using pre-commit."""
#     args = session.posargs or [
#         "run",
#         "--all-files",
#         "--hook-stage=manual",
#         # "--show-diff-on-failure",
#     ]

#     session.run(
#         "uv",
#         "sync",
#         "--group",
#         "dev",
#         "--group",
#         "lint",
#         external=True,
#     )

#     session.run("pre-commit", *args, external=True)


@nox.session(python=python_versions[0])
def docs(session: nox.Session) -> None:
    """Build and serve the documentation with live reloading on file changes."""
    session.run(
        "uv",
        "sync",
        "--group",
        "docs",
        external=True,
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )

    build_dir = Path("docs", "_build")

    if build_dir.exists():
        shutil.rmtree(build_dir)

    args = session.posargs or ["--open-browser", "docs", "docs/_build"]
    session.run("sphinx-autobuild", *args)
