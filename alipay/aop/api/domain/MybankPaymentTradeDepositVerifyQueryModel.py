#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class MybankPaymentTradeDepositVerifyQueryModel(object):

    def __init__(self):
        self._verify_id = None

    @property
    def verify_id(self):
        return self._verify_id

    @verify_id.setter
    def verify_id(self, value):
        self._verify_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.verify_id:
            if hasattr(self.verify_id, 'to_alipay_dict'):
                params['verify_id'] = self.verify_id.to_alipay_dict()
            else:
                params['verify_id'] = self.verify_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = MybankPaymentTradeDepositVerifyQueryModel()
        if 'verify_id' in d:
            o.verify_id = d['verify_id']
        return o


