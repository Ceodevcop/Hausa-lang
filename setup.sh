#!/bin/bash

# Print a welcome message
echo "Welcome to the Hausa Programming Language Setup!"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install Python3 and try again."
    exit 1
fi

# Install dependencies
echo "Installing dependencies..."
pip install ply

# Run the Hausa program
echo "Running the Hausa program..."
python3 cli.py examples/hello.hausa

# Print a completion message
echo "Setup complete!"
