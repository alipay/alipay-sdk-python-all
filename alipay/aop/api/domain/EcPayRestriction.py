#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class EcPayRestriction(object):

    def __init__(self):
        self._category = None
        self._ranges = None

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value
    @property
    def ranges(self):
        return self._ranges

    @ranges.setter
    def ranges(self, value):
        if isinstance(value, list):
            self._ranges = list()
            for i in value:
                self._ranges.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.category:
            if hasattr(self.category, 'to_alipay_dict'):
                params['category'] = self.category.to_alipay_dict()
            else:
                params['category'] = self.category
        if self.ranges:
            if isinstance(self.ranges, list):
                for i in range(0, len(self.ranges)):
                    element = self.ranges[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.ranges[i] = element.to_alipay_dict()
            if hasattr(self.ranges, 'to_alipay_dict'):
                params['ranges'] = self.ranges.to_alipay_dict()
            else:
                params['ranges'] = self.ranges
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = EcPayRestriction()
        if 'category' in d:
            o.category = d['category']
        if 'ranges' in d:
            o.ranges = d['ranges']
        return o


