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
    download.add_argument("--consolidated", required=False, help="download consolidated data (.json from data.gouv.fr)", action="store_true")
    download.add_argument("--augmented", required=False, help="download augmented data (.csv from economie.gouv.fr)", action="store_true")
    audit = subparser.add_parser('audit', help="audit data quality and store results")
    audit.add_argument("--rows", required=False, help="rows to audit quality for", type=int)
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
        if args.consolidated:
            functions.download_consolidated_data_schema_to_disk()
            functions.download_consolidated_data_to_disk()
        if args.augmented:
            functions.download_augmented_data_to_disk(n_rows=args.rows)
        if not args.consolidated and not args.augmented:
            print("Neither --consolidated nor --augmented was passed. Nothing will be downloaded.")
    elif args.command == "audit":
        functions.audit_consolidated_data_quality(n_rows=args.rows)
    elif args.command == "web":
        functions.run_web_app()

if __name__ == '__main__':
    main()