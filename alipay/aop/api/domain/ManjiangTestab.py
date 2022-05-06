#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ManjiangTestabc import ManjiangTestabc


class ManjiangTestab(object):

    def __init__(self):
        self._comflex_1 = None
        self._tes = None

    @property
    def comflex_1(self):
        return self._comflex_1

    @comflex_1.setter
    def comflex_1(self, value):
        self._comflex_1 = value
    @property
    def tes(self):
        return self._tes

    @tes.setter
    def tes(self, value):
        if isinstance(value, ManjiangTestabc):
            self._tes = value
        else:
            self._tes = ManjiangTestabc.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.comflex_1:
            if hasattr(self.comflex_1, 'to_alipay_dict'):
                params['comflex_1'] = self.comflex_1.to_alipay_dict()
            else:
                params['comflex_1'] = self.comflex_1
        if self.tes:
            if hasattr(self.tes, 'to_alipay_dict'):
                params['tes'] = self.tes.to_alipay_dict()
            else:
                params['tes'] = self.tes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ManjiangTestab()
        if 'comflex_1' in d:
            o.comflex_1 = d['comflex_1']
        if 'tes' in d:
            o.tes = d['tes']
        return o


