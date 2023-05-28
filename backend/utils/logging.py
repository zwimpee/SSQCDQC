import os
from typing import Any, Dict
from qiskit import Aer as qiskit_aer
class SSQCLogger(qiskit_aer.backends.aer_simulator.logger):

    def __init__(self, log_dir: str = os.path.abspath(os.path.curdir), **kwargs: Dict[str, Any]):
        super(SSQCLogger, self).__init__(**kwargs)
        self.log_dir = log_dir

    def __call__(self, *args, **kwargs):
        return self.log_dir