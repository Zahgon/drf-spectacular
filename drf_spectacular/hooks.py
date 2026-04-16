import re
from collections import defaultdict
from collections.abc import MutableMapping

from inflection import camelize
from rest_framework.settings import api_settings

from drf_spectacular.drainage import warn
from drf_spectacular.plumbing import (
    ResolvedComponent, list_hash, load_enum_name_overrides, safe_ref,
)
from drf_spectacular.settings import spectacular_settings


def postprocess_schema_enums(result, generator, **kwargs):
    """
    simple replacement of Enum/Choices that globally share the same name and have
    the same choices. Aids client generation to not generate a separate enum for
    every occurrence. only takes effect when replacement is guaranteed to be correct.
    """
    pass


def postprocess_schema_enum_id_removal(result, generator, **kwargs):
    """
    Iterative modifying approach to scanning the whole schema and removing the
    temporary helper ids that allowed us to distinguish similar enums.
    """
    pass


def preprocess_exclude_path_format(endpoints, **kwargs):
    """
        preprocessing hook that filters out {format} suffixed paths, in case
        format_suffix_patterns is used and {format} path params are unwanted.
    """
    format_path = f'{{{api_settings.FORMAT_SUFFIX_KWARG}}}'
    return [
        (path, path_regex, method, callback)
        for path, path_regex, method, callback in endpoints
        if not (path.endswith(format_path) or path.endswith(format_path + '/'))
    ]
