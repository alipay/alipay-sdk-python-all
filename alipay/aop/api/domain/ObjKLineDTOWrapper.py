#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.ObjKLineDTO import ObjKLineDTO


class ObjKLineDTOWrapper(object):

    def __init__(self):
        self._data = None

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if isinstance(value, ObjKLineDTO):
            self._data = value
        else:
            self._data = ObjKLineDTO.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.data:
            if hasattr(self.data, 'to_alipay_dict'):
                params['data'] = self.data.to_alipay_dict()
            else:
                params['data'] = self.data
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ObjKLineDTOWrapper()
        if 'data' in d:
            o.data = d['data']
        return o


