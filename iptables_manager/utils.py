"""Utils functions definition."""
from argparse import ArgumentParser


def iptables_arg_parser():
    parser = ArgumentParser()

    # Append to chain
    parser.add_argument('--append', '-A', type=str, nargs='*')
    # Insert in chain as rulenum
    parser.add_argument('--insert', '-I', type=str, nargs='*', dest='rulenum')
    # zero counters in chain or all chains
    parser.add_argument('--zero', '-Z', type=str, nargs='*')
    # source specifications
    parser.add_argument('--source', '-s', type=str, nargs='*')
    # destination specifications
    parser.add_argument('--destination', '-d', type=str, nargs='*')
    # input network interface
    parser.add_argument('--input-interface', '-i', type=str, nargs='*',
                        dest='in_interface')
    # output network interface
    parser.add_argument('--output-interface', '-o', type=str,
                        dest='out_interface', nargs='*')
    # target for rule (may load target extension)
    parser.add_argument('--jump', '-j', type=str, dest='target', nargs='*')
    # change chain name (moving any reference)
    # TODO: Keep ?
    parser.add_argument('--rename-chain', '-E', nargs='*', type=str)
    # protocol: by number or name, eg. tcp
    parser.add_argument('--protocol', '-p', type=str, nargs='*')

    # matches for addresses with a source of type <type>
    #parser.add_argument('--src-type', type=str, nargs='*')
    # matches for addresses with a destination of type <type>
    #parser.add_argument('--dst-type', type=str, nargs='*')

    # extended match
    #parser.add_argument('--match', '-m', type=str, nargs='*')

    return parser
