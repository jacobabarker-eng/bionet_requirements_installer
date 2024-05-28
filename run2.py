#!/usr/bin/env python3

import subprocess

filenames = [
    'scripts/install_NVM' , 
    'scripts/install_nodeJS', 
    'scripts/install_yarn', 
]

# Read the commands from each file and execute them one at a time
for filename in filenames:
    with open(filename, 'r') as file:
        commands = file.readlines()

    # Execute each command one at a time
    for command in commands:
        command = command.strip()  # Remove leading/trailing whitespace
        if command:  # Ensure the command is not empty
            try:
                # Run the command and save the output to a file
                result = subprocess.run(command, shell=True, capture_output=True, text=True)
                result.check_returncode()  # Raise an error if the command failed

                # Print the command and its output
                # print(f"jacob@PC1024:~/491/project_loader$ {command}")
                # print(result.stdout)
                
                # Save the output to output.txt
                with open('output.txt', 'a') as output_file:
                    output_file.write(f"jacob@PC1024:~/491/project_loader$ {command}\n")
                    output_file.write(result.stdout if result.stdout else 'none\n')

            except subprocess.CalledProcessError as e:
                # Print and log the error if the command fails
                # print(f"Command failed: {command}")
                # print(e.stderr)
                with open('output.txt', 'a') as output_file:
                    output_file.write(f"Command failed: {command}\n")
                    output_file.write(e.stderr if e.stderr else 'none\n')

# Print a message indicating where the output has been saved
print("Output has been saved to output.txt")
