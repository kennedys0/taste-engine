#!/usr/bin/env python3
"""Unit checks for explicit style alias resolution. Run from any cwd."""
import importlib.util
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('style_probe',root/'scripts'/'style_probe.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
registry=json.loads((root/'styles'/'registry.json').read_text())
scenarios=[
 ('Buat website portfolio bertema skeumorphsm','skeuomorphism',[]),
 ('Buat website portfolio tema Skeuomorphism','skeuomorphism',[]),
 ('Design a neo-brutalism portfolio','neo-brutalism',[]),
 ('Design in NeoBrutalism','neo-brutalism',[]),
 ('Need an edgy brutalist portfolio','brutalism',[]),
 ('Buat web glassmorphism jangan claymorphism','glassmorphism',['claymorphism']),
 ('Buat web tanpa glassmorphism',None,['glassmorphism']),
 ('Buatkan aku website portfolio',None,[]),
 ('Please make a minimalist dashboard','minimalism',[]),
 ('Build a retro-terminal portfolio','retro-terminal',[]),
 ('Buat web bertema neo brutalism','neo-brutalism',[]),
 ('Buat web gaya skeumorphism','skeuomorphism',[]),
]
for prompt,expected,excluded in scenarios:
    result=mod.candidates(prompt,registry)
    assert result['primary_style']==expected,(prompt,result)
    assert result['excluded_styles']==excluded,(prompt,result)
print('PASS:',len(scenarios),'alias and exclusion scenarios')
