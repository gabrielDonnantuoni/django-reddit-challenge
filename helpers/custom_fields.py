from rest_framework.serializers import RelatedField, ValidationError


class NameRelatedField(RelatedField):
    def __init__(self, *args, **kwargs):
        self.lookup = kwargs.pop('lookup', 'name')
        super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        return getattr(obj, self.lookup)

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        try:
            return queryset.get(**{f'{self.lookup}': data})
        except queryset.model.DoesNotExist:
            model_name = queryset.model.__name__
            raise ValidationError([
                    f'There is no {model_name} with {self.lookup} = {data}'
                ])
