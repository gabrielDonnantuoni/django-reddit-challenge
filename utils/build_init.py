import sys
from pathlib import Path
import importlib

try:
    cc = importlib.import_module('case_converter').CaseConverter
except ModuleNotFoundError as err:
    print(f'\nModuleNotFoundError: {err}')
    print(
        'First you need to add case_converter to the same'
        ' package as this script.'
    )
    sys.exit(1)


def build_init(package_path: str) -> None:
    _package_path = Path(package_path)
    if _package_path.is_dir():
        modules = list(_package_path.glob('*.py'))
        init_path = _package_path.joinpath('__init__.py')
    else:
        print(
            f'{package_path} is not a directory.'
            'Please, call the the script with a package directory path.'
        )
        return

    with init_path.open('w') as file:
        def dict_with_pascal_and_snake(module: Path):
            without_suffix = module.stem
            return {
                'snake': without_suffix,
                'pascal': cc.snake_to_pascal(without_suffix),
            }

        modules = [
            dict_with_pascal_and_snake(module)
            for module in modules
            if module != init_path
        ]

        for module in modules:
            snake = module['snake']
            pascal = module['pascal']
            file.write(f'from .{snake} import {pascal}\n')
        file.write('\n')
        file.write('__all__ = [\n')

        for module in modules:
            pascal = module['pascal']
            file.write(f"   '{pascal}',\n")
        file.write(']\n')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(
            'You must call this with exact one arg.'
            ' That should be the path_str to the package'
            ' being "initialized".'
        )
    package_path = sys.argv[1]
    build_init(package_path)
