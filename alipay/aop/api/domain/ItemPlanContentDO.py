#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ItemPlanContentDO(object):

    def __init__(self):
        self._codes = None
        self._type = None

    @property
    def codes(self):
        return self._codes

    @codes.setter
    def codes(self, value):
        if isinstance(value, list):
            self._codes = list()
            for i in value:
                self._codes.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.codes:
            if isinstance(self.codes, list):
                for i in range(0, len(self.codes)):
                    element = self.codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.codes[i] = element.to_alipay_dict()
            if hasattr(self.codes, 'to_alipay_dict'):
                params['codes'] = self.codes.to_alipay_dict()
            else:
                params['codes'] = self.codes
        if self.type:
            if hasattr(self.type, 'to_alipay_dict'):
                params['type'] = self.type.to_alipay_dict()
            else:
                params['type'] = self.type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ItemPlanContentDO()
        if 'codes' in d:
            o.codes = d['codes']
        if 'type' in d:
            o.type = d['type']
        return o


