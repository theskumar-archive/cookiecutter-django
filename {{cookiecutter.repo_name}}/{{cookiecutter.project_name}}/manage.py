#!/usr/bin/env python
import os
import sys
import dotenv

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{cookiecutter.project_name}}.config.settings")
    os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

    dotenv.read_dotenv()

    from configurations.management import execute_from_command_line

    execute_from_command_line(sys.argv)
