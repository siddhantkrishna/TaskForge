import argparse

def create_parser():
    parser = argparse.ArgumentParser(description="TaskForge CLI Task Manager")
    subparsers = parser.add_subparsers(dest="command")
    return parser, subparsers
