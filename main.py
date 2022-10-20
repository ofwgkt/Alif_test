import argparse

if name == 'main':

    parser = argparse.ArgumentParser(description='Product list')
    parser.add_argument('-f', required=True, help='File name')
    parser.add_argument('-a', required=True, help='Action name: 1) add 2) edit 3) delete 4) total')

    args = parser.parse_args()
    file_name = args.f
    action = args.a
