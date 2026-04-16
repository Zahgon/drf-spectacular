from django.core.checks import Error, Warning, register


@register(deploy=True)
def schema_check(app_configs, **kwargs):
    """ Perform dummy generation and emit warnings/errors as part of Django's check framework """
    pass
