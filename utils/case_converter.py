import re


class CaseConverter:
    """Stati method only class for case converting."""

    @staticmethod
    def snake_to_camel(string: str) -> str:
        """Convert snake case into camel case"""
        words_list = string.split('_')
        first = words_list[0]
        rest = [word.title() for word in words_list[1:]]
        return first + ''.join(rest)

    @staticmethod
    def snake_to_pascal(string: str) -> str:
        """Convert snake case into pascal case"""
        return string.replace("_", " ").title().replace(" ", "")

    @staticmethod
    def pascal_to_snake(string: str) -> str:
        """Convert pascal case into snake case"""
        string = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', string)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', string).lower()

    @classmethod
    def camel_to_snake(cls, string: str) -> str:
        """Convert camel case into snake case"""
        return cls.pascal_to_snake(string)
