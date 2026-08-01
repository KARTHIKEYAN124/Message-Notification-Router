from pathlib import Path
import runpy


if __name__ == "__main__":
    code_main = Path(__file__).resolve().parent / "code" / "main.py"
    runpy.run_path(str(code_main), run_name="__main__")
