#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *


class RentSignFundAuthFreezeInfoDTO(object):

    def __init__(self):
        self._risk_assessment_price = None
        self._risk_scheme_id = None

    @property
    def risk_assessment_price(self):
        return self._risk_assessment_price

    @risk_assessment_price.setter
    def risk_assessment_price(self, value):
        self._risk_assessment_price = value
    @property
    def risk_scheme_id(self):
        return self._risk_scheme_id

    @risk_scheme_id.setter
    def risk_scheme_id(self, value):
        self._risk_scheme_id = value


    def to_alipay_dict(self):
        params = dict()
        if self.risk_assessment_price:
            if hasattr(self.risk_assessment_price, 'to_alipay_dict'):
                params['risk_assessment_price'] = self.risk_assessment_price.to_alipay_dict()
            else:
                params['risk_assessment_price'] = self.risk_assessment_price
        if self.risk_scheme_id:
            if hasattr(self.risk_scheme_id, 'to_alipay_dict'):
                params['risk_scheme_id'] = self.risk_scheme_id.to_alipay_dict()
            else:
                params['risk_scheme_id'] = self.risk_scheme_id
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = RentSignFundAuthFreezeInfoDTO()
        if 'risk_assessment_price' in d:
            o.risk_assessment_price = d['risk_assessment_price']
        if 'risk_scheme_id' in d:
            o.risk_scheme_id = d['risk_scheme_id']
        return o


