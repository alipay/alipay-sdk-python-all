#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class ShipGoodsRiskVO(object):

    def __init__(self):
        self._can_ship_flag = None
        self._risk_code = None

    @property
    def can_ship_flag(self):
        return self._can_ship_flag

    @can_ship_flag.setter
    def can_ship_flag(self, value):
        self._can_ship_flag = value
    @property
    def risk_code(self):
        return self._risk_code

    @risk_code.setter
    def risk_code(self, value):
        self._risk_code = value


    def to_alipay_dict(self):
        params = dict()
        if self.can_ship_flag:
            if hasattr(self.can_ship_flag, 'to_alipay_dict'):
                params['can_ship_flag'] = self.can_ship_flag.to_alipay_dict()
            else:
                params['can_ship_flag'] = self.can_ship_flag
        if self.risk_code:
            if hasattr(self.risk_code, 'to_alipay_dict'):
                params['risk_code'] = self.risk_code.to_alipay_dict()
            else:
                params['risk_code'] = self.risk_code
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = ShipGoodsRiskVO()
        if 'can_ship_flag' in d:
            o.can_ship_flag = d['can_ship_flag']
        if 'risk_code' in d:
            o.risk_code = d['risk_code']
        return o


