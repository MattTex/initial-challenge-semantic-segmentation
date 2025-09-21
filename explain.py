import torch
import torchvision
from pathlib import Path
import numpy as np
from pytorch_grad_cam import GradCAM
from pytorch_grad_cam.utils.image import show_cam_on_image
from models import get_unet

# --- CONFIGURAÇÕES ---
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
checkpoint_path = Path("checkpoints/best_model.pth")

# --- CARREGAR MODELO ---
model = get_unet().to(device)
if not checkpoint_path.exists():
    raise FileNotFoundError(
        f"Checkpoint não encontrado em: {checkpoint_path}\n"
        "➡️ Rode o treino e salve o modelo antes de executar o explain."
    )
model.load_state_dict(torch.load(checkpoint_path, map_location=device))
model.eval()

# --- PREPARAR INPUT ---
# Substitua pelas suas imagens reais!
# img_tensor: Tensor [B, C, H, W], normalizado para o modelo (ex.: [0,1])
# rgb_image : Numpy [H, W, 3], normalizado [0,1] para show_cam_on_image
# Exemplo de placeholders:
# img_tensor = torch.rand(1, 3, 256, 256).to(device)  # exemplo fake
# rgb_image = np.random.rand(256, 256, 3).astype(np.float32)

# 🚨 INSIRA AQUI SEUS DADOS REAIS
img_tensor = img_tensor.to(device)       # já fornecido pelo seu pipeline
rgb_image = np.clip(rgb_image, 0, 1)    # garante [0,1] para show_cam_on_image

# --- CONFIGURAR CAM ---
# Se o seu UNet tem encoder como nn.ModuleList, pegue a última camada
target_layer = model.encoder[-1]

cam = GradCAM(model=model, target_layers=[
              target_layer], use_cuda=device.type == "cuda")
grayscale_cam = cam(input_tensor=img_tensor)[0, :]  # [H, W]

# --- VISUALIZAÇÃO ---
visualization = show_cam_on_image(rgb_image, grayscale_cam, use_rgb=True)

# Converter para tensor (C,H,W) e salvar
visualization_tensor = torch.tensor(visualization).permute(2, 0, 1)
Path("outputs").mkdir(exist_ok=True)
torchvision.utils.save_image(
    visualization_tensor, "outputs/cam_visualization.png")

print("✅ Grad-CAM salvo em: outputs/cam_visualization.png")
