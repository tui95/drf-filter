from typing import List, Optional, Type

from django.db import models


class ListDisplayBuilder:
    @classmethod
    def build(
        cls,
        model: Type[models.Model],
        fields: Optional[List[str]] = None,
        exclude: Optional[List[str]] = None,
    ) -> List[str]:
        """
        Build list_display attribute of django ModelAdmin

        Args:
            model: model class to register via admin site
            fields: fields to include in list_display attribute. If not specify, will include all of model's fields
            exclude: fields to exclude from list_display attribute

        Returns:
            List[str]: list of model's fields
        """
        all_fields = cls.get_model_field_names(model=model)
        if fields is None and exclude is None:
            return all_fields
        elif isinstance(fields, list) and len(fields):
            return fields
        return [field for field in all_fields if field not in exclude]

    @classmethod
    def get_model_field_names(cls, model: Type[models.Model]) -> List[str]:
        return [field.name for field in model._meta.fields]
