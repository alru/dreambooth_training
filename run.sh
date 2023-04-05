#!/bin/bash

venv_name="venv"
vert_path=$PWD/$venv_name

if [ ! -d "$vert_path" ]; then
    echo "Virtual environment will be created in this path: ${vert_path}"
    sleep 1
    #sudo apt-get update -y
    #sudo apt-get install -y python3-venv
    python3 -m venv $vert_path
fi

source "${vert_path}/bin/activate"
python --version

# Install dependencies
# Define your dependencies in the following format:
# "type:<file|package> url:<url> filename:<filename> name:<package_name> git_url:<git_url> version:<version> pre:<pre> upgrade:<upgrade>"
dependencies=(
    "type:file url:https://github.com/ShivamShrirao/diffusers/raw/main/examples/dreambooth/train_dreambooth.py filename:train_dreambooth.py"
    "type:file url:https://github.com/ShivamShrirao/diffusers/raw/main/scripts/convert_diffusers_to_original_stable_diffusion.py filename:convert_diffusers_to_original_stable_diffusion.py"
    "type:package name:triton git_url:git+https://github.com/ptillet/triton pre:true upgrade:true"
    "type:package name:diffusers git_url:git+https://github.com/ShivamShrirao/diffusers"
    "type:package name:accelerate"
    "type:package name:transformers"
    "type:package name:ftfy"
    "type:package name:bitsandbytes version:0.35.0"
    "type:package name:gradio"
    "type:package name:natsort"
    "type:package name:safetensors"
    "type:package name:xformers"
)

for dep in "${dependencies[@]}"; do
    # Parse the dependency properties
    properties=$(echo $dep | tr " " "\n")
    declare -A dep_props
    for prop in $properties; do
        IFS=":" read -ra key_value <<<"$prop"
        dep_props[${key_value[0]}]=${key_value[1]}
    done

    # Install packages or download files based on the type
    if [ "${dep_props[type]}" == "file" ]; then
        echo "Installing ${dep_props[filename]}..."
        if [ ! -f "${dep_props[filename]}" ]; then
            echo "Downloading ${dep_props[filename]}..."
            wget -q "${dep_props[url]}" -O "${dep_props[filename]}"
        else
            echo "${dep_props[filename]} already exists."
        fi
    elif [ "${dep_props[type]}" == "package" ]; then
        echo "Installing ${dep_props[name]}..."
        cmd="pip install"

        if [ "${dep_props[pre]}" == "true" ]; then
            cmd="$cmd --pre"
        fi

        if [ "${dep_props[upgrade]}" == "true" ]; then
            cmd="$cmd -U"
        fi

        if [ ! -z "${dep_props[git_url]}" ]; then
            cmd="$cmd -qq ${dep_props[git_url]}"
        elif [ ! -z "${dep_props[version]}" ]; then
            cmd="$cmd -q ${dep_props[name]}==${dep_props[version]}"
        else
            cmd="$cmd -q ${dep_props[name]}"
        fi

        eval $cmd
    fi
done

#pip install -r requirements.txt
python main.py "$@"