#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys
from threading import Thread

def start_react_server():
    """Start the React development server if not already running."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    react_project_directory = os.path.join(BASE_DIR, 'frontend')

    # Check if the React development server is already running
    try:
        subprocess.run(['npm', 'list', 'react-scripts', '-g'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("React development server is already running.")
    except subprocess.CalledProcessError:
        # Run npm install and npm run dev if not running
        subprocess.run(['npm', 'install'], cwd=react_project_directory, check=True)
        subprocess.run(['npm', 'run', 'build'], cwd=react_project_directory, check=True)
        subprocess.run(['npm', 'run', 'dev'], cwd=react_project_directory, check=True)

def main():
    """Run administrative tasks."""
    # Start the React development server in a separate thread
    react_thread = Thread(target=start_react_server)
    react_thread.start()

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    # Run the Django development server
    execute_from_command_line(sys.argv)

    # Wait for the React thread to finish before exiting
    react_thread.join()

if __name__ == '__main__':
    main()
