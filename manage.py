#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
<<<<<<< HEAD
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "empweb.settings")
=======
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webpage.settings")
>>>>>>> 6379c6184892de37ef80568f1903429f809e179e

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
