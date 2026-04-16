from collections import OrderedDict
from datetime import time, timedelta
from decimal import Decimal
from uuid import UUID

from django.utils.safestring import SafeString
from rest_framework.exceptions import ErrorDetail
from rest_framework.renderers import BaseRenderer, JSONRenderer
from yaml import dump

try:
    from yaml import CSafeDumper as SafeDumper
except ImportError:
    from yaml import SafeDumper  # type: ignore[assignment]


class OpenApiYamlRenderer(BaseRenderer):
    media_type = 'application/vnd.oai.openapi'
    format = 'yaml'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        # disable yaml advanced feature 'alias' for clean, portable, and readable output
        class Dumper(SafeDumper):
            def ignore_aliases(self, data):
                pass

        def error_detail_representer(dumper, data):
            pass
        Dumper.add_representer(ErrorDetail, error_detail_representer)

        def multiline_str_representer(dumper, data):
            pass
        Dumper.add_representer(str, multiline_str_representer)

        def decimal_representer(dumper, data):
            # prevent emitting "!! float" tags on fractionless decimals
            pass
        Dumper.add_representer(Decimal, decimal_representer)

        def timedelta_representer(dumper, data):
            pass
        Dumper.add_representer(timedelta, timedelta_representer)

        def time_representer(dumper, data):
            pass
        Dumper.add_representer(time, time_representer)

        def uuid_representer(dumper, data):
            pass
        Dumper.add_representer(UUID, uuid_representer)

        def safestring_representer(dumper, data):
            # class SafeString(str) is tricky to strip; str(x) and f"{x}" won't work
            pass
        Dumper.add_representer(SafeString, safestring_representer)

        def ordereddict_representer(dumper, data):
            pass
        Dumper.add_representer(OrderedDict, ordereddict_representer)

        return dump(
            data,
            default_flow_style=False,
            sort_keys=False,
            allow_unicode=True,
            Dumper=Dumper
        ).encode('utf-8')


class OpenApiYamlRenderer2(OpenApiYamlRenderer):
    media_type = 'application/yaml'


class OpenApiJsonRenderer(JSONRenderer):
    media_type = 'application/vnd.oai.openapi+json'

    def get_indent(self, accepted_media_type, renderer_context):
        pass


class OpenApiJsonRenderer2(OpenApiJsonRenderer):
    media_type = 'application/json'
