import os
import subprocess
import importlib


def download_file(url, filename):
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        subprocess.run(["wget", "-q", url, "-O", filename])
    else:
        print(f"{filename} already exists.")


def install_package(package_name, version=None, git_url=None, pre=False, upgrade=False):
    try:
        importlib.import_module(package_name)
        print(f"{package_name} is already installed.")
    except ImportError:
        print(f"Installing {package_name}...")
        cmd = ["pip", "install"]
        if pre:
            cmd.append("--pre")
        if upgrade:
            cmd.append("-U")
        if git_url:
            cmd.extend(["-qq", git_url])
        elif version:
            cmd.extend(["-q", f"{package_name}=={version}"])
        else:
            cmd.extend(["-q", package_name])
        subprocess.run(cmd)


def install_dependencies(dependencies):
    for dependency in dependencies:
        if 'type' in dependency and dependency['type'] == 'file':
            print(f"Installing {dependency['filename']}...")
            download_file(dependency['url'], dependency['filename'])
        elif 'type' in dependency and dependency['type'] == 'package':
            print(f"Installing {dependency['name']}...")
            install_package(dependency['name'], dependency.get('version'), dependency.get('git_url'), dependency.get('pre', False), dependency.get('upgrade', False))
