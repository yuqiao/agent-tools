"""Command line interface for agent tools."""

import click


@click.command()
def cli():
    """CLI entry point for agent tools."""
    click.echo("Agent tools CLI")