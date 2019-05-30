#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SupplierAssetResponse import SupplierAssetResponse


class AlipayCommerceIotSupplierAssetModifyModel(object):

    def __init__(self):
        self._record = None

    @property
    def record(self):
        return self._record

    @record.setter
    def record(self, value):
        if isinstance(value, SupplierAssetResponse):
            self._record = value
        else:
            self._record = SupplierAssetResponse.from_alipay_dict(value)


    def to_alipay_dict(self):
        params = dict()
        if self.record:
            if hasattr(self.record, 'to_alipay_dict'):
                params['record'] = self.record.to_alipay_dict()
            else:
                params['record'] = self.record
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceIotSupplierAssetModifyModel()
        if 'record' in d:
            o.record = d['record']
        return o


