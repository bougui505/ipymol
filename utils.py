#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-03-04 11:23:36 (UTC+0100)

import chempy
from pymol import cmd


def pseudoatoms(coords, objectname):
    """
    Add multiple pseudoatoms as object
    """
    model = chempy.models.Indexed()
    for c in coords:
        atom = chempy.Atom()
        atom.coord = c
        model.add_atom(atom)
    cmd.load_model(model, objectname)
