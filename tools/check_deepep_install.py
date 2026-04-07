import importlib
import sys


def check_module(name: str) -> bool:
    try:
        module = importlib.import_module(name)
    except Exception as exc:
        print(f"[FAIL] import {name}: {exc}")
        return False

    module_path = getattr(module, "__file__", None)
    module_pkg = getattr(module, "__path__", None)
    print(f"[OK] import {name}")
    if module_path is not None:
        print(f"  file: {module_path}")
    if module_pkg is not None:
        print(f"  path: {list(module_pkg)}")
    return True


def main() -> int:
    ok = True
    ok &= check_module("deep_ep")
    ok &= check_module("deep_ep_cpp")

    if ok:
        print("[PASS] DeepEP Python modules are visible in the current environment.")
        return 0

    print("[FAIL] DeepEP installation is incomplete.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
