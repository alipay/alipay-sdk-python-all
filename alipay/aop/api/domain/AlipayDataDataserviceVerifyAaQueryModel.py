#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.CanshujiaoyanPeihuan import CanshujiaoyanPeihuan
from alipay.aop.api.domain.CanshujiaoyanPeihuan import CanshujiaoyanPeihuan


class AlipayDataDataserviceVerifyAaQueryModel(object):

    def __init__(self):
        self._booleanaa = None
        self._c = None
        self._ceisjnvikdv = None
        self._datecc = None
        self._datesy = None
        self._dd = None
        self._dddddcfnj = None
        self._dddvg = None
        self._ddjhgfd = None
        self._de = None
        self._f = None
        self._fuaza = None
        self._fuza = None
        self._gr = None
        self._hy = None
        self._ll = None
        self._prcides = None
        self._stringstylea = None
        self._stringstyleb = None

    @property
    def booleanaa(self):
        return self._booleanaa

    @booleanaa.setter
    def booleanaa(self, value):
        self._booleanaa = value
    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, value):
        self._c = value
    @property
    def ceisjnvikdv(self):
        return self._ceisjnvikdv

    @ceisjnvikdv.setter
    def ceisjnvikdv(self, value):
        self._ceisjnvikdv = value
    @property
    def datecc(self):
        return self._datecc

    @datecc.setter
    def datecc(self, value):
        if isinstance(value, list):
            self._datecc = list()
            for i in value:
                self._datecc.append(i)
    @property
    def datesy(self):
        return self._datesy

    @datesy.setter
    def datesy(self, value):
        if isinstance(value, list):
            self._datesy = list()
            for i in value:
                self._datesy.append(i)
    @property
    def dd(self):
        return self._dd

    @dd.setter
    def dd(self, value):
        self._dd = value
    @property
    def dddddcfnj(self):
        return self._dddddcfnj

    @dddddcfnj.setter
    def dddddcfnj(self, value):
        self._dddddcfnj = value
    @property
    def dddvg(self):
        return self._dddvg

    @dddvg.setter
    def dddvg(self, value):
        self._dddvg = value
    @property
    def ddjhgfd(self):
        return self._ddjhgfd

    @ddjhgfd.setter
    def ddjhgfd(self, value):
        if isinstance(value, list):
            self._ddjhgfd = list()
            for i in value:
                self._ddjhgfd.append(i)
    @property
    def de(self):
        return self._de

    @de.setter
    def de(self, value):
        if isinstance(value, list):
            self._de = list()
            for i in value:
                self._de.append(i)
    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, value):
        self._f = value
    @property
    def fuaza(self):
        return self._fuaza

    @fuaza.setter
    def fuaza(self, value):
        if isinstance(value, CanshujiaoyanPeihuan):
            self._fuaza = value
        else:
            self._fuaza = CanshujiaoyanPeihuan.from_alipay_dict(value)
    @property
    def fuza(self):
        return self._fuza

    @fuza.setter
    def fuza(self, value):
        if isinstance(value, CanshujiaoyanPeihuan):
            self._fuza = value
        else:
            self._fuza = CanshujiaoyanPeihuan.from_alipay_dict(value)
    @property
    def gr(self):
        return self._gr

    @gr.setter
    def gr(self, value):
        if isinstance(value, list):
            self._gr = list()
            for i in value:
                self._gr.append(i)
    @property
    def hy(self):
        return self._hy

    @hy.setter
    def hy(self, value):
        self._hy = value
    @property
    def ll(self):
        return self._ll

    @ll.setter
    def ll(self, value):
        self._ll = value
    @property
    def prcides(self):
        return self._prcides

    @prcides.setter
    def prcides(self, value):
        self._prcides = value
    @property
    def stringstylea(self):
        return self._stringstylea

    @stringstylea.setter
    def stringstylea(self, value):
        self._stringstylea = value
    @property
    def stringstyleb(self):
        return self._stringstyleb

    @stringstyleb.setter
    def stringstyleb(self, value):
        if isinstance(value, list):
            self._stringstyleb = list()
            for i in value:
                self._stringstyleb.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.booleanaa:
            if hasattr(self.booleanaa, 'to_alipay_dict'):
                params['booleanaa'] = self.booleanaa.to_alipay_dict()
            else:
                params['booleanaa'] = self.booleanaa
        if self.c:
            if hasattr(self.c, 'to_alipay_dict'):
                params['c'] = self.c.to_alipay_dict()
            else:
                params['c'] = self.c
        if self.ceisjnvikdv:
            if hasattr(self.ceisjnvikdv, 'to_alipay_dict'):
                params['ceisjnvikdv'] = self.ceisjnvikdv.to_alipay_dict()
            else:
                params['ceisjnvikdv'] = self.ceisjnvikdv
        if self.datecc:
            if isinstance(self.datecc, list):
                for i in range(0, len(self.datecc)):
                    element = self.datecc[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.datecc[i] = element.to_alipay_dict()
            if hasattr(self.datecc, 'to_alipay_dict'):
                params['datecc'] = self.datecc.to_alipay_dict()
            else:
                params['datecc'] = self.datecc
        if self.datesy:
            if isinstance(self.datesy, list):
                for i in range(0, len(self.datesy)):
                    element = self.datesy[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.datesy[i] = element.to_alipay_dict()
            if hasattr(self.datesy, 'to_alipay_dict'):
                params['datesy'] = self.datesy.to_alipay_dict()
            else:
                params['datesy'] = self.datesy
        if self.dd:
            if hasattr(self.dd, 'to_alipay_dict'):
                params['dd'] = self.dd.to_alipay_dict()
            else:
                params['dd'] = self.dd
        if self.dddddcfnj:
            if hasattr(self.dddddcfnj, 'to_alipay_dict'):
                params['dddddcfnj'] = self.dddddcfnj.to_alipay_dict()
            else:
                params['dddddcfnj'] = self.dddddcfnj
        if self.dddvg:
            if hasattr(self.dddvg, 'to_alipay_dict'):
                params['dddvg'] = self.dddvg.to_alipay_dict()
            else:
                params['dddvg'] = self.dddvg
        if self.ddjhgfd:
            if isinstance(self.ddjhgfd, list):
                for i in range(0, len(self.ddjhgfd)):
                    element = self.ddjhgfd[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ddjhgfd[i] = element.to_alipay_dict()
            if hasattr(self.ddjhgfd, 'to_alipay_dict'):
                params['ddjhgfd'] = self.ddjhgfd.to_alipay_dict()
            else:
                params['ddjhgfd'] = self.ddjhgfd
        if self.de:
            if isinstance(self.de, list):
                for i in range(0, len(self.de)):
                    element = self.de[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.de[i] = element.to_alipay_dict()
            if hasattr(self.de, 'to_alipay_dict'):
                params['de'] = self.de.to_alipay_dict()
            else:
                params['de'] = self.de
        if self.f:
            if hasattr(self.f, 'to_alipay_dict'):
                params['f'] = self.f.to_alipay_dict()
            else:
                params['f'] = self.f
        if self.fuaza:
            if hasattr(self.fuaza, 'to_alipay_dict'):
                params['fuaza'] = self.fuaza.to_alipay_dict()
            else:
                params['fuaza'] = self.fuaza
        if self.fuza:
            if hasattr(self.fuza, 'to_alipay_dict'):
                params['fuza'] = self.fuza.to_alipay_dict()
            else:
                params['fuza'] = self.fuza
        if self.gr:
            if isinstance(self.gr, list):
                for i in range(0, len(self.gr)):
                    element = self.gr[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.gr[i] = element.to_alipay_dict()
            if hasattr(self.gr, 'to_alipay_dict'):
                params['gr'] = self.gr.to_alipay_dict()
            else:
                params['gr'] = self.gr
        if self.hy:
            if hasattr(self.hy, 'to_alipay_dict'):
                params['hy'] = self.hy.to_alipay_dict()
            else:
                params['hy'] = self.hy
        if self.ll:
            if hasattr(self.ll, 'to_alipay_dict'):
                params['ll'] = self.ll.to_alipay_dict()
            else:
                params['ll'] = self.ll
        if self.prcides:
            if hasattr(self.prcides, 'to_alipay_dict'):
                params['prcides'] = self.prcides.to_alipay_dict()
            else:
                params['prcides'] = self.prcides
        if self.stringstylea:
            if hasattr(self.stringstylea, 'to_alipay_dict'):
                params['stringstylea'] = self.stringstylea.to_alipay_dict()
            else:
                params['stringstylea'] = self.stringstylea
        if self.stringstyleb:
            if isinstance(self.stringstyleb, list):
                for i in range(0, len(self.stringstyleb)):
                    element = self.stringstyleb[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.stringstyleb[i] = element.to_alipay_dict()
            if hasattr(self.stringstyleb, 'to_alipay_dict'):
                params['stringstyleb'] = self.stringstyleb.to_alipay_dict()
            else:
                params['stringstyleb'] = self.stringstyleb
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayDataDataserviceVerifyAaQueryModel()
        if 'booleanaa' in d:
            o.booleanaa = d['booleanaa']
        if 'c' in d:
            o.c = d['c']
        if 'ceisjnvikdv' in d:
            o.ceisjnvikdv = d['ceisjnvikdv']
        if 'datecc' in d:
            o.datecc = d['datecc']
        if 'datesy' in d:
            o.datesy = d['datesy']
        if 'dd' in d:
            o.dd = d['dd']
        if 'dddddcfnj' in d:
            o.dddddcfnj = d['dddddcfnj']
        if 'dddvg' in d:
            o.dddvg = d['dddvg']
        if 'ddjhgfd' in d:
            o.ddjhgfd = d['ddjhgfd']
        if 'de' in d:
            o.de = d['de']
        if 'f' in d:
            o.f = d['f']
        if 'fuaza' in d:
            o.fuaza = d['fuaza']
        if 'fuza' in d:
            o.fuza = d['fuza']
        if 'gr' in d:
            o.gr = d['gr']
        if 'hy' in d:
            o.hy = d['hy']
        if 'll' in d:
            o.ll = d['ll']
        if 'prcides' in d:
            o.prcides = d['prcides']
        if 'stringstylea' in d:
            o.stringstylea = d['stringstylea']
        if 'stringstyleb' in d:
            o.stringstyleb = d['stringstyleb']
        return o


