"""IP Table Rule model."""

class Rule:
    """iptable rule model."""

    chain = None
    destination_network = None
    source_network = None
    input_interface = None
    output_interface = None
    rulenum = None
    target = None
    protocol = None

    def __init__(self, args):
        """Create a rule object from given argument."""
        self.destination_network = args.destination
        self.source_network = args.source
        self.input_interface = args.in_interface
        self.output_interface = args.out_interface
        self.rulenum = args.rulenum
        self.target = args.target
        self.protocol = args.protocol

    def __repr__(self):
        """String representation of a rule object."""
        return f'<Rule chain="{self.chain}">'
