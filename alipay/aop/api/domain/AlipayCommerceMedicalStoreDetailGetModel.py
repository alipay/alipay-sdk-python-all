#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceMedicalStoreDetailGetModel(object):

    def __init__(self):
        self._store_codes = None

    @property
    def store_codes(self):
        return self._store_codes

    @store_codes.setter
    def store_codes(self, value):
        if isinstance(value, list):
            self._store_codes = list()
            for i in value:
                self._store_codes.append(i)


    def to_alipay_dict(self):
        params = dict()
        if self.store_codes:
            if isinstance(self.store_codes, list):
                for i in range(0, len(self.store_codes)):
                    element = self.store_codes[i]
                    if hasattr(element, 'to_alipay_dict'):
                        self.store_codes[i] = element.to_alipay_dict()
            if hasattr(self.store_codes, 'to_alipay_dict'):
                params['store_codes'] = self.store_codes.to_alipay_dict()
            else:
                params['store_codes'] = self.store_codes
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceMedicalStoreDetailGetModel()
        if 'store_codes' in d:
            o.store_codes = d['store_codes']
        return o


