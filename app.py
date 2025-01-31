# Install required libraries if they are not already installed
!pip install -q diffusers transformers torch pillow gspread google-auth google-auth-oauthlib google-auth-httplib2

# Import necessary libraries
from diffusers import StableDiffusionInpaintPipeline
import torch
from PIL import Image
from google.colab import auth
import os
import gspread
from google.auth import default
from google.colab import drive

# Authenticate and mount Google Drive
auth.authenticate_user()
creds, _ = default()
gc = gspread.authorize(creds)

# Força a remontagem do Google Drive e limpa a pasta de cache
if os.path.exists('/content/drive'):
    drive.flush_and_unmount()
    print('Google Drive desmontado.')
drive.mount('/content/drive', force_remount=True)
print('Google Drive montado com sucesso!')

# Define input and output directories
INPUT_DIR = os.path.join('/content/drive/My Drive/input-logos')
OUTPUT_DIR = os.path.join('/content/drive/My Drive/output-logos')

# Create output directory if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Check if input directory exists
if not os.path.exists(INPUT_DIR):
    print(f"Erro: Diretório de entrada '{INPUT_DIR}' não encontrado.")
    os.makedirs(INPUT_DIR, exist_ok=True)
    print(f"Diretório de entrada '{INPUT_DIR}' criado. Adicione as imagens e execute novamente.")
else:
    # Initialize the inpainting pipeline
    device = "cuda" if torch.cuda.is_available() else "cpu"
    pipe = StableDiffusionInpaintPipeline.from_pretrained(
        "runwayml/stable-diffusion-inpainting",
        torch_dtype=torch.float16
    ).to(device)

    # Base prompt for logo generation
    BASE_PROMPT = (
        "The original image is a logo. Keep the style and composition intact, but make subtle creative variations."
    )

    # Function to process logos and generate 4 variations per logo
    def process_logos(input_dir, output_dir, base_prompt):
        for filename in os.listdir(input_dir):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                input_path = os.path.join(input_dir, filename)
                try:
                    print(f"Processando: {filename}")
                    init_image = Image.open(input_path).convert("RGB").resize((512, 512))  # Resize to a standard size
                    mask_image = Image.new("RGB", init_image.size, "white")  # Create a white mask

                    # Generate 4 variations of the logo
                    for i in range(4):
                        variation_prompt = f"{base_prompt} Variation {i + 1}: Add unique stylistic elements."
                        result = pipe(prompt=variation_prompt, image=init_image, mask_image=mask_image, num_inference_steps=50).images[0]
                        output_filename = f"{filename.split('.')[0]}_variation_{i + 1}.png"
                        output_path = os.path.join(output_dir, output_filename)
                        result.save(output_path)
                        print(f"Variação salva em: {output_path}")
                except Exception as e:
                    print(f"Erro ao processar {filename}: {e}")

    # Process the logos
    process_logos(INPUT_DIR, OUTPUT_DIR, BASE_PROMPT)