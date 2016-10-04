# mypy-django-example
## A demo project for django-mypy

This repository contains an implementation of the [django 1.10 tutorial](https://docs.djangoproject.com/en/1.10/intro/tutorial01/)
extended with PEP-484 type annotations. Its goal is to be used as an example and demonstration of
the [mypy-django](https://github.com/machinalis/mypy-django) type stubs project. See the README
file at https://github.com/machinalis/mypy-django for more details.

## Usage

To type check the project you should install mypy-django and run:

```
$ mypy --strict-optional -p polls
polls/apps.py:1: error: No library stub file for module 'django.apps'
polls/apps.py:1: note: (Stub files are from https://github.com/python/typeshed)
polls/models.py:3: error: No library stub file for module 'django.db'
polls/tests.py:4: error: No library stub file for module 'django.test'
polls/views.py:1: error: No library stub file for module 'django.db.models.query'
polls/views.py:4: error: No library stub file for module 'django.shortcuts'
$ mypy --strict-optional -p tutorial
tutorial/urls.py:17: error: No library stub file for module 'django.contrib'
tutorial/urls.py:17: note: (Stub files are from https://github.com/python/typeshed)
tutorial/wsgi.py:12: error: No library stub file for module 'django.core.wsgi'
```

The error messages known shown above are expected (They just mention that mypy-django doesn't
cover some of the Django modules).

If you need information about how to run this as a project you should probably follow the django
tutorial itself.

## Using type annotations

If you take a look at the repo and its commits, you'll see how annotations were added; this can be
useful as an example of what to expect when annotating your own code.

Most of the changes consisted mainly in adding types to views, namely a `request: HttpRequest` argument
and a return value `-> HttpResponse`. See for example [60c1ff4](https://github.com/machinalis/mypy-django-example/commit/60c1ff4).

Other functions/methods that are now views can usually be annotated in a fairly simple and obvious way,
see for example [74335dd](https://github.com/machinalis/mypy-django-example/commit/74335dd), [07a8f6b](https://github.com/machinalis/mypy-django-example/commit/07a8f6b) or [b18aa7b](https://github.com/machinalis/mypy-django-example/commit/b18aa7b)

What follows is a list of trickier cases

 * You need to provide a type for `settings.ALLOWED HOSTS` if left empty, see [e6fdfab](https://github.com/machinalis/mypy-django-example/commit/e6fdfab)
 * You need to modify migrations with no dependencies and also add a `# type: List[Tuple[str, str]]`
   annotation to tis `dependencies` field, see [6b8f15a](https://github.com/machinalis/mypy-django-example/commit/6b8f15a)
 * You may want to `# type: ignore` some of the imported modules that have no type stubs to avoid warning messages. See [fb2e1f4](https://github.com/machinalis/mypy-django-example/commit/fb2e1f4)
 * Some complicated/deep structures containing None values can produce some warnings that can be avoided
   by giving more detailed annotations. See for example this case with `ModelAdmin.fieldsets`: [abb3ab0](https://github.com/machinalis/mypy-django-example/commit/abb3ab0)
 * Setting attributes to function objects (something you do if you use them in admin modules, for
   example for a `list_display`) is not very well supported by mypy. You can see that I workarounded that at [abb3ab0](https://github.com/machinalis/mypy-django-example/commit/abb3ab0).
   There is [an open issue](https://github.com/python/mypy/issues/2087) at the mypy tracker about this.
