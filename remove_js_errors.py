import click
import subprocess
import os

def find_and_remove_errors(filename):
    with open(filename, 'r') as file:
        code = file.read()

    temp_file = "temp.js"
    with open(temp_file, 'w') as temp:
        temp.write(code)

    node_command = f'node {temp_file}'
    process = subprocess.Popen(node_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    os.remove(temp_file)

    if stderr.strip():
        print("JavaScript error(s) found in the file. Deleting the file...")
        os.remove(filename)
        print(f"File '{filename}' deleted.")
    else:
        print("No errors found in the file.")

@click.command()
@click.argument('filename', type=click.Path(exists=True))
def main(filename):
    """
    A CLI app to delete the JavaScript file if errors are found.
    Please do not use :)
    """
    find_and_remove_errors(filename)

if __name__ == '__main__':
    main()