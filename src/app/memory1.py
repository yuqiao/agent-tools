"""Sample memory implementation."""


class SimpleMemory:
    """Simple memory store."""
    
    def __init__(self):
        self.data = {}
    
    def set(self, key, value):
        """Set a memory value."""
        self.data[key] = value
    
    def get(self, key):
        """Get a memory value."""
        return self.data.get(key)