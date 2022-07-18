# `pyo3` integration with poetry
This repository is a small POC of how it's possible to use pyo3 together with poetry. It's also shown how to debug the extension modules in rust using vscode.

## Quickstart
It's extremely simple ensure that you've installed `rust` and `poetry`
1. `poetry install` - Install required dependencies and compile rust code
1. `poetry run python debug.py` - Use the compiled rust code

## Debugging
1. Update the python interpreter in .vscode/launch.json
1. Add breakpoint in the function `double`in src/lib.rs
1. Launch _(lldb) Launch_ in vscode debugger