from execute import execute
from install_dependencies import install_dependencies

#https://colab.research.google.com/github/ShivamShrirao/diffusers/blob/main/examples/dreambooth/DreamBooth_Stable_Diffusion.ipynb
#https://github.com/ShivamShrirao/diffusers/tree/main/examples/dreambooth

# Get the GPU name and memory
execute("nvidia-smi --query-gpu=name,memory.total,memory.free --format=csv,noheader")

# Install dependencies
dependencies = [
    {'type': 'file', 'url': "https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py", 'filename': "train_dreambooth.py"},
    {'type': 'file', 'url': "https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py", 'filename': "convert_diffusers_to_original_stable_diffusion.py"},
    {'type': 'package', 'name': 'triton', 'git_url': 'git+https://github.com/ptillet/triton', 'pre': True, 'upgrade': True},
    {'type': 'package', 'name': 'diffusers', 'git_url': 'git+https://github.com/ShivamShrirao/diffusers'},
    {'type': 'package', 'name': 'accelerate'},
    {'type': 'package', 'name': 'transformers'},
    {'type': 'package', 'name': 'ftfy'},
    {'type': 'package', 'name': 'bitsandbytes', 'version': '0.35.0'},
    {'type': 'package', 'name': 'gradio'},
    {'type': 'package', 'name': 'natsort'},
    {'type': 'package', 'name': 'safetensors'},
    {'type': 'package', 'name': 'xformers'}
]

print("Installing dependencies...")
install_dependencies(dependencies)