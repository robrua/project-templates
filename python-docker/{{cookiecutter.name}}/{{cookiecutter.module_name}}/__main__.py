import click

from {{cookiecutter.module_name}} import __version__


@click.group(help="{{cookiecutter.cli_help}}")
@click.version_option(version=__version__)
def {{ cookiecutter.name.replace('-', '_') }}() -> None:
    pass


@{{ cookiecutter.name.replace('-', '_') }}.command(name="echo", help="Echos a message")
@click.argument("message", type=str)
@click.option(
    "-s/-n",
    "--shout/--no-shout",
    default=False,
    help="whether to shout the message  [default no shout]",
    show_default=False,
)
@click.option(
    "-r",
    "--repeat",
    default=1,
    help="how many times to repeat the message",
    show_default=True,
)
def echo(message: str, shout: bool = False, repeat: int = 1) -> None:
    if shout:
        message = message.upper()
    for _ in range(repeat):
        print(message)


if __name__ == "__main__":
    {{ cookiecutter.name.replace('-', '_') }}(prog_name="{{cookiecutter.cli_command}}")
