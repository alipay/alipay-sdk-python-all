#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayOpenSearchBoxQueryModel(object):

    def __init__(self):
        self._box_id = None
        self._merchant_id = None

    @property
    def box_id(self):
        return self._box_id

    @box_id.setter
    def box_id(self, value):
        self._box_id = value
    @property
    def merchant_id(self):
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, value):
        self._merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.box_id:
            if hasattr(self.box_id, 'to_alipay_dict'):
                params['box_id'] = self.box_id.to_alipay_dict()
            else:
                params['box_id'] = self.box_id
        if self.merchant_id:
            if hasattr(self.merchant_id, 'to_alipay_dict'):
                params['merchant_id'] = self.merchant_id.to_alipay_dict()
            else:
                params['merchant_id'] = self.merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayOpenSearchBoxQueryModel()
        if 'box_id' in d:
            o.box_id = d['box_id']
        if 'merchant_id' in d:
            o.merchant_id = d['merchant_id']
        return o


