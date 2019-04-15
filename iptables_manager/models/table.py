"""Table model definition."""

class Table:
    """Table model."""

    name = None
    chains = None

    @property
    def rules(self):
        return [_.rules for _ in self.chains]

    def __init__(self, name):
        """Create a new table object."""
        self.name = name

    def __repr__(self):
        """String representation of a table."""
        return f'<Table name="{self.name}">'
