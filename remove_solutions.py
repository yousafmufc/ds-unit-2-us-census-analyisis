import click
import json


@click.command()
@click.argument('input', type=click.File('rb'))
@click.option(
    '-n', '--name', type=str, help="Name of the generated notebook",
    required=True)
def main(input, name):
    original = json.load(input)
    found_solution = False
    new_cells = []
    for cell in original['cells']:
        if 'Solution:' in "".join(cell['source']).strip():
            found_solution = True

        if not found_solution:
            new_cells.append(cell)

        if '(END SOLUTION)' in "".join(cell['source']).strip():
            found_solution = False

    original['cells'] = new_cells
    with open(name, 'w') as fp:
        fp.write(json.dumps(original))


if __name__ == '__main__':
    main()
