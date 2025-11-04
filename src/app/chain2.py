"""Another sample chain implementation."""


def process_chain(input_data):
    """Process data through the second chain."""
    print(f"Processing in chain2: {input_data}")
    return input_data + "_processed"