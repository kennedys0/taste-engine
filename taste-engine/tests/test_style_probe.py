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
 ('Buat website portfolio bertema skeumorphsm','skeuomorphism',[],'ready'),
 ('Buat website portfolio tema Skeuomorphism','skeuomorphism',[],'ready'),
 ('Design a neo-brutalism portfolio','neo-brutalism',[],'ready'),
 ('Design in NeoBrutalism','neo-brutalism',[],'ready'),
 ('Need an edgy brutalist portfolio','brutalism',[],'ready'),
 ('Buat web glassmorphism jangan claymorphism','glassmorphism',['claymorphism'],'ready'),
 ('Buat web tanpa glassmorphism',None,['glassmorphism'],'needs-selection'),
 ('Buatkan aku website portfolio',None,[],'needs-selection'),
 ('Please make a minimalist dashboard','minimalism',[],'ready'),
 ('Build a retro-terminal portfolio','retro-terminal',[],'ready'),
 ('Buat web bertema neo brutalism','neo-brutalism',[],'ready'),
 ('Buat web gaya skeumorphism','skeuomorphism',[],'ready'),
 ('dashboard with no clutter, in brutalism','brutalism',[],'ready'),
 ('not only glassmorphism but also clay','glassmorphism',[],'blend'),
 ('I hate glassmorphism, go with bento','bento',['glassmorphism'],'ready'),
 ('without a sign-up form, in minimalism','minimalism',[],'ready'),
 ('I dislike brutalism, choose minimalism','minimalism',['brutalism'],'ready'),
 ('I do not want skeuomorphism, in brutalism','brutalism',['skeuomorphism'],'ready'),
 ('I don’t want neo-brutalism, make it clean minimalism','minimalism',['neo-brutalism'],'ready'),
 ('saya gak mau claymorphism tapi brutalism','brutalism',['claymorphism'],'ready'),
 ('tidak mau retro-terminal dan benci glassmorphism, pilih swiss editorial','swiss-editorial',['retro-terminal','glassmorphism'],'ready'),
 ('tanpa glassmorphism, buat dengan neo brutalism','neo-brutalism',['glassmorphism'],'ready'),
 ('hindari skeuomorphism melainkan bento','bento',['skeuomorphism'],'ready'),
]
for prompt,expected,excluded,status in scenarios:
    result=mod.candidates(prompt,registry)
    assert result['primary_style']==expected,(prompt,result)
    assert result['excluded_styles']==excluded,(prompt,result)
    assert result['status']==status,(prompt,result)
print('PASS:',len(scenarios),'alias and exclusion scenarios')
