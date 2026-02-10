#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EpRatioInfo(object):

    def __init__(self):
        self._crn = None
        self._name = None
        self._ratio = None

    @property
    def crn(self):
        return self._crn

    @crn.setter
    def crn(self, value):
        self._crn = value
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    @property
    def ratio(self):
        return self._ratio

    @ratio.setter
    def ratio(self, value):
        self._ratio = value


    def to_alipay_dict(self):
        params = dict()
        if self.crn:
            if hasattr(self.crn, 'to_alipay_dict'):
                params['crn'] = self.crn.to_alipay_dict()
            else:
                params['crn'] = self.crn
        if self.name:
            if hasattr(self.name, 'to_alipay_dict'):
                params['name'] = self.name.to_alipay_dict()
            else:
                params['name'] = self.name
        if self.ratio:
            if hasattr(self.ratio, 'to_alipay_dict'):
                params['ratio'] = self.ratio.to_alipay_dict()
            else:
                params['ratio'] = self.ratio
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EpRatioInfo()
        if 'crn' in d:
            o.crn = d['crn']
        if 'name' in d:
            o.name = d['name']
        if 'ratio' in d:
            o.ratio = d['ratio']
        return o


