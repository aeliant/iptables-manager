"""Chain model definition."""

class Chain:
    """Chain model."""

    table = None
    name = None
    policy = None
    packet_counter = None
    byte_counter = None
    ipv6 = False
    rules = []

    def __init__(self, table, name, policy, packet_counter, byte_counter, ipv6):
        """Create a chain object."""
        self.table = table
        self.name = name
        self.policy = policy
        self.packet_counter = packet_counter
        self.byte_counter = byte_counter
        self.ipv6 = ipv6

    def __repr__(self):
        """String representation of the chain."""
        return f'<Chain name="{self.name}">'
