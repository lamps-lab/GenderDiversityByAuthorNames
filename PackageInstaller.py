import subprocess
import importlib.util
import sys


def install(package):
    if package in sys.modules:
        print(f"{package!r} already in sys.modules")
    elif (spec := importlib.util.find_spec(package)) is not None:
        # If you choose to perform the actual import ...
        module = importlib.util.module_from_spec(spec)
        sys.modules[package] = module
        spec.loader.exec_module(module)
        print(f"{package!r} has been imported")
    else:
        print(f"Can't find the {package!r} module. Installing {package!r}")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
