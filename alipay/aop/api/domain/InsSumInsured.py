#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class InsSumInsured(object):

    def __init__(self):
        self._default_value = None
        self._max_value = None
        self._min_value = None
        self._sum_insured_type = None
        self._sum_insureds = None

    @property
    def default_value(self):
        return self._default_value

    @default_value.setter
    def default_value(self, value):
        self._default_value = value
    @property
    def max_value(self):
        return self._max_value

    @max_value.setter
    def max_value(self, value):
        self._max_value = value
    @property
    def min_value(self):
        return self._min_value

    @min_value.setter
    def min_value(self, value):
        self._min_value = value
    @property
    def sum_insured_type(self):
        return self._sum_insured_type

    @sum_insured_type.setter
    def sum_insured_type(self, value):
        self._sum_insured_type = value
    @property
    def sum_insureds(self):
        return self._sum_insureds

    @sum_insureds.setter
    def sum_insureds(self, value):
        if isinstance(value, list):
            self._sum_insureds = list()
            for i in value:
                self._sum_insureds.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.default_value:
            if hasattr(self.default_value, 'to_alipay_dict'):
                params['default_value'] = self.default_value.to_alipay_dict()
            else:
                params['default_value'] = self.default_value
        if self.max_value:
            if hasattr(self.max_value, 'to_alipay_dict'):
                params['max_value'] = self.max_value.to_alipay_dict()
            else:
                params['max_value'] = self.max_value
        if self.min_value:
            if hasattr(self.min_value, 'to_alipay_dict'):
                params['min_value'] = self.min_value.to_alipay_dict()
            else:
                params['min_value'] = self.min_value
        if self.sum_insured_type:
            if hasattr(self.sum_insured_type, 'to_alipay_dict'):
                params['sum_insured_type'] = self.sum_insured_type.to_alipay_dict()
            else:
                params['sum_insured_type'] = self.sum_insured_type
        if self.sum_insureds:
            if isinstance(self.sum_insureds, list):
                for i in range(0, len(self.sum_insureds)):
                    element = self.sum_insureds[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.sum_insureds[i] = element.to_alipay_dict()
            if hasattr(self.sum_insureds, 'to_alipay_dict'):
                params['sum_insureds'] = self.sum_insureds.to_alipay_dict()
            else:
                params['sum_insureds'] = self.sum_insureds
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = InsSumInsured()
        if 'default_value' in d:
            o.default_value = d['default_value']
        if 'max_value' in d:
            o.max_value = d['max_value']
        if 'min_value' in d:
            o.min_value = d['min_value']
        if 'sum_insured_type' in d:
            o.sum_insured_type = d['sum_insured_type']
        if 'sum_insureds' in d:
            o.sum_insureds = d['sum_insureds']
        return o


