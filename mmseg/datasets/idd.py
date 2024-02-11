from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class ExampleDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('road', 'drivable fallback','sidewalk'),
        palette=[128, 64, 128], [244, 35, 232],[0, 0, 142])

    def __init__(self, aeg1, arg2):
        pass
