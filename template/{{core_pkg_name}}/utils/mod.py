from importlib import import_module


def import_from_string(spec):
    """
    Thanks to https://github.com/encode/django-rest-framework/blob/master/rest_framework/settings.py#L170
    Example:
        import_from_string('django_filters.rest_framework.DjangoFilterBackend')
        engine = conf['ENGINE']
        engine = import_from_string(engine) if isinstance(engine, six.string_types) else engine
    """
    try:
        # Nod to tastypie's use of importlib.
        parts = spec.split('.')
        module_path, class_name = '.'.join(parts[:-1]), parts[-1]
        module = import_module(module_path)
        return getattr(module, class_name)
    except (ImportError, AttributeError) as e:
        msg = "Could not import '%s'. %s: %s." % (spec, e.__class__.__name__, e)
        raise ImportError(msg) from e
