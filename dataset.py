# Preparação do dataset e tiles
import torch
from torch.utils.data import Dataset
import rasterio
import numpy as np


class RunwayDataset(Dataset):
    def __init__(self, tile_paths, mask_paths, transform=None):
        self.tiles = tile_paths
        self.masks = mask_paths
        self.transform = transform

    def __len__(self):
        return len(self.tiles)

    def __getitem__(self, idx):
        img = rasterio.open(self.tiles[idx]).read().astype('float32')
        mask = rasterio.open(self.masks[idx]).read(1).astype('uint8')
        # normalize if not done
        img = (img - img.min()) / (img.max() - img.min() + 1e-6)
        sample = {'image': img, 'mask': mask}
        if self.transform:
            sample = self.transform(**sample)
        # Rearrange for torch: C,H,W
        image = torch.tensor(sample['image']).float()
        mask = torch.tensor(sample['mask'])[None, :, :].float()
        return image, mask
# Note: Ensure that tile_paths and mask_paths are aligned lists of file paths.
# You may want to add data augmentation/transforms as needed.
