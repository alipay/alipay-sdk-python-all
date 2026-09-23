#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

from alipay.aop.api.constant.ParamConstants import *
from alipay.aop.api.domain.SaasBuyerInfo import SaasBuyerInfo


class AlipayTradeSaasEbankConsultModel(object):

    def __init__(self):
        self._buyer_info = None
        self._total_amount = None

    @property
    def buyer_info(self):
        return self._buyer_info

    @buyer_info.setter
    def buyer_info(self, value):
        if isinstance(value, SaasBuyerInfo):
            self._buyer_info = value
        else:
            self._buyer_info = SaasBuyerInfo.from_alipay_dict(value)
    @property
    def total_amount(self):
        return self._total_amount

    @total_amount.setter
    def total_amount(self, value):
        self._total_amount = value


    def to_alipay_dict(self):
        params = dict()
        if self.buyer_info:
            if hasattr(self.buyer_info, 'to_alipay_dict'):
                params['buyer_info'] = self.buyer_info.to_alipay_dict()
            else:
                params['buyer_info'] = self.buyer_info
        if self.total_amount:
            if hasattr(self.total_amount, 'to_alipay_dict'):
                params['total_amount'] = self.total_amount.to_alipay_dict()
            else:
                params['total_amount'] = self.total_amount
        return params

    @staticmethod
    def from_alipay_dict(d):
        if not d:
            return None
        o = AlipayTradeSaasEbankConsultModel()
        if 'buyer_info' in d:
            o.buyer_info = d['buyer_info']
        if 'total_amount' in d:
            o.total_amount = d['total_amount']
        return o


