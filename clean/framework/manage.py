#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# 👉 THÊM ĐOẠN NÀY
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CLEAN_ROOT = os.path.dirname(CURRENT_DIR)
sys.path.append(CLEAN_ROOT)
# 👉 KẾT THÚC

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
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
