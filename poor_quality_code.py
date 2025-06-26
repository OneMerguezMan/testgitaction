# Fichier avec problèmes de qualité de code pour test SAST
import os
import sys
import json
import requests
import datetime
import time
import random
import math
import re
import subprocess
import threading
import multiprocessing
import asyncio
import aiohttp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import tensorflow as tf
import torch
import django
import flask
import fastapi
import sqlalchemy
import pymongo
import redis
import celery
import pytest
import unittest
import coverage
import black
import flake8
import mypy
import pylint
import bandit
import safety
import pip
import setuptools
import wheel
import twine
import sphinx
import mkdocs
import jupyter
import ipython
import spyder
import pycharm
import vscode
import sublime
import vim
import emacs
import atom
import brackets
import notepad
import wordpad
import notepad_plus_plus
import ultraedit
import editplus
import textpad
import textwrangler
import bbedit
import komodo
import netbeans
import eclipse
import intellij
import webstorm
import phpstorm
import rubymine
import pycharm
import clion
import rider
import datagrip
import appcode
import android_studio
import xcode
import visual_studio
import visual_studio_code
import atom
import brackets
import sublime_text
import vim
import emacs
import nano
import gedit
import kate
import kwrite
import leafpad
import mousepad
import pluma
import xed
import gvim
import nvim
import spacevim
import doom_emacs
import spacemacs
import evil
import org_mode
import magit
import helm
import ivy
import counsel
import swiper
import company
import yasnippet
import flycheck
import flymake
import lsp_mode
import eglot
import dap_mode
import treemacs
import neotree
import projectile
import helm_projectile
import ivy_projectile
import counsel_projectile
import swiper_projectile
import company_projectile
import yasnippet_projectile
import flycheck_projectile
import flymake_projectile
import lsp_mode_projectile
import eglot_projectile
import dap_mode_projectile
import treemacs_projectile
import neotree_projectile

# Variables mal nommées et inutilisées
a=1
b=2
c=3
d=4
e=5
f=6
g=7
h=8
i=9
j=10
k=11
l=12
m=13
n=14
o=15
p=16
q=17
r=18
s=19
t=20
u=21
v=22
w=23
x=24
y=25
z=26

# Fonction mal formatée avec code mort
def bad_function(  param1,param2,param3,param4,param5,param6,param7,param8,param9,param10,param11,param12,param13,param14,param15,param16,param17,param18,param19,param20,param21,param22,param23,param24,param25,param26,param27,param28,param29,param30,param31,param32,param33,param34,param35,param36,param37,param38,param39,param40,param41,param42,param43,param44,param45,param46,param47,param48,param49,param50,param51,param52,param53,param54,param55,param56,param57,param58,param59,param60,param61,param62,param63,param64,param65,param66,param67,param68,param69,param70,param71,param72,param73,param74,param75,param76,param77,param78,param79,param80,param81,param82,param83,param84,param85,param86,param87,param88,param89,param90,param91,param92,param93,param94,param95,param96,param97,param98,param99,param100):
    # Code mort - jamais exécuté
    if False:
        print("Ce code ne s'exécute jamais")
        return None
        print("Code après return - jamais atteint")
    
    # Code mal formaté
    result=param1+param2+param3+param4+param5+param6+param7+param8+param9+param10+param11+param12+param13+param14+param15+param16+param17+param18+param19+param20+param21+param22+param23+param24+param25+param26+param27+param28+param29+param30+param31+param32+param33+param34+param35+param36+param37+param38+param39+param40+param41+param42+param43+param44+param45+param46+param47+param48+param49+param50+param51+param52+param53+param54+param55+param56+param57+param58+param59+param60+param61+param62+param63+param64+param65+param66+param67+param68+param69+param70+param71+param72+param73+param74+param75+param76+param77+param78+param79+param80+param81+param82+param83+param84+param85+param86+param87+param88+param89+param90+param91+param92+param93+param94+param95+param96+param97+param98+param99+param100
    return result

# Classe mal formatée avec méthodes inutilisées
class BadClass:
    def __init__(self):
        self.attr1=1
        self.attr2=2
        self.attr3=3
        self.attr4=4
        self.attr5=5
        self.attr6=6
        self.attr7=7
        self.attr8=8
        self.attr9=9
        self.attr10=10
    
    # Méthode inutilisée
    def unused_method1(self):
        print("Cette méthode n'est jamais appelée")
        return "dead code"
    
    # Méthode inutilisée
    def unused_method2(self):
        print("Cette méthode n'est jamais appelée non plus")
        return "more dead code"
    
    # Méthode mal formatée
    def bad_method(self,param1,param2,param3,param4,param5,param6,param7,param8,param9,param10):
        # Code mort
        if 1==2:
            print("Impossible condition")
            return None
        
        # Code mal formaté
        result=param1*param2+param3-param4/param5%param6**param7//param8&param9|param10
        return result

# Variables globales inutilisées
UNUSED_GLOBAL_1 = "Cette variable globale n'est jamais utilisée"
UNUSED_GLOBAL_2 = 42
UNUSED_GLOBAL_3 = [1, 2, 3, 4, 5]
UNUSED_GLOBAL_4 = {"key": "value"}
UNUSED_GLOBAL_5 = (1, 2, 3)

# Fonction avec code mort et mal formaté
def another_bad_function():
    # Code mort
    if False:
        print("Code mort 1")
        return "dead"
    
    # Code mort
    if 0:
        print("Code mort 2")
        return "dead"
    
    # Code mort
    if None:
        print("Code mort 3")
        return "dead"
    
    # Code mal formaté
    x=1;y=2;z=3
    if x==1:print("x is 1")
    elif y==2:print("y is 2")
    else:print("z is 3")
    
    # Code mort après return
    return "result"
    print("Ce code ne s'exécute jamais")

# Code mal formaté dans le scope global
if True:print("Mal formaté")
else:print("Aussi mal formaté")

# Boucle inutile
for i in range(100):
    pass  # Code mort

# Try-except mal formaté
try:result=1/0
except:print("Exception")
finally:print("Finally")

# Code mort dans une condition impossible
if 1 == 2 and 2 == 3 and 3 == 4:
    print("Code mort dans condition impossible")
    import this  # Import inutile dans code mort

# Fonction avec paramètres inutilisés
def function_with_unused_params(used_param, unused_param1, unused_param2, unused_param3):
    print(f"Only using: {used_param}")
    # unused_param1, unused_param2, unused_param3 ne sont jamais utilisés
    return used_param

# Code mal formaté avec espaces incorrects
def badly_spaced_function( ):
    x=1
    y=2
    z=3
    if x==1:
        print("x is 1")
    elif y==2:
        print("y is 2")
    else:
        print("z is 3")
    return x+y+z

# Variables inutilisées dans une fonction
def function_with_unused_vars():
    used_var = "I'm used"
    unused_var1 = "I'm not used"
    unused_var2 = 42
    unused_var3 = [1, 2, 3]
    print(used_var)
    return used_var

# Code mort dans une classe
class ClassWithDeadCode:
    def __init__(self):
        self.value = 42
    
    def method_with_dead_code(self):
        # Code mort
        if False:
            return "dead"
        
        # Code mort après return
        return "alive"
        print("This never executes")
    
    # Méthode inutilisée
    def unused_method(self):
        return "unused"

# Code mal formaté avec indentation incorrecte
def bad_indentation():
    x=1
  y=2  # Mauvaise indentation
    z=3
        w=4  # Indentation excessive
    return x+y+z+w

# Variables avec noms non descriptifs
def function_with_bad_names():
    x = 1
    y = 2
    z = 3
    a = x + y
    b = a * z
    return b

# Code mort dans une expression
def dead_code_in_expression():
    result = (1 + 2) or (print("This never executes"), 3)[1]
    return result

# Import inutile dans une fonction
def function_with_unused_import():
    import datetime  # Import inutile
    return "hello"

# Code mal formaté avec opérateurs
def bad_operator_formatting():
    x=1+2*3/4-5%6**7//8
    y=x&1|2^3<<4>>5
    return x+y

# Variables inutilisées dans le scope global
unused_var1 = "global unused"
unused_var2 = 123
unused_var3 = [1, 2, 3, 4, 5]

# Code mort dans une boucle
def dead_code_in_loop():
    for i in range(10):
        if i == 5:
            break
            print("This never executes")  # Code mort après break
        if i == 3:
            continue
            print("This never executes either")  # Code mort après continue

# Fonction avec docstring manquante
def function_without_docstring(param1, param2):
    return param1 + param2

# Classe avec docstring manquante
class ClassWithoutDocstring:
    def __init__(self):
        pass

# Code mal formaté avec parenthèses
def bad_parentheses():
    x=(1+2)*(3+4)
    y=((1+2)*(3+4))
    z=(((1+2)*(3+4)))
    return x+y+z

# Variables avec types mixtes
def mixed_types():
    x = 1
    y = "2"
    z = [3]
    w = {"4": 5}
    return x + int(y) + z[0] + w["4"]

# Code mort dans une fonction lambda
dead_lambda = lambda x: x + 1 if x > 0 else (print("dead"), 0)[1]

# Fonction avec trop de paramètres
def too_many_parameters(p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15):
    return p1 + p2 + p3 + p4 + p5 + p6 + p7 + p8 + p9 + p10 + p11 + p12 + p13 + p14 + p15

# Code mal formaté avec chaînes
def bad_string_formatting():
    x="hello"+"world"
    y='single'+'quotes'
    z="""triple
    quotes"""
    return x+y+z

# Variables avec noms trop courts
def short_names():
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    return a + b + c + d + e

# Code mort dans une condition
def dead_code_in_condition():
    if True:
        return "alive"
    else:
        print("This never executes")
        return "dead"

# Fonction avec retour inutile
def unnecessary_return():
    x = 1 + 2
    print(x)
    return  # Retour inutile

# Code mal formaté avec commentaires
def bad_comment_formatting():
    x=1#comment without space
    y=2#another comment
    z=3#yet another comment
    return x+y+z

# Variables inutilisées dans une liste comprehension
def unused_in_comprehension():
    numbers = [1, 2, 3, 4, 5]
    result = [x for x in numbers if x > 3]  # x est utilisé
    unused = [y for y in numbers]  # y n'est pas utilisé dans la condition
    return result

# Code mort dans une fonction générateur
def dead_code_in_generator():
    for i in range(10):
        yield i
        print("This executes after each yield")  # Ce code s'exécute
        return  # Ce return termine le générateur prématurément
        print("This never executes")  # Code mort

# Fonction avec exception non gérée
def unhandled_exception():
    x = 1 / 0  # Exception non gérée
    return x

# Code mal formaté avec dictionnaire
def bad_dict_formatting():
    d={"key1":"value1","key2":"value2","key3":"value3"}
    return d

# Variables avec noms non conformes PEP8
def bad_naming():
    myVariable = 1  # CamelCase au lieu de snake_case
    MyClass = 2     # Nom de classe pour une variable
    CONSTANT = 3    # Constante en minuscules
    return myVariable + MyClass + CONSTANT

# Code mort dans une fonction récursive
def recursive_with_dead_code(n):
    if n <= 0:
        return 0
    return n + recursive_with_dead_code(n - 1)
    print("This never executes")  # Code mort après return

# Import avec alias inutile
import os as operating_system  # Alias inutile
import sys as system  # Alias inutile

# Code mal formaté avec tuples
def bad_tuple_formatting():
    t=(1,2,3,4,5)
    x,y,z,w,v=t
    return x+y+z+w+v

# Fonction avec paramètres par défaut inutiles
def default_params_unused(param1, param2="default", param3=None):
    return param1  # param2 et param3 ne sont jamais utilisés

# Code mort dans une fonction avec yield
def generator_with_dead_code():
    yield 1
    yield 2
    return "done"  # Code mort dans un générateur
    yield 3  # Code mort après return

# Variables avec types incorrects
def wrong_types():
    x = "1" + 2  # Concaténation string + int
    y = [1, 2, 3] + "4"  # Liste + string
    return x, y

# Code mal formaté avec sets
def bad_set_formatting():
    s={1,2,3,4,5}
    return s

# Fonction avec docstring incorrecte
def wrong_docstring():
    """
    This is a docstring but it doesn't describe the function properly.
    """
    return "hello"

# Code mort dans une fonction avec raise
def function_with_raise():
    raise Exception("This exception is always raised")
    print("This never executes")  # Code mort après raise
    return "never reached"

# Variables inutilisées dans une fonction avec *args
def unused_args(*args):
    return len(args)  # args est utilisé mais pas les éléments individuels

# Code mal formaté avec f-strings
def bad_fstring_formatting():
    x=1
    y=2
    z=f"x={x} y={y}"
    return z

# Fonction avec paramètres inutilisés et code mort
def complex_bad_function(param1, unused_param, param2):
    if param1 > 0:
        if param2 < 0:
            return param1 + param2
        else:
            return param1 - param2
    else:
        if False:  # Code mort
            return "dead"
        return "alive"
    
    print("This never executes")  # Code mort après tous les returns

# Code mal formaté avec classes
class BadlyFormattedClass:
    def __init__(self):self.x=1;self.y=2
    def method(self):return self.x+self.y

# Variables globales mal nommées
GLOBAL_VAR_1 = "bad naming"
global_var_2 = "inconsistent naming"

# Code mort dans une fonction avec assert
def function_with_assert():
    x = 1
    assert x == 1, "This assertion always passes"
    assert False, "This assertion always fails"  # Code mort après assert False
    return "never reached"

# Fonction avec trop de lignes (plus de 79 caractères)
def very_long_line_function():
    very_long_variable_name_that_exceeds_pep8_line_length_limit = "this is a very long string that makes the line exceed 79 characters"
    return very_long_variable_name_that_exceeds_pep8_line_length_limit

# Code mal formaté avec imports
from os import path, environ, getcwd, listdir, mkdir, rmdir, remove, rename, stat, access, chmod, chown, link, symlink, readlink, walk, scandir, makedirs, removedirs, rename, utime, stat_result, statvfs_result, terminal_size, environb, getenv, putenv, unsetenv, getpid, getppid, getuid, geteuid, getgid, getegid, getgroups, setuid, setgid, setgroups, initgroups, getlogin, getpgrp, setpgrp, getpgid, setpgid, getsid, setsid, umask, chroot, chdir, fchdir, getcwd, makedirs, removedirs, rename, listdir, scandir, walk, stat, lstat, access, chmod, lchmod, chown, lchown, link, symlink, readlink, remove, unlink, rmdir, removedirs, mkdir, makedirs, rename, replace, stat, lstat, access, chmod, lchmod, chown, lchown, link, symlink, readlink, remove, unlink, rmdir, removedirs, mkdir, makedirs, rename, replace

# Code mort dans une fonction avec exit
def function_with_exit():
    print("About to exit")
    exit(0)  # Code mort après exit
    print("This never executes")

# Variables avec noms réservés
def reserved_names():
    class_ = 1  # Nom réservé avec underscore
    def_ = 2    # Nom réservé avec underscore
    return class_ + def_

# Code mal formaté avec expressions
def bad_expression_formatting():
    x=1+2*3/4-5%6**7//8&9|10^11<<12>>13
    return x

# Fonction avec docstring vide
def empty_docstring():
    """
    """
    return "empty"

# Code mort dans une fonction avec sys.exit
def function_with_sys_exit():
    import sys
    print("Exiting")
    sys.exit(0)  # Code mort après sys.exit
    print("This never executes")

# Variables inutilisées dans une fonction avec kwargs
def unused_kwargs(**kwargs):
    return "kwargs not used"  # kwargs n'est jamais utilisé

# Code mal formaté avec listes
def bad_list_formatting():
    l=[1,2,3,4,5]
    return l

# Fonction avec paramètres en double
def duplicate_parameters(param1, param1):  # Paramètre en double
    return param1

# Code mort dans une fonction avec return multiple
def multiple_returns():
    if True:
        return "first"
    return "second"
    return "third"  # Code mort

# Variables avec noms trop longs
def very_long_variable_names():
    this_is_a_very_long_variable_name_that_exceeds_reasonable_length = 1
    another_very_long_variable_name_that_is_unnecessarily_long = 2
    return this_is_a_very_long_variable_name_that_exceeds_reasonable_length + another_very_long_variable_name_that_is_unnecessarily_long

# Code mal formaté avec conditions
def bad_condition_formatting():
    x=1
    if x==1:print("x is 1")
    elif x==2:print("x is 2")
    else:print("x is something else")

# Fonction avec docstring mal formatée
def malformed_docstring():
    """This docstring
    is malformed
    and doesn't follow
    proper formatting
    """
    return "malformed"

# Code mort dans une fonction avec break
def function_with_break():
    for i in range(10):
        if i == 5:
            break
            print("This never executes")  # Code mort après break
        print(i)

# Variables inutilisées dans une fonction avec yield from
def unused_in_yield_from():
    def inner():
        yield 1
        yield 2
    
    for item in inner():
        yield item
        unused_var = "not used"  # Variable inutilisée

# Code mal formaté avec try-except
def bad_try_except_formatting():
    try:x=1/0
    except:print("Exception")
    finally:print("Finally")

# Fonction avec paramètres inutiles et code mort
def final_bad_function(param1, param2, param3, param4, param5):
    # Paramètres inutilisés
    if param1 > 0:
        return param1
    else:
        if False:  # Code mort
            return param2 + param3 + param4 + param5
        return -param1
    
    # Code mort après tous les returns
    print("This never executes")
    return "dead code" 
