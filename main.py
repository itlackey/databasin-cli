
import click
import inquirer
from pprint import pprint
from src.users import list_users

@click.group()
def cli():
    pass

@cli.command(name="test")
def test():
    questions = [
    inquirer.Text("name", message="What's your name?"),
    inquirer.Text("surname", message="What's your surname, {name}?"),
    inquirer.Text(
        "phone",
        message="What's your phone number"
        ),
    ]
    answers = inquirer.prompt(questions)
    pprint(answers)


@cli.group(name="users")
def users():
    pass

@users.command(name="list")
def users_list_command():
    list_users()


if __name__ == '__main__':
    cli()
