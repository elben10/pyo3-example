from typing import Any, Dict

from setuptools_rust import Binding, RustExtension


def build(config: Dict[str, Any]) -> None:
    config["rust_extensions"] = [RustExtension("example._internal", binding=Binding.PyO3, debug=True)]
