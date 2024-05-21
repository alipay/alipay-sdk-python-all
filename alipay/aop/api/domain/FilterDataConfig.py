#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.FilterChildDataConfig import FilterChildDataConfig


class FilterDataConfig(object):

    def __init__(self):
        self._options = None

    @property
    def options(self):
        return self._options

    @options.setter
    def options(self, value):
        if isinstance(value, list):
            self._options = list()
            for i in value:
                if isinstance(i, FilterChildDataConfig):
                    self._options.append(i)
                else:
                    self._options.append(FilterChildDataConfig.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.options:
            if isinstance(self.options, list):
                for i in range(0, len(self.options)):
                    element = self.options[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.options[i] = element.to_alipay_dict()
            if hasattr(self.options, 'to_alipay_dict'):
                params['options'] = self.options.to_alipay_dict()
            else:
                params['options'] = self.options
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = FilterDataConfig()
        if 'options' in d:
            o.options = d['options']
        return o


