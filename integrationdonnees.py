# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 19:59:10 2022

@author: Feyn
"""

import pandas

declarations=pandas.read_csv(r"C:\Users\Feyn\Talendintegration\declarations.csv",delimiter=";")


t=declarations.sample(10000)
tcol=t.columns

t.to_csv('transparencecol.csv') 

Declarationsconvid=declarations["convention_liee"]

#te=t[1].head(10)
"""uniqueValues = declarations.nunique(dropna=False)
uniqueValues.to_csv('nbmodalites.csv')
"""
L1=declarations['beneficiaire_profession_code'].unique()
L2=declarations['profession_libelle'].unique()
L3=declarations['secteur_activite'].unique()

#Modal=pandas.concat([L1,L2,L3],axis=1)
print(L1)

Conv=declarations[declarations['lien_interet']=='convention']

convsamp=Conv.sample(10000)


"""
convid=convid.dropna()

conviddup=pandas.concat(g for _, g in declarations.groupby("convention_liee") if len(g) > 1)

Convrem=declarations[declarations['convention_liee']=='25577_136466_566_C']
conviddupp=conviddup.sample(5000)
"""

indconv=pandas.concat(g for _, g in Conv.groupby("id_beneficiaire") if len(g) > 10)
indconv
indconvsamp=indconv.sample(10000)
