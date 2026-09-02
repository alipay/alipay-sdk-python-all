#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class AlipayCommerceLifeserviceRedemptionQueryModel(object):

    def __init__(self):
        self._redemption_code = None

    @property
    def redemption_code(self):
        return self._redemption_code

    @redemption_code.setter
    def redemption_code(self, value):
        self._redemption_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.redemption_code:
            if hasattr(self.redemption_code, 'to_alipay_dict'):
                params['redemption_code'] = self.redemption_code.to_alipay_dict()
            else:
                params['redemption_code'] = self.redemption_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayCommerceLifeserviceRedemptionQueryModel()
        if 'redemption_code' in d:
            o.redemption_code = d['redemption_code']
        return o


