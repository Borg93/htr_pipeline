from htr.processes.base_process import Process
from htr.processes.postprocess.simple_postprocessing import SimplePost
from htr.processes.preprocess.simple_binarize import SimpleBinarize


class ProcessFactory:
    def __init__(self):
        self.preprocessing = "preprocessing"
        self.postprocessing = "postprocessing"
        self.processes = {
            SimpleBinarize.__name__: SimpleBinarize,
            SimplePost.__name__: SimplePost,
            # Add more as needed
        }

    def register_custom_process(self, process_name, process_class):
        if not issubclass(process_class, Process):
            raise TypeError("process_class must be a subclass of Strategkky.")
        self.processes[process_name] = process_class

    def create(self, process_name, process_type):
        process_class = self.processes.get(process_name)

        if not process_class:
            available_process = ", ".join(self.processes.keys())
            raise ValueError(f"Invalid process name: {process_name}. Available processs: {available_process}")

        if process_class.process_type != process_type:
            raise ValueError(f"Process type mismatch: process {process_name} is not of type {process_type}")

        process = process_class()

        return process
