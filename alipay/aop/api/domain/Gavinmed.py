#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.GavintestNewLeveaOne import GavintestNewLeveaOne


class Gavinmed(object):

    def __init__(self):
        self._meds = None
        self._str = None

    @property
    def meds(self):
        return self._meds

    @meds.setter
    def meds(self, value):
        if isinstance(value, list):
            self._meds = list()
            for i in value:
                if isinstance(i, GavintestNewLeveaOne):
                    self._meds.append(i)
                else:
                    self._meds.append(GavintestNewLeveaOne.from_alipay_dict(i))
    @property
    def str(self):
        return self._str

    @str.setter
    def str(self, value):
        self._str = value


    def to_alipay_dict(self):
        params = dict()
        if self.meds:
            if isinstance(self.meds, list):
                for i in range(0, len(self.meds)):
                    element = self.meds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.meds[i] = element.to_alipay_dict()
            if hasattr(self.meds, 'to_alipay_dict'):
                params['meds'] = self.meds.to_alipay_dict()
            else:
                params['meds'] = self.meds
        if self.str:
            if hasattr(self.str, 'to_alipay_dict'):
                params['str'] = self.str.to_alipay_dict()
            else:
                params['str'] = self.str
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Gavinmed()
        if 'meds' in d:
            o.meds = d['meds']
        if 'str' in d:
            o.str = d['str']
        return o


