#!/usr/bin/env sh
# -*- coding: UTF8 -*-

# Author: Guillaume Bouvier -- guillaume.bouvier@pasteur.fr
# https://research.pasteur.fr/en/member/guillaume-bouvier/
# 2020-02-27 09:03:23 (UTC+0100)

DIRSCRIPT="$(dirname "$(readlink -f "$0")")"
ipython --profile=pymol -i "$DIRSCRIPT/ipython_script.py"
