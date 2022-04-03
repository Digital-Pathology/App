
from unified_image_reader import Image

from model_manager_for_web_app import ModelManager

from . import status_lock


class DiagnosisRunner:
    """ Handles thread-safe diagnosis of images by models """
    def __init__(self, model_name) -> None:
        """ model_name is a model handled by ModelManagerForWebApp"""
        self.status_lock = status_lock.StatusLock()
        self.model_name = model_name
        self.model = ModelManager().load_model(self.model_name)
        self._status = {
            "status": "initialized",
            "model_name": self.model_name
        }

    def make_region_stream(self, filepath):
        """ iterates over regions in an image and updates status to reflect progress """
        img = Image(filepath)
        self.update_status(
            status="processing_regions",
            filepath=filepath,
            current_region=-1,
            total_regions=Image(filepath).number_of_regions()
        )
        for region_num, region in enumerate(img):
            self.update_status(current_region=region_num)
            yield region

    def do_diagnosis(self, filepath):
        """ converts filepath to region stream, then adds diagnosis to status """
        region_stream = self.make_region_stream(filepath)
        diagnosis = self.model.diagnose(region_stream)
        self.update_status(diagnosis=diagnosis)

    def read_status(self):
        """ uses thread-safe locking for reading """
        with self.status_lock as permission:
            return self._status

    def update_status(self, **kwargs):
        """ uses thread-safe locking for writing """
        with self.status_lock as permission:
            for key, value in kwargs.items():
                self._status[key] = value
