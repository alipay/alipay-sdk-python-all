#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.DataEntry import DataEntry
from alipay.aop.api.domain.DataDim import DataDim


class Datas(object):

    def __init__(self):
        self._data = None
        self._dimension = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, list):
            self._data = list()
            for i in value:
                if isinstance(i, DataEntry):
                    self._data.append(i)
                else:
                    self._data.append(DataEntry.from_alipay_dict(i))
    @property
    def dimension(self):
        return self._dimension

    @dimension.setter
    def dimension(self, value):
        if isinstance(value, list):
            self._dimension = list()
            for i in value:
                if isinstance(i, DataDim):
                    self._dimension.append(i)
                else:
                    self._dimension.append(DataDim.from_alipay_dict(i))


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if isinstance(self.data, list):
                for i in range(0, len(self.data)):
                    element = self.data[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.data[i] = element.to_alipay_dict()
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        if self.dimension:
            if isinstance(self.dimension, list):
                for i in range(0, len(self.dimension)):
                    element = self.dimension[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.dimension[i] = element.to_alipay_dict()
            if hasattr(self.dimension, 'to_alipay_dict'):
                params['dimension'] = self.dimension.to_alipay_dict()
            else:
                params['dimension'] = self.dimension
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = Datas()
        if 'data' in d:
            o.data = d['data']
        if 'dimension' in d:
            o.dimension = d['dimension']
        return o


