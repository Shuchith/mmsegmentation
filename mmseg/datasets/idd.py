from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


@DATASETS.register_module()
class iddDataset(BaseSegDataset):

    METAINFO = dict(
        classes=('road','sidewalk', 'drivable fallback'),
        palette=[[128, 64, 128], [244, 35, 232],[0, 0, 142]])

    def __init__(self,
                 img_suffix='_leftImg8bit.png',
                 seg_map_suffix='_road_mask.png',
                 **kwargs) -> None:
        super().__init__(
            img_suffix=img_suffix, seg_map_suffix=seg_map_suffix, **kwargs)
