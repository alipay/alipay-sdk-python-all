#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ScopeInfo(object):

    def __init__(self):
        self._circular_area = None
        self._polygon_area = None
        self._type = None

    @property
    def circular_area(self):
        return self._circular_area

    @circular_area.setter
    def circular_area(self, value):
        self._circular_area = value
    @property
    def polygon_area(self):
        return self._polygon_area

    @polygon_area.setter
    def polygon_area(self, value):
        if isinstance(value, list):
            self._polygon_area = list()
            for i in value:
                self._polygon_area.append(i)
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.circular_area:
            if hasattr(self.circular_area, 'to_alipay_dict'):
                params['circular_area'] = self.circular_area.to_alipay_dict()
            else:
                params['circular_area'] = self.circular_area
        if self.polygon_area:
            if isinstance(self.polygon_area, list):
                for i in range(0, len(self.polygon_area)):
                    element = self.polygon_area[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.polygon_area[i] = element.to_alipay_dict()
            if hasattr(self.polygon_area, 'to_alipay_dict'):
                params['polygon_area'] = self.polygon_area.to_alipay_dict()
            else:
                params['polygon_area'] = self.polygon_area
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
        o = ScopeInfo()
        if 'circular_area' in d:
            o.circular_area = d['circular_area']
        if 'polygon_area' in d:
            o.polygon_area = d['polygon_area']
        if 'type' in d:
            o.type = d['type']
        return o


