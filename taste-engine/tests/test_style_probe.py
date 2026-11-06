#!/usr/bin/env python3
"""Unit checks for explicit style alias resolution. Run from any cwd."""
import importlib.util
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('style_probe',root/'scripts'/'style_probe.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
registry=json.loads((root/'styles'/'registry.json').read_text(encoding='utf-8'))
scenarios=[
 ('Buat website portfolio bertema skeumorphsm','frutiger-aero',[],'ready','tactile'),
 ('Buat website portfolio tema Skeuomorphism','frutiger-aero',[],'ready','tactile'),
 ('Design a neo-brutalism portfolio','neo-brutalism',[],'ready'),
 ('Design in NeoBrutalism','neo-brutalism',[],'ready'),
 ('Need an edgy brutalist portfolio','brutalism',[],'ready'),
 ('Buat web glassmorphism jangan claymorphism','frutiger-aero',['claymorphism'],'ready','glass'),
 ('Buat web tanpa glassmorphism',None,['frutiger-aero'],'needs-selection'),
 ('Buatkan aku website portfolio',None,[],'needs-selection'),
 ('Please make a minimalist dashboard','minimalism',[],'ready'),
 ('Build a retro-terminal portfolio','retro-terminal',[],'ready'),
 ('Buat web bertema neo brutalism','neo-brutalism',[],'ready'),
 ('Buat web gaya skeumorphism','frutiger-aero',[],'ready','tactile'),
 ('dashboard with no clutter, in brutalism','brutalism',[],'ready'),
 ('not only glassmorphism but also clay','frutiger-aero',[],'blend','glass'),
 ('I hate glassmorphism, go with bento','brutalism',['frutiger-aero'],'ready','bento'),
 ('without a sign-up form, in minimalism','minimalism',[],'ready',None),
 ('I dislike brutalism, choose minimalism','minimalism',['brutalism'],'ready',None),
 ('I do not want skeuomorphism, in brutalism','brutalism',['frutiger-aero'],'ready','raw'),
 ('I don’t want neo-brutalism, make it clean minimalism','minimalism',['neo-brutalism'],'ready',None),
 ('saya gak mau claymorphism tapi brutalism','brutalism',['claymorphism'],'ready','raw'),
 ('tidak mau retro-terminal dan benci glassmorphism, pilih swiss editorial','swiss-editorial',['retro-terminal','frutiger-aero'],'ready',None),
 ('tanpa glassmorphism, buat dengan neo brutalism','neo-brutalism',['frutiger-aero'],'ready',None),
 ('hindari skeuomorphism melainkan bento','brutalism',['frutiger-aero'],'ready','bento'),
 ('Build a Retro Pixel portfolio','retro-pixel',[],'ready',None),
 ('Create a pixel art landing page','retro-pixel',[],'ready',None),
 ('Build a retro terminal','retro-terminal',[],'ready',None),
 ('I want neo-brutalism, not pixel art','neo-brutalism',['retro-pixel'],'ready',None),
 ('Do not use retro pixel design',None,['retro-pixel'],'needs-selection',None),
 ('Buat web portfolio retro pixel','retro-pixel',[],'ready',None),
 ('Buat website 8-bit ui','retro-pixel',[],'ready',None),
 ('Build an enterprise B2B dashboard','minimalism',[],'ready',None),
 ('Design a data-first console','minimalism',[],'ready',None),
 ('Build a brutalist bento grid landing page','brutalism',[],'ready','bento'),
 ('Design a raw brutalist website','brutalism',[],'ready','raw'),
 ('Design an art deco portfolio','art-deco',[],'ready','modern'),
 ('Create a classic deco luxury landing page','art-deco',[],'ready','classic'),
 ('Build a minimal deco architectural website','art-deco',[],'ready','minimal'),
 ('Buat web tema art deco','art-deco',[],'ready','modern'),
 ('I want gatsby style, not brutalism','art-deco',['brutalism'],'ready','classic'),
 ('Do not use art deco',None,['art-deco'],'needs-selection',None),
 ('Design a frutiger aero portfolio','frutiger-aero',[],'ready','classic'),
 ('Create an aero glass interface','frutiger-aero',[],'ready','glass'),
 ('Build an aero tactile dashboard','frutiger-aero',[],'ready','tactile'),
 ('Buat web tema frutiger aero','frutiger-aero',[],'ready','classic'),
 ('Do not use frutiger aero',None,['frutiger-aero'],'needs-selection',None),
 ('Design a Y2K futurism portfolio','y2k-futurism',[],'ready','chrome'),
 ('Create a holographic interface','y2k-futurism',[],'ready','holographic'),
 ('Build a retro-tech console interface','y2k-futurism',[],'ready','retro-tech'),
 ('Buat web tema y2k aesthetic','y2k-futurism',[],'ready','chrome'),
 ('Do not use y2k futurism',None,['y2k-futurism'],'needs-selection',None),
 ('I want liquid chrome, not brutalism','y2k-futurism',['brutalism'],'ready','chrome'),
]
for item in scenarios:
    if len(item) == 5:
        prompt,expected,excluded,status,expected_variant = item
    else:
        prompt,expected,excluded,status = item
        expected_variant = None
    result=mod.candidates(prompt,registry)
    assert result['primary_style']==expected,(prompt,result)
    assert result['excluded_styles']==excluded,(prompt,result)
    assert result['status']==status,(prompt,result)
    if expected_variant is not None:
        assert result['variant']==expected_variant,(prompt,result)
print('PASS:',len(scenarios),'alias and exclusion scenarios')
