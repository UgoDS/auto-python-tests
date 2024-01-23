from dataclasses import dataclass


@dataclass
class FunctionInfos:
    module_name: str = None
    module_path: str = None
    function: function = None
