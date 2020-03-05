#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-03-04 11:23:36 (UTC+0100)

import chempy
from pymol import cmd


def pseudoatoms(coords, objectname, resids=None):
    """
    Add multiple pseudoatoms as object
    """
    model = chempy.models.Indexed()
    if resids is None:
        resids = range(coords.shape[0])
    for i, c in enumerate(coords):
        atom = chempy.Atom()
        atom.coord = c
        atom.resi_number = resids[i]
        model.add_atom(atom)
    cmd.load_model(model, objectname)
    return model
