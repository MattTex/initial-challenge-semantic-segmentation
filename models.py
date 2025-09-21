# Definição de modelos (U-Net, SwinTransformer, etc.)
import segmentation_models_pytorch as smp


def get_unet(num_classes=1, encoder_name='resnet34', pretrained=True):

    model = smp.Unet(encoder_name=encoder_name, encoder_weights='imagenet' if pretrained else None,
                     in_channels=4, classes=num_classes, activation=None)
    return model


# Para transformer: encoder_name='timm-swin-base-patch4-window7-224' ou similar (dependendo de supprt de SMP)
