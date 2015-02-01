#!/usr/bin/env python
import os
import sys


if __name__ == "__main__":
    if not os.path.exists('/tmp/mklkfifo'):
        os.system('mkfifo /tmp/mklkfifo')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)

