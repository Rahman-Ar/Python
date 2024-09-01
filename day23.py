#Command-Line Interfaces
import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument(
    'filename', 
    type=str, 
    help='Name of the file to process'
)

parser.add_argument(
    '-v', '--verbose', 
    action='store_true', 
    help='Increase output verbosity'
)
args = parser.parse_args()
if args.verbose:
    print(f'Verbosity turned on. Processing file: {args.filename}')
else:
    print(f'Processing file: {args.filename}')
