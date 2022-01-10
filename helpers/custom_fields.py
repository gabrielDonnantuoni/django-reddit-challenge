from rest_framework.serializers import RelatedField


class NameRelatedField(RelatedField):
    def __init__(self, *args, **kwargs):
        self.lookup = kwargs.pop('lookup', 'name')
        super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        return getattr(obj, self.lookup)

    def to_internal_value(self, data):
        queryset = self.get_queryset()
        return queryset.get(**{f'{self.lookup}': data})
