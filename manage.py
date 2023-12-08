#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import subprocess
import sys


def main():
    """Run administrative tasks."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    # Assuming your ReactJS project is in the 'frontend' directory inside your Django project
    react_project_directory = os.path.join(BASE_DIR, 'frontend')
    
    subprocess.run(['npm', 'run', 'build'], cwd=react_project_directory, check=True)

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
