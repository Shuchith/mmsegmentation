from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class iddDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('road','sidewalk', 'drivable fallback','background'),
        palette=[[0, 255,0], [255,0,0],[0, 0,255],[0,0,0]])

    def __init__(self,
                 img_suffix='_leftImg8bit.png',
                 seg_map_suffix='_gtFine_labelTrainIds.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
