#!/usr/bin/env python
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-02-27 09:00:55 (UTC+0100)

from IPython import get_ipython
import pymol
from pymol import cmd
from pymol.cmd import *
import chempy
import numpy
import matplotlib.pyplot as plt
plt.ion()  # Interactive mode (non-blocking window)
from utils import *
import sys
sys.path.append('/home/bougui/source/pymol_plugins/pymol_isosurface')
from mrcutils import *
sys.path.append('/home/bougui/source/pymol-psico')
# -------------------------------- psico module --------------------------------
import psico.fullinit
from psico.exporting import *
# ------------------------------------- - --------------------------------------

ipython = get_ipython()
ipython.magic("load_ext autoreload")
ipython.magic("autoreload 2")

pymol.finish_launching(args=['pymol', '-x']) # no external gui

# --- improve PyMOL performance for many-state objects and long trajectories ---
# See: https://pymolwiki.org/index.php/Defer_builds_mode
cmd.set('defer_builds_mode', 3)
# ------------------------------------- - --------------------------------------
