#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MerchantMenber(object):

    def __init__(self):
        self._birth = None
        self._cell = None
        self._gende = None
        self._name = None

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
    @property
    def cell(self):
        return self._cell

    @cell.setter
    def cell(self, value):
        self._cell = value
    @property
    def gende(self):
        return self._gende

    @gende.setter
    def gende(self, value):
        self._gende = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    def to_alipay_dict(self):
        params = dict()
        if self.birth:
            if hasattr(self.birth, 'to_alipay_dict'):
                params['birth'] = self.birth.to_alipay_dict()
            else:
                params['birth'] = self.birth
        if self.cell:
            if hasattr(self.cell, 'to_alipay_dict'):
                params['cell'] = self.cell.to_alipay_dict()
            else:
                params['cell'] = self.cell
        if self.gende:
            if hasattr(self.gende, 'to_alipay_dict'):
                params['gende'] = self.gende.to_alipay_dict()
            else:
                params['gende'] = self.gende
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MerchantMenber()
        if 'birth' in d:
            o.birth = d['birth']
        if 'cell' in d:
            o.cell = d['cell']
        if 'gende' in d:
            o.gende = d['gende']
        if 'name' in d:
            o.name = d['name']
        return o


