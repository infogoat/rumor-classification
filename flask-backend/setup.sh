#!/bin/bash
echo "Creating virtual environment..."
python -m venv venv

echo "Activating virtual environment..."
source venv/Scripts/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete! Run the application with:"
echo "source venv/bin/activate && python app.py"
