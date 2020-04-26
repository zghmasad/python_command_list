import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Echo your input')
    parser.add_argument('message',
                        help='Message to echo')

    parser.add_argument('--aaaa', '-a',
                        help='AAA a A',
                        action='store_true')
    parser.add_argument('--bbbb', '-b',
                        help='Do it twice',
                        action='store_false')

    parser.add_argument('--cccc', '-c',
                        help='Do it twice',
                        action='store')

    parser.add_argument('--dddd', '-d',
                        help='Do it twice',
                        action='store_const',
                        const='lll')

    args = parser.parse_args()

    print(args)

    print(args.message)
    if args.aaaa:
        print(args.message)

    if args.bbbb:
        print('this is the shit i told')

    if args.cccc:
        print(args.cccc)

    print(args.dddd)