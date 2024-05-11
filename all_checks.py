#!/usr/bin/env
import os
def check_reboot():
    """returns True if the computer has a pending reboot."""
    return os.path.exist("/run/reboot-required")
def main():
    pass

main()
