import logging
import time
from contextlib import contextmanager
from pathlib import Path

def setup_logging(output_dir: str = "output"):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s | %(levelname)s | %(message)s",
                        handlers=[logging.FileHandler(Path(output_dir) / "execution.log"),
                                  logging.StreamHandler()
                                  ]
                        )

@contextmanager
def timer(name: str = "Process"):
    start = time.perf_counter()
    yield
    end = time.perf_counter()
    logging.info(f"{name} completed in {end - start:.4f} seconds")

def format_currency(value: float) -> str:
    return f"${value:,.2f}"