#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 14:36:47 2025

@author: nikipaspali
"""

-parser:protocol InterfaceAnalyzer.xml
-use_input_sc
-ex1
-ex2aro
-out:file:scorefile cluster_InterfaceAnalyzer.csv
-out:no_nstruct_label
-out:file:score_only
-in:file:spanfile 7BR3_PEP.span
-membrane:Membed_init
-membrane:Mhbond_depth
-score:weights membrane_highres.wts
