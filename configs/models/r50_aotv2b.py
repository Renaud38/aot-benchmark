from .default import DefaultModelConfig


class ModelConfig(DefaultModelConfig):
    def __init__(self):
        super().__init__()
        self.MODEL_NAME = 'R50_AOTv2B'
        self.MODEL_VOS = 'aotv2'

        self.MODEL_ENCODER = 'resnet50'
        self.MODEL_ENCODER_DIM = [256, 512, 1024, 1024]  # 4x, 8x, 16x, 16x

        self.MODEL_LSTT_NUM = 3
