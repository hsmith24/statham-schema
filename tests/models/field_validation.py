from typing import ClassVar, List, Type, Union

from attr import attrs, attrib
from jsonschema_objects import validators as val
from jsonschema_objects.validators import NotPassed


def instantiate(model: Type):
    def _convert(kwargs):
        return model(**kwargs)

    return _convert


def map_instantiate(model: Type):
    def _convert(list_kwargs):
        return [model(**kwargs) for kwargs in list_kwargs]

    return _convert


@attrs(kw_only=True)
class Model:
    """Model"""

    _required: ClassVar[List[str]] = []

    string_no_validation: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str)], default=NotPassed()
    )
    string_default: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str)], default="foo"
    )
    string_format_uuid: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.has_format("uuid")],
        default=NotPassed(),
    )
    string_format_date_time: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.has_format("date-time")],
        default=NotPassed(),
    )
    string_format_uri: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.has_format("uri")],
        default=NotPassed(),
    )
    string_pattern: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.pattern(r"^(foo|bar).*")],
        default=NotPassed(),
    )
    string_minLength: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.min_length(3)], default=NotPassed()
    )
    string_maxLength: Union[str, NotPassed] = attrib(
        validator=[val.instance_of(str), val.max_length(3)], default=NotPassed()
    )
    integer_no_validation: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int)], default=NotPassed()
    )
    integer_default: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int)], default=1
    )
    integer_minimum: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int), val.minimum(3)], default=NotPassed()
    )
    integer_exclusiveMinimum: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int), val.exclusive_minimum(3)],
        default=NotPassed(),
    )
    integer_maximum: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int), val.maximum(3)], default=NotPassed()
    )
    integer_exclusiveMaximum: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int), val.exclusive_maximum(3)],
        default=NotPassed(),
    )
    integer_multipleOf: Union[int, NotPassed] = attrib(
        validator=[val.instance_of(int), val.multiple_of(2)],
        default=NotPassed(),
    )
    number_no_validation: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float)], default=NotPassed()
    )
    number_default: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float)], default=1.5
    )
    number_minimum: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float), val.minimum(2.5)],
        default=NotPassed(),
    )
    number_exclusiveMinimum: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float), val.exclusive_minimum(2.5)],
        default=NotPassed(),
    )
    number_maximum: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float), val.maximum(2.5)],
        default=NotPassed(),
    )
    number_exclusiveMaximum: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float), val.exclusive_maximum(2.5)],
        default=NotPassed(),
    )
    number_multipleOf: Union[float, NotPassed] = attrib(
        validator=[val.instance_of(float), val.multiple_of(2.5)],
        default=NotPassed(),
    )
    boolean_no_validation: Union[bool, NotPassed] = attrib(
        validator=[val.instance_of(bool)], default=NotPassed()
    )
    boolean_default: Union[bool, NotPassed] = attrib(
        validator=[val.instance_of(bool)], default=True
    )
    null_no_validation: Union[None, NotPassed] = attrib(
        validator=[val.instance_of(type(None))], default=NotPassed()
    )
