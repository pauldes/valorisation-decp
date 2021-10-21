import argparse

from src import functions

__version__ = "0.1"

def get_parser():
    """
    Creates a new argument parser.
    """
    parser = argparse.ArgumentParser()
    version = '%(prog)s ' + __version__
    parser.add_argument('--version', '-v', action='version', version=version, help="print version and exits")
    subparser = parser.add_subparsers(dest='command')
    download = subparser.add_parser('download', help="download last version of the dataset to disk")
    download.add_argument("--rows", required=False, help="rows to download", type=int)
    load = subparser.add_parser('load', help="print a sample of the dataset and its shape")
    load.add_argument("--rows", required=False, help="rows to load", type=int)
    web = subparser.add_parser('web', help="run the reporting web app")
    return parser

def main(args=None):
    """ Main entry point.
    
    Args:
        args : list of arguments as if they were input in the command line.
    """
    parser = get_parser()
    args = parser.parse_args(args)
    if args.command == "download":
        functions.download_data_to_disk(n_rows=args.rows)
    elif args.command == "load":
        functions.print_data_shape_and_sample(n_rows=args.rows)
    elif args.command == "web":
        functions.run_web_app()

if __name__ == '__main__':
    main()