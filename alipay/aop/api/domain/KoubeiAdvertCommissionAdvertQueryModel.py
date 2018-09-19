#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class KoubeiAdvertCommissionAdvertQueryModel(object):

    def __init__(self):
        self._identifies = None
        self._identify_type = None

    @property
    def identifies(self):
        return self._identifies

    @identifies.setter
    def identifies(self, value):
        if isinstance(value, list):
            self._identifies = list()
            for i in value:
                self._identifies.append(i)
    @property
    def identify_type(self):
        return self._identify_type

    @identify_type.setter
    def identify_type(self, value):
        self._identify_type = value


    def to_alipay_dict(self):
        params = dict()
        if self.identifies:
            if isinstance(self.identifies, list):
                for i in range(0, len(self.identifies)):
                    element = self.identifies[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.identifies[i] = element.to_alipay_dict()
            if hasattr(self.identifies, 'to_alipay_dict'):
                params['identifies'] = self.identifies.to_alipay_dict()
            else:
                params['identifies'] = self.identifies
        if self.identify_type:
            if hasattr(self.identify_type, 'to_alipay_dict'):
                params['identify_type'] = self.identify_type.to_alipay_dict()
            else:
                params['identify_type'] = self.identify_type
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = KoubeiAdvertCommissionAdvertQueryModel()
        if 'identifies' in d:
            o.identifies = d['identifies']
        if 'identify_type' in d:
            o.identify_type = d['identify_type']
        return o


