
"""Interface module for high level application."""

from .inference import StochasticVBOptimizer
from .inference import SVAEStochasticVBOptimizer

from .parallel import parallel

from .utils import collect_stats
