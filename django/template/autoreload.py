from pathlib import Path

from django.dispatch import receiver
from django.template import engines
from django.template.backends.django import DjangoTemplates
from django.utils._os import to_path
from django.utils.autoreload import autoreload_started, file_changed, is_django_path

#data structure to hold coverage information about the conditional branches
coverage_info = {
    "backend_not_django_templates": False,
    "update_items_dirs": False,
    "loader_not_get_dirs": False,
    "update_items_loader_dirs": False,
    "loader_is_get_dirs": False,
    "update_items_filtered_dirs": False,
}

def get_template_directories():
    # Iterate through each template backend and find
    # any template_loader that has a 'get_dirs' method.
    # Collect the directories, filtering out Django templates.
    cwd = Path.cwd()
    items = set()
    for backend in engines.all():
        if not isinstance(backend, DjangoTemplates):
            coverage_info["backend_not_django_templates"] = True
            continue

        items.update(cwd / to_path(dir) for dir in backend.engine.dirs if dir)
        coverage_info["update_items_dirs"] = True

        for loader in backend.engine.template_loaders:
            if not hasattr(loader, "get_dirs"):
                coverage_info["loader_not_get_dirs"] = True
                continue
            items.update(
                cwd / to_path(directory)
                for directory in loader.get_dirs()
                if directory and not is_django_path(directory)
            )
            coverage_info["loader_is_get_dirs"] = True
            coverage_info["update_items_loader_dirs"] = True
            coverage_info["update_items_filtered_dirs"] = True
    return items


def reset_loaders():
    from django.forms.renderers import get_default_renderer

    for backend in engines.all():
        if not isinstance(backend, DjangoTemplates):
            continue
        for loader in backend.engine.template_loaders:
            loader.reset()

    backend = getattr(get_default_renderer(), "engine", None)
    if isinstance(backend, DjangoTemplates):
        for loader in backend.engine.template_loaders:
            loader.reset()


@receiver(autoreload_started, dispatch_uid="template_loaders_watch_changes")
def watch_for_template_changes(sender, **kwargs):
    for directory in get_template_directories():
        sender.watch_dir(directory, "**/*")


@receiver(file_changed, dispatch_uid="template_loaders_file_changed")
def template_changed(sender, file_path, **kwargs):
    if file_path.suffix == ".py":
        return
    for template_dir in get_template_directories():
        if template_dir in file_path.parents:
            reset_loaders()
            return True

def print_coverage_info():
    print("Coverage Information:")
    for branch, executed in coverage_info.items():
        print(f"{branch}: {'Executed' if executed else 'Not Executed'}")