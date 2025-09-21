# Treinamento do modelo
from sklearn import metrics
import torch
from torch.utils.data import DataLoader
from tqdm import tqdm
from pathlib import Path
from dataset import RunwayDataset
from models import get_unet
import wandb
from sklearn.metrics import f1_score, jaccard_score
import numpy as np

wandb.init(project="runway-segmentation",
           config={"lr": 1e-4, "batch_size": 16})


def compute_metrics(preds, masks):
    preds_bin = (preds > 0).astype(np.uint8)
    return {
        "iou": jaccard_score(masks.flatten(), preds_bin.flatten()),
        "f1": f1_score(masks.flatten(), preds_bin.flatten())
    }


def main():
    model = get_unet().cuda()
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    criterion = torch.nn.BCEWithLogitsLoss()

    tiles_dir = Path("data/tiles")
    masks_dir = Path("data/masks")

    train_tiles = sorted(list(tiles_dir.glob("*.tif")))
    train_masks = sorted(list(masks_dir.glob("*.tif")))

    train_dataset = RunwayDataset(train_tiles, train_masks, transform=None)
    print(len(train_tiles), len(train_masks))

    train_loader = DataLoader(train_dataset,
                              batch_size=16,
                              shuffle=True,
                              num_workers=4,   # agora pode usar multiprocessing
                              pin_memory=True)

    for epoch in range(1, 51):
        model.train()
        all_preds = []
        all_masks = []

        for imgs, masks in tqdm(train_loader):
            imgs, masks = imgs.cuda(), masks.cuda()
            preds = model(imgs)
            loss = criterion(preds, masks)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            wandb.log({"loss": loss.item()})
            wandb.log({"predictions": [wandb.Image(preds[0].cpu())]})
            # para métricas – traz para CPU e numpy
        all_preds.append(preds.detach().cpu().numpy())
        all_masks.append(masks.cpu().numpy())

    # depois da época
    all_preds = np.concatenate(all_preds)
    all_masks = np.concatenate(all_masks)
    metrics = compute_metrics(all_preds, all_masks)
    wandb.log(metrics)
    print(f"Epoch {epoch} finished.")


if __name__ == "__main__":
    main()

    # validação e salvar checkpoint
