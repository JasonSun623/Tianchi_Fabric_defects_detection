from .registry import DATASETS
from .xml_style import XMLDataset


@DATASETS.register_module
class VOCDataset(XMLDataset):

    #CLASSES = ('aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car',
    #           'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse',
    #           'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train',
    #           'tvmonitor')
    CLASSES = ('Rebar',)
    def __init__(self, **kwargs):
        super(VOCDataset, self).__init__(**kwargs)
        if 'VOC2007' in self.img_prefix:
            self.year = 2007
        elif 'VOC2012' in self.img_prefix:
            self.year = 2012
        elif 'VOC2019' in self.img_prefix:
            self.year = 2019
        else:
            raise ValueError('Cannot infer dataset year from img_prefix')
