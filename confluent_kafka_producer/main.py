from typing import Optional

import typer

__app_name__ = "confluent-kafka-producer"
__version__ = "0.1.0"

from confluent_kafka_producer.src.service import producer

app = typer.Typer()
app.add_typer(producer.app, name='producer')


def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()


@app.callback()
def main(version: Optional[bool] = typer.Option(
    None,
    "--version",
    "-v",
    help="Show the application's version and exit.",
    callback=_version_callback,
    is_eager=True,
)
) -> None:
    return


if __name__ == '__main__':
    app()
