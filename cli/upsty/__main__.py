from argparse import ArgumentParser
from upsty.lib import upload_file

def main():
    parser = ArgumentParser()
    parser.add_argument('filepath', help='Path to file for upload.')
    parser.add_argument('filename', help='Filename to download as.')
    args = parser.parse_args()
    content = upload_file(args.filepath, args.filename).decode('utf-8')
    print(content)

if __name__ == "__main__":
    main()
