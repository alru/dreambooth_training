import subprocess


def execute(command, print_output=True):
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )
    output = result.stdout.decode('utf-8').strip()
    if print_output:
        print(output)
    return output
