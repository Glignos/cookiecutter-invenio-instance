{% include 'misc/header.py' %}
"""Blueprint definitions."""

from __future__ import absolute_import, print_function

from flask import Blueprint

blueprint = Blueprint(
    '{{ cookiecutter.package_name}}_records',
    __name__,
    template_folder='templates',
    static_folder='static',
)
"""Blueprint used for loading templates and static assets

The sole purpose of this blueprint is to ensure that Invenio can find the
templates and static files located in the folders of the same names next to
this file.
"""
