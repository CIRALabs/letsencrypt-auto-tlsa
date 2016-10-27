import argparse
import os

from cira.labs.leat.structs.Bunch import Bunch

def parse_args():
    argument_parser = argparse.ArgumentParser(prog="le-at")

    create_arguments(argument_parser)
    args = argument_parser.parse_args()
    print(args)
    args = args_to_bunch(args)
    print(args)

    return args

def create_arguments(parser):
    def add_positionals():
        parser.add_argument('domain')

    add_positionals()

def args_to_bunch(args):
    pass