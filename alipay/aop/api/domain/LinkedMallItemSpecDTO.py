#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.LinkedMallItemSpecValueDTO import LinkedMallItemSpecValueDTO


class LinkedMallItemSpecDTO(object):

    def __init__(self):
        self._key = None
        self._values = None

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, value):
        self._key = value
    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        if isinstance(value, list):
            self._values = list()
            for i in value:
                if isinstance(i, LinkedMallItemSpecValueDTO):
                    self._values.append(i)
                else:
                    self._values.append(LinkedMallItemSpecValueDTO.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.key:
            if hasattr(self.key, 'to_alipay_dict'):
                params['key'] = self.key.to_alipay_dict()
            else:
                params['key'] = self.key
        if self.values:
            if isinstance(self.values, list):
                for i in range(0, len(self.values)):
                    element = self.values[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.values[i] = element.to_alipay_dict()
            if hasattr(self.values, 'to_alipay_dict'):
                params['values'] = self.values.to_alipay_dict()
            else:
                params['values'] = self.values
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = LinkedMallItemSpecDTO()
        if 'key' in d:
            o.key = d['key']
        if 'values' in d:
            o.values = d['values']
        return o


