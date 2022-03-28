
import random

from model_manager_for_web_app import ManagedModel

class RandomModel:
    def diagnose_region(self, *args):
        return bool(random.randint(0,2))

class WrappedModel(ManagedModel):
    def __init__(self, model):
        self.model = model # can aggregate another model easily
    def diagnose(self, region_stream):
        region_level_diagnoses = []
        for region in region_stream:
            region_level_diagnoses.append(
                self.model.diagnose_region(region)
            )
        return sum(region_level_diagnoses) / len(region_level_diagnoses)