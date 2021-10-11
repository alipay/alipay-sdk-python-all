#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayTradeContractQuicksettlementQueryModel(object):

    def __init__(self):
        self._secondary_merchant_id = None

    @property
    def secondary_merchant_id(self):
        return self._secondary_merchant_id

    @secondary_merchant_id.setter
    def secondary_merchant_id(self, value):
        self._secondary_merchant_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.secondary_merchant_id:
            if hasattr(self.secondary_merchant_id, 'to_alipay_dict'):
                params['secondary_merchant_id'] = self.secondary_merchant_id.to_alipay_dict()
            else:
                params['secondary_merchant_id'] = self.secondary_merchant_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeContractQuicksettlementQueryModel()
        if 'secondary_merchant_id' in d:
            o.secondary_merchant_id = d['secondary_merchant_id']
        return o


