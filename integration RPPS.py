# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 22:47:32 2022

@author: Daniel Feyn(ris) MA
"""


import pandas

RPPS=pandas.read_csv(r"PS_LibreAcces_Personne_activite_202211021031.txt",delimiter="|" )
Samplerpps=RPPS.sample(1000)

uniqueValueRPPS= RPPS.nunique(dropna=False)
uniqueValueRPPS.to_csv('nbmodalitesRPPS.csv',encoding='iso-8859-1')
LRPPS1=RPPS['Libellé type savoir-faire'].unique()
LRPPS2=RPPS["Libellé secteur d'activité"].unique()