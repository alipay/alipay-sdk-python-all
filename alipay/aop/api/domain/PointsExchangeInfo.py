#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class PointsExchangeInfo(object):

    def __init__(self):
        self._ids = None
        self._type = None

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if isinstance(value, list):
            self._ids = list()
            for i in value:
                self._ids.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.ids:
            if isinstance(self.ids, list):
                for i in range(0, len(self.ids)):
                    element = self.ids[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ids[i] = element.to_alipay_dict()
            if hasattr(self.ids, 'to_alipay_dict'):
                params['ids'] = self.ids.to_alipay_dict()
            else:
                params['ids'] = self.ids
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
        o = PointsExchangeInfo()
        if 'ids' in d:
            o.ids = d['ids']
        if 'type' in d:
            o.type = d['type']
        return o


