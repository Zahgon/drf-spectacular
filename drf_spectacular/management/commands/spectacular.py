from textwrap import dedent

from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.utils.module_loading import import_string

from drf_spectacular.drainage import GENERATOR_STATS
from drf_spectacular.renderers import OpenApiJsonRenderer, OpenApiYamlRenderer
from drf_spectacular.settings import patched_settings, spectacular_settings
from drf_spectacular.validation import validate_schema


class SchemaGenerationError(CommandError):
    pass


class SchemaValidationError(CommandError):
    pass


class Command(BaseCommand):
    help = dedent("""
        Generate a spectacular OpenAPI3-compliant schema for your API.

        The warnings serve as a indicator for where your API could not be properly
        resolved. @extend_schema and @extend_schema_field are your friends.
        The spec should be valid in any case. If not, please open an issue
        on github: https://github.com/tfranzel/drf-spectacular/issues

        Remember to configure your APIs meta data like servers, version, url,
        documentation and so on in your SPECTACULAR_SETTINGS."
    """)

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        pass

    def get_renderer(self, format):
        pass
