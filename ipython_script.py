#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-02-27 09:00:55 (UTC+0100)

from IPython import get_ipython
import pymol
from pymol import cmd
from pymol.cmd import *
import numpy
import sys
sys.path.append('/home/bougui/source/pymol_plugins/pymol_isosurface')
import mrcutils

ipython = get_ipython()
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

pymol.finish_launching(args=['pymol', '-x']) # no external gui
