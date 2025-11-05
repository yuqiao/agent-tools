from typer import Typer

app = Typer(help="agentic工具箱")

@app.command()
def generate(text: str):
    pass

