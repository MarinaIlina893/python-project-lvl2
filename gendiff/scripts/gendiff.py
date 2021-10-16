from gendiff.generate_diff import generate_diff
import argparse


def main():
    parser = argparse.ArgumentParser('gendiff', description='Generate diff ')
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
