"""Parser definition."""
from .models import Table, Chain, Rule
from .utils import iptables_arg_parser

import subprocess
import re


TABLE_REGEX = re.compile(r'\*(\w+)\n')
CHAIN_REGEX = re.compile(r'\:(\D+)\s(\D+)\s\[(\d+)\:(\d+)\]\n')

def tables(ipv6=False):
    """List ipv4 or ipv6 tables."""
    tables = []
    command = 'ip6tables-save' if ipv6 else 'iptables-save'
    command_output = subprocess.check_output(command).decode()
    extracted = [_[1:] for _ in command_output.split('\n') if _.startswith('*')]

    return [Table(name=_) for _ in extracted]


def chains(table, ipv6=False):
    """List chains for the given ipv4 or ipv6 table."""
    command = 'ip6tables-save' if ipv6 else 'iptables-save'
    command = f'{command} -t {table.name}'.split(' ')
    command_output = subprocess.check_output(command).decode()
    extracted = [_ for _ in command_output.split('\n') if _.startswith(':')]
    extracted = [_[1:].split(' ') for _ in extracted]

    return [Chain(
        table=table,
        name=_[0],
        policy=_[1],
        packet_counter=int(_[2][1:].split(':')[0]),
        byte_counter=int(_[2][:-1].split(':')[1]),
        ipv6=ipv6
    ) for _ in extracted]

def rules(table, ipv6=False):
    """List rules for the given ipv4 or ipv6 table."""
    rules = []
    parser = iptables_arg_parser()
    command = 'ip6tables-save' if ipv6 else 'iptables-save'
    command = f'{command} -t {table.name}'.split(' ')
    command_output = subprocess.check_output(command).decode()
    extracted = [_ for _ in command_output.split('\n') if _.startswith('-')]

    for _rule in extracted:
        args = parser.parse_known_args(_rule.split())
        namespace = args[0]
        rules.append(Rule(namespace))

    return rules
