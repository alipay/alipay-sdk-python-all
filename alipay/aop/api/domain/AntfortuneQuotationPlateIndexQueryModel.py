#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AntfortuneQuotationPlateIndexQueryModel(object):

    def __init__(self):
        self._plate_id = None
        self._type = None

    @property
    def plate_id(self):
        return self._plate_id

    @plate_id.setter
    def plate_id(self, value):
        self._plate_id = value
    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value


    def to_alipay_dict(self):
        params = dict()
        if self.plate_id:
            if hasattr(self.plate_id, 'to_alipay_dict'):
                params['plate_id'] = self.plate_id.to_alipay_dict()
            else:
                params['plate_id'] = self.plate_id
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
        o = AntfortuneQuotationPlateIndexQueryModel()
        if 'plate_id' in d:
            o.plate_id = d['plate_id']
        if 'type' in d:
            o.type = d['type']
        return o


